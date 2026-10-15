/*
 * DS18B20 calibration test - ISEF 26 PCM project
 *
 * One-point (offset) calibration against an ice slurry (0.00 C), plus two
 * check points that are kept OUT of the fit:
 *   room  - water at room temperature
 *   warm  - hot water at ~50-60 C in a thermos or insulated mug, i.e. at
 *           field-test temperatures (optional, no boiling needed)
 * All probes sit in the same bath, so the check points need no reference
 * thermometer: after the ice offset is applied the probes should agree, and
 * how far they still disagree is the sensor-to-sensor uncertainty.
 *
 * What it does for you
 *   - waits until the probes have settled, then averages 10 readings per probe
 *   - keys every result to the probe's 64-bit address, not its bus index, so the
 *     corrections still apply after the probes are split across the field rigs
 *   - saves each capture to EEPROM: opening the port resets the Uno, and this
 *     way a reset between baths does not lose the ice point
 *   - prints offsets, the held-out residual spread (the number that goes in the
 *     paper) and a paste-ready correction table
 *
 * Wiring: all probes in parallel on D2, 4.7k pull-up from D2 to 5V, VDD to 5V.
 * Serial Monitor at 9600 baud. Any line-ending setting works.
 *
 * Commands (type the letter, press Enter)
 *   i  capture ice point          r  capture room check point
 *   w  capture warm check point   f  capture now, skip the settle wait
 *   a  abort a capture            c  compute and print the corrections
 *   l  list stored captures       x  clear stored captures (asks for y)
 *   h  help
 *
 * Output: data rows start with a digit:
 *   elapsed_s,phase,S0..Sn,mean,spread,spread_cal
 * spread_cal is blank until the ice point is captured. Every other line is a
 * note. serial_logger.py records both.
 */

#include <OneWire.h>
#include <DallasTemperature.h>
#include <EEPROM.h>
#include <string.h>

const int ONE_WIRE_BUS = 2;
const uint8_t MAX_SENSORS = 10;
const uint8_t EXPECTED_SENSORS = 4;     // a warning only
const unsigned long PERIOD_MS = 2000;   // one row every 2 s, as in ds18b20_calibrate.ino
const uint8_t N_CAPTURE = 10;           // readings averaged per point (paper section 3.8)
const uint8_t N_SETTLE = 10;            // settle window, in readings (20 s)
const float SETTLE_BAND = 0.125;        // 2 LSB over the window
const float SD_WARN = 0.10;             // flag a capture noisier than this
const float ICE_REF = 0.00;

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

enum Point : uint8_t { ICE, ROOM, WARM, N_POINTS };
const char *const POINT_NAME[N_POINTS] = {"ice", "room", "warm"};

struct Rec {
  DeviceAddress addr;
  uint8_t have;                         // bit p set = point p captured
  float mean[N_POINTS];
  float sd[N_POINTS];
};

Rec cal[MAX_SENSORS];
uint8_t nDev = 0;

// EEPROM layout: Header, then one Rec per probe
const uint16_t MAGIC = 0xCA1C;
struct Header { uint16_t magic; uint8_t n; };
const int REC_BASE = sizeof(Header);

enum Mode : uint8_t { IDLE, SETTLING, CAPTURING };
Mode mode = IDLE;
Point target = ICE;
uint8_t nCap = 0, settleRows = 0;
float capK[MAX_SENSORS], capS1[MAX_SENSORS], capS2[MAX_SENSORS];

float hist[MAX_SENSORS][N_SETTLE];
uint8_t histPos = 0, histFill = 0;

bool confirmClear = false;
unsigned long nextRead = 0;

// ---------------------------------------------------------------- helpers

void printAddress(const uint8_t *a) {
  for (uint8_t i = 0; i < 8; i++) {
    if (a[i] < 16) Serial.print('0');
    Serial.print(a[i], HEX);
  }
}

void printProbe(uint8_t i) {
  Serial.print(F("# S"));
  Serial.print(i);
  Serial.print(' ');
  printAddress(cal[i].addr);
}

// -127 = disconnected, 85.0 exactly = power-on value, conversion never ran
bool valid(float t) { return t > -100.0 && t != 85.0; }

bool has(uint8_t i, Point p) { return cal[i].have & (1 << p); }

bool allHave(Point p) {
  for (uint8_t i = 0; i < nDev; i++)
    if (!has(i, p)) return false;
  return nDev > 0;
}

bool inWindow(Point p, float m) {
  switch (p) {
    case ICE:  return m > ICE_REF - 2.0 && m < ICE_REF + 2.0;
    case ROOM: return m > 10.0 && m < 40.0;
    default:   return m > 35.0 && m < 80.0;
  }
}

float offsetOf(uint8_t i) { return ICE_REF - cal[i].mean[ICE]; }

// ---------------------------------------------------------------- EEPROM

void saveAll() {
  Header h = {MAGIC, nDev};
  EEPROM.put(0, h);
  for (uint8_t i = 0; i < nDev; i++) EEPROM.put(REC_BASE + i * sizeof(Rec), cal[i]);
}

void loadAll() {
  Header h;
  EEPROM.get(0, h);
  if (h.magic != MAGIC || h.n > MAX_SENSORS) return;

  uint8_t matched = 0;
  for (uint8_t k = 0; k < h.n; k++) {
    Rec r;
    EEPROM.get(REC_BASE + k * sizeof(Rec), r);
    for (uint8_t i = 0; i < nDev; i++) {
      if (memcmp(r.addr, cal[i].addr, 8) == 0) {
        cal[i] = r;
        if (r.have) matched++;
        break;
      }
    }
  }
  if (matched) {
    Serial.print(F("# restored stored captures for "));
    Serial.print(matched);
    Serial.println(F(" probe(s) - type x to start fresh"));
    listCaptures();
  }
}

// ---------------------------------------------------------------- result

// spread of the per-probe means at point p, raw or offset-corrected
float spreadOf(Point p, bool corrected) {
  float lo = 999, hi = -999;
  for (uint8_t i = 0; i < nDev; i++) {
    float v = cal[i].mean[p] + (corrected ? offsetOf(i) : 0);
    if (v < lo) lo = v;
    if (v > hi) hi = v;
  }
  return hi - lo;
}

void printCheck(Point p) {
  Serial.print(F("# "));
  Serial.print(POINT_NAME[p]);
  Serial.print(F(" check (held out of the fit): raw spread "));
  Serial.print(spreadOf(p, false), 4);
  Serial.print(F(" C, corrected spread "));
  Serial.print(spreadOf(p, true), 4);
  Serial.println(F(" C"));
}

void compute() {
  if (!allHave(ICE)) {
    Serial.println(F("# cannot compute yet - capture the ice point (i) first"));
    return;
  }

  Serial.println(F("#"));
  Serial.println(F("# ================= calibration result ================="));
  Serial.println(F("# one-point offset against ice 0.00 C.  corrected = raw + offset"));
  Serial.println(F("# probe address           ice_mean ice_sd  offset"));
  for (uint8_t i = 0; i < nDev; i++) {
    printProbe(i);
    Serial.print(F("  "));
    Serial.print(cal[i].mean[ICE], 4);
    Serial.print(F("  "));
    Serial.print(cal[i].sd[ICE], 4);
    Serial.print(F("  "));
    if (offsetOf(i) >= 0) Serial.print('+');
    Serial.println(offsetOf(i), 4);
  }
  Serial.print(F("# raw spread at ice: "));
  Serial.print(spreadOf(ICE, false), 4);
  Serial.println(F(" C (0 after correction by construction - it was used in the fit)"));

  bool anyCheck = false;
  float worst = 0;
  for (uint8_t p = ROOM; p < N_POINTS; p++) {
    if (!allHave((Point)p)) continue;
    printCheck((Point)p);
    float s = spreadOf((Point)p, true);
    if (s > worst) worst = s;
    anyCheck = true;
  }
  if (anyCheck) {
    Serial.print(F("# -> sensor-to-sensor uncertainty to report: "));
    Serial.print(worst, 4);
    Serial.println(F(" C (the larger check spread)"));
  } else {
    Serial.println(F("# no check point yet - capture room (r) and/or warm (w) for an honest residual"));
  }
  if (!allHave(WARM))
    Serial.println(F("# no warm point: agreement at field temperatures (40-70 C) is untested"));

  // paste-ready table for field_logger.ino / thermal_chamber.ino
  Serial.println(F("# ---------- paste block start ----------"));
  Serial.println(F("// DS18B20 one-point calibration, ice 0.00 C.  corrected = raw + offset"));
  Serial.println(F("struct SensorCal { uint8_t addr[8]; float offset; };"));
  Serial.println(F("const SensorCal CAL[] = {"));
  for (uint8_t i = 0; i < nDev; i++) {
    Serial.print(F("  {{"));
    for (uint8_t b = 0; b < 8; b++) {
      Serial.print(F("0x"));
      if (cal[i].addr[b] < 16) Serial.print('0');
      Serial.print(cal[i].addr[b], HEX);
      if (b < 7) Serial.print(',');
    }
    Serial.print(F("}, "));
    Serial.print(offsetOf(i), 4);
    Serial.print(F("f},  // S"));
    Serial.println(i);
  }
  Serial.println(F("};"));
  Serial.println(F("const uint8_t N_CAL = sizeof(CAL) / sizeof(CAL[0]);"));
  Serial.println(F("// look up by address, so it works whichever rig and bus index a probe is on"));
  Serial.println(F("float calibrate(const uint8_t *addr, float raw) {"));
  Serial.println(F("  if (raw <= -100.0) return raw;                // disconnected, leave as -127"));
  Serial.println(F("  for (uint8_t k = 0; k < N_CAL; k++)"));
  Serial.println(F("    if (memcmp(addr, CAL[k].addr, 8) == 0) return raw + CAL[k].offset;"));
  Serial.println(F("  return NAN;                                    // probe was never calibrated"));
  Serial.println(F("}"));
  Serial.println(F("# ---------- paste block end ----------"));

  // one line per probe for the notebook / spreadsheet
  Serial.println(F("#CAL,probe,address,ice_mean,ice_sd,offset,room_mean,room_corrected,warm_mean,warm_corrected"));
  for (uint8_t i = 0; i < nDev; i++) {
    Serial.print(F("#CAL,S"));
    Serial.print(i);
    Serial.print(',');
    printAddress(cal[i].addr);
    Serial.print(',');
    Serial.print(cal[i].mean[ICE], 4);
    Serial.print(',');
    Serial.print(cal[i].sd[ICE], 4);
    Serial.print(',');
    Serial.print(offsetOf(i), 4);
    for (uint8_t p = ROOM; p < N_POINTS; p++) {
      Serial.print(',');
      if (has(i, (Point)p)) {
        Serial.print(cal[i].mean[p], 4);
        Serial.print(',');
        Serial.print(cal[i].mean[p] + offsetOf(i), 4);
      } else {
        Serial.print(',');
      }
    }
    Serial.println();
  }
  Serial.println(F("# ======================================================"));
}

// ---------------------------------------------------------------- capture

void startCapture(Point p) {
  if (nDev == 0) {
    Serial.println(F("# no probes on the bus"));
    return;
  }
  target = p;
  mode = SETTLING;
  histFill = histPos = settleRows = 0;
  Serial.print(F("# "));
  Serial.print(POINT_NAME[p]);
  if (p == WARM)
    Serial.print(F(": warm water cools, so this waits for the probes to AGREE steadily (within "));
  else
    Serial.print(F(": waiting for every probe to settle (range <= "));
  Serial.print(SETTLE_BAND, 3);
  Serial.print(F(" C over "));
  Serial.print(N_SETTLE);
  Serial.println(F(" readings). f = capture now, a = abort"));
}

void beginCapturing(bool forced) {
  mode = CAPTURING;
  nCap = 0;
  Serial.print(F("# "));
  Serial.print(forced ? F("forced") : F("settled"));
  Serial.print(F(" - averaging "));
  Serial.print(N_CAPTURE);
  Serial.print(F(" readings for "));
  Serial.println(POINT_NAME[target]);
}

void finishCapture() {
  float m[MAX_SENSORS], s[MAX_SENSORS];
  bool allIn = true;
  for (uint8_t i = 0; i < nDev; i++) {
    m[i] = capK[i] + capS1[i] / N_CAPTURE;
    float var = (capS2[i] - capS1[i] * capS1[i] / N_CAPTURE) / (N_CAPTURE - 1);
    s[i] = var > 0 ? sqrt(var) : 0;
    printProbe(i);
    Serial.print(' ');
    Serial.print(POINT_NAME[target]);
    Serial.print(F("  mean "));
    Serial.print(m[i], 4);
    Serial.print(F("  sd "));
    Serial.print(s[i], 4);
    if (!inWindow(target, m[i])) {
      Serial.print(F("  <- outside the expected range"));
      allIn = false;
    } else if (s[i] > SD_WARN && target != WARM) {   // warm water is meant to drift
      Serial.print(F("  <- noisy, bath moving?"));
    }
    Serial.println();
  }
  mode = IDLE;

  if (!allIn) {
    Serial.print(F("# NOT SAVED. "));
    if (target == ICE) Serial.println(F("Ice should read near 0 C: crushed-ice slurry, stirred, bundle buried in it."));
    else if (target == ROOM) Serial.println(F("Room water should be 10-40 C."));
    else Serial.println(F("Warm water should be 35-80 C."));
    Serial.println(F("# One probe far off while the rest look right = suspect that probe."));
    return;
  }

  float lo = 999, hi = -999;
  for (uint8_t i = 0; i < nDev; i++) {
    cal[i].mean[target] = m[i];
    cal[i].sd[target] = s[i];
    cal[i].have |= (1 << target);
    if (m[i] < lo) lo = m[i];
    if (m[i] > hi) hi = m[i];
  }
  saveAll();

  Serial.print(F("# "));
  Serial.print(POINT_NAME[target]);
  Serial.print(F(" saved. raw spread "));
  Serial.print(hi - lo, 4);
  Serial.println(F(" C"));
  if (!allHave(ICE)) Serial.println(F("# next: ice bath, then i"));
  else if (!allHave(ROOM)) Serial.println(F("# next: room-temperature water, then r"));
  else if (!allHave(WARM)) Serial.println(F("# next: warm water (optional), then w - or c to compute now"));
  else Serial.println(F("# all three points in - type c"));
}

// largest change over the settle window. For ice and room: of each probe's own
// reading. For warm: of each probe's difference from the bundle mean, so a bath
// that cools steadily still counts as settled once the probes track each other.
float worstMovement(uint8_t &wi) {
  float worst = 0;
  for (uint8_t i = 0; i < nDev; i++) {
    float lo = 999, hi = -999;
    for (uint8_t k = 0; k < N_SETTLE; k++) {
      float v = hist[i][k];
      if (target == WARM) {
        float mean = 0;
        for (uint8_t j = 0; j < nDev; j++) mean += hist[j][k];
        v -= mean / nDev;
      }
      if (v < lo) lo = v;
      if (v > hi) hi = v;
    }
    if (hi - lo > worst) { worst = hi - lo; wi = i; }
  }
  return worst;
}

void stepCapture(const float *t, bool ok) {
  if (mode == IDLE) return;

  if (!ok) {
    if (mode == CAPTURING) {
      mode = IDLE;
      Serial.println(F("# capture aborted: a probe read -127 or 85.0 - check its wiring, then retry"));
    } else {
      histFill = histPos = 0;           // restart the settle window
    }
    return;
  }

  if (mode == SETTLING) {
    if (histFill < N_SETTLE) return;
    uint8_t wi = 0;
    float worst = worstMovement(wi);
    if (worst <= SETTLE_BAND) {
      beginCapturing(false);
    } else if (++settleRows % 5 == 1) {
      Serial.print(F("# settling: S"));
      Serial.print(wi);
      Serial.print(F(" still moving, range "));
      Serial.print(worst, 3);
      Serial.println(F(" C"));
    }
    return;
  }

  // CAPTURING: shifted sums keep the variance accurate in float
  for (uint8_t i = 0; i < nDev; i++) {
    if (nCap == 0) {
      capK[i] = t[i];
      capS1[i] = capS2[i] = 0;
    }
    float d = t[i] - capK[i];
    capS1[i] += d;
    capS2[i] += d * d;
  }
  if (++nCap >= N_CAPTURE) finishCapture();
}

// ---------------------------------------------------------------- commands

void listCaptures() {
  Serial.println(F("# stored captures:"));
  for (uint8_t i = 0; i < nDev; i++) {
    printProbe(i);
    for (uint8_t p = 0; p < N_POINTS; p++) {
      Serial.print(F("  "));
      Serial.print(POINT_NAME[p]);
      Serial.print(' ');
      if (has(i, (Point)p)) Serial.print(cal[i].mean[p], 4);
      else Serial.print(F("--"));
    }
    Serial.println();
  }
}

void clearAll() {
  for (uint8_t i = 0; i < nDev; i++) cal[i].have = 0;
  mode = IDLE;
  saveAll();
  Serial.println(F("# all stored captures cleared"));
}

void printHelp() {
  Serial.println(F("# commands: i ice   r room check   w warm check   f capture now   a abort"));
  Serial.println(F("#           c compute   l list   x clear   h help"));
  Serial.println(F("# order: bundle the tips -> ice, i -> room water, r -> (warm water, w) -> c"));
}

void handleSerial() {
  while (Serial.available()) {
    char c = tolower(Serial.read());
    if (c == '\r' || c == '\n' || c == ' ') continue;

    if (confirmClear) {
      confirmClear = false;
      if (c == 'y') clearAll();
      else Serial.println(F("# clear cancelled"));
      continue;
    }

    switch (c) {
      case 'i': startCapture(ICE); break;
      case 'r': startCapture(ROOM); break;
      case 'w': startCapture(WARM); break;
      case 'f':
        if (mode == SETTLING) beginCapturing(true);
        else Serial.println(F("# nothing to force - type i, r or w first"));
        break;
      case 'a':
        if (mode != IDLE) Serial.println(F("# capture aborted, nothing saved"));
        mode = IDLE;
        break;
      case 'c': compute(); break;
      case 'l': listCaptures(); break;
      case 'x':
        confirmClear = true;
        Serial.println(F("# clear ALL stored captures? type y to confirm"));
        break;
      case 'h':
      case '?': printHelp(); break;
      default:
        Serial.print(F("# unknown command '"));
        Serial.print(c);
        Serial.println(F("' - type h for help"));
    }
  }
}

// ---------------------------------------------------------------- main

void printRow(const float *t) {
  Serial.print(millis() / 1000);
  Serial.print(',');
  if (mode == IDLE) {
    Serial.print(F("idle"));
  } else {
    Serial.print(mode == SETTLING ? F("settle_") : F("capture_"));
    Serial.print(POINT_NAME[target]);
  }

  bool calReady = allHave(ICE);
  float sum = 0, lo = 999, hi = -999, clo = 999, chi = -999;
  uint8_t n = 0;
  for (uint8_t i = 0; i < nDev; i++) {
    Serial.print(',');
    Serial.print(t[i], 4);              // 4 dp - do not round during calibration
    if (!valid(t[i])) continue;
    sum += t[i];
    n++;
    if (t[i] < lo) lo = t[i];
    if (t[i] > hi) hi = t[i];
    if (calReady) {
      float c = t[i] + offsetOf(i);
      if (c < clo) clo = c;
      if (c > chi) chi = c;
    }
  }
  Serial.print(',');
  if (n) Serial.print(sum / n, 4);
  Serial.print(',');
  if (n) Serial.print(hi - lo, 4);      // worst probe-to-probe disagreement, raw
  Serial.print(',');
  if (n && calReady) Serial.print(chi - clo, 4);   // same, after correction
  Serial.println();
}

// with no probes, keep saying so (and keep looking) instead of going quiet
void waitForProbes() {
  while (true) {
    sensors.begin();
    nDev = sensors.getDeviceCount();
    if (nDev) return;
    Serial.println(F("# probes found: 0 - check the 4.7k pull-up between D2 and 5V, and each probe's 3 wires. Retrying..."));
    delay(PERIOD_MS);
  }
}

void setup() {
  Serial.begin(9600);
  delay(500);
  Serial.println(F("# DS18B20 calibration test (ice offset + held-out checks)"));
  waitForProbes();

  Serial.print(F("# probes found: "));
  Serial.println(nDev);
  if (nDev > MAX_SENSORS) {
    Serial.print(F("# only the first "));
    Serial.print(MAX_SENSORS);
    Serial.println(F(" are used - raise MAX_SENSORS"));
    nDev = MAX_SENSORS;
  }
  if (nDev != EXPECTED_SENSORS) {
    Serial.print(F("# expected "));
    Serial.print(EXPECTED_SENSORS);
    Serial.println(F(" - is a probe unplugged? (fine if you meant it)"));
  }

  sensors.setResolution(12);            // 0.0625 C
  for (uint8_t i = 0; i < nDev; i++) {
    if (!sensors.getAddress(cal[i].addr, i)) memset(cal[i].addr, 0, 8);
    cal[i].have = 0;
  }
  if (nDev && sensors.isParasitePowerMode())
    Serial.println(F("# a probe is in parasite mode - its VDD is not reaching 5V"));

  // the address map: label each physical probe S0, S1, ... with tape
  for (uint8_t i = 0; i < nDev; i++) {
    printProbe(i);
    Serial.println();
  }

  loadAll();
  printHelp();

  Serial.print(F("elapsed_s,phase"));
  for (uint8_t i = 0; i < nDev; i++) {
    Serial.print(F(",S"));
    Serial.print(i);
  }
  Serial.println(F(",mean,spread,spread_cal"));
  nextRead = millis();
}

void loop() {
  handleSerial();
  if ((long)(millis() - nextRead) < 0) return;
  nextRead += PERIOD_MS;

  sensors.requestTemperatures();        // ~750 ms at 12 bit; typed commands wait in the buffer
  float t[MAX_SENSORS];
  bool ok = true;
  for (uint8_t i = 0; i < nDev; i++) {
    t[i] = sensors.getTempC(cal[i].addr);
    if (!valid(t[i])) ok = false;
    hist[i][histPos] = t[i];
  }
  histPos = (histPos + 1) % N_SETTLE;
  if (histFill < N_SETTLE) histFill++;

  printRow(t);
  stepCapture(t, ok);
}
