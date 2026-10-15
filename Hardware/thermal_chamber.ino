/*
 * Thermal chamber controller - ISEF 26 PCM project
 *
 * Two modes:
 *   HOLD  - constant setpoint (leakage series: 50 / 60 / 70 C)
 *   CYCLE - Protocol F: 20-25 cycles between 60 C and 25 C, unattended
 *
 * Logs CSV to Serial: timestamp, control temp, corner temp, heater state.
 * Capture with Arduino IDE Serial Monitor, or PuTTY logging to a file.
 *
 * Hardware: DS18B20 x3 on D2 (4.7k pull-up to 5V), MOSFET heater on D3,
 *           DS3231 RTC on I2C. Fan wired direct to 12V, always on.
 *
 * SAFETY: software cutoff below + 100 C thermal fuse in series with heater.
 */

#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <RTClib.h>

// ---------- pins ----------
const int ONE_WIRE_BUS = 2;
const int HEATER_PIN   = 3;

// ---------- configure per run ----------
const bool  CYCLE_MODE = false;   // false = HOLD, true = CYCLE
const float SETPOINT   = 60.0;    // HOLD setpoint, deg C
const float HYSTERESIS = 0.5;     // deg C either side

// cycling parameters (Protocol F)
const float CYCLE_HIGH = 60.0;
const float CYCLE_LOW  = 25.0;
const unsigned long HOLD_HIGH_MS = 10UL * 60UL * 1000UL;  // 10 min at high
const int   TOTAL_CYCLES = 25;

// ---------- safety ----------
const float SAFETY_MARGIN = 15.0;   // cut out this far above setpoint
const float SENSOR_FAULT  = -100.0; // DS18B20 reads -127 if disconnected

const unsigned long LOG_INTERVAL_MS = 30000UL;  // 30 s

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
RTC_DS3231 rtc;

float ctrlT = 0, farT = 0;
bool heaterOn = false;
int cycleCount = 0;
bool heatingPhase = true;
unsigned long holdStart = 0;
unsigned long lastLog = 0;

void heater(bool on) {
  heaterOn = on;
  digitalWrite(HEATER_PIN, on ? HIGH : LOW);
}

void halt(const char *reason) {
  heater(false);
  Serial.print(F("# HALTED: "));
  Serial.println(reason);
  while (true) { delay(1000); }   // requires manual reset
}

void setup() {
  pinMode(HEATER_PIN, OUTPUT);
  heater(false);                   // heater off before anything else
  Serial.begin(9600);
  sensors.begin();
  sensors.setResolution(12);       // 0.0625 C

  if (!rtc.begin()) Serial.println(F("# WARNING: RTC not found"));

  Serial.println(F("# Thermal chamber controller"));
  Serial.print(F("# mode="));
  Serial.println(CYCLE_MODE ? F("CYCLE") : F("HOLD"));
  Serial.println(F("timestamp,elapsed_s,control_C,corner_C,gradient_C,heater,cycle"));

  holdStart = millis();
}

void loop() {
  sensors.requestTemperatures();
  ctrlT = sensors.getTempCByIndex(0);   // control sensor, at the samples
  farT  = sensors.getTempCByIndex(1);   // far corner, uniformity check

  // ---- safety first ----
  if (ctrlT < SENSOR_FAULT || farT < SENSOR_FAULT) halt("sensor disconnected");

  float target = CYCLE_MODE ? (heatingPhase ? CYCLE_HIGH : CYCLE_LOW) : SETPOINT;
  if (ctrlT > target + SAFETY_MARGIN) halt("overtemperature");

  // ---- control ----
  if (CYCLE_MODE) {
    if (heatingPhase) {
      if (ctrlT < CYCLE_HIGH - HYSTERESIS) heater(true);
      else if (ctrlT > CYCLE_HIGH + HYSTERESIS) heater(false);

      if (ctrlT >= CYCLE_HIGH - HYSTERESIS) {
        if (holdStart == 0) holdStart = millis();
        if (millis() - holdStart >= HOLD_HIGH_MS) {
          heatingPhase = false;      // start cooling
          heater(false);
          holdStart = 0;
        }
      }
    } else {
      heater(false);                 // cool passively; fan keeps running
      if (ctrlT <= CYCLE_LOW) {
        cycleCount++;
        if (cycleCount >= TOTAL_CYCLES) halt("cycling complete");
        heatingPhase = true;
        holdStart = 0;
      }
    }
  } else {
    if (ctrlT < SETPOINT - HYSTERESIS)      heater(true);
    else if (ctrlT > SETPOINT + HYSTERESIS) heater(false);
  }

  // ---- log ----
  if (millis() - lastLog >= LOG_INTERVAL_MS) {
    lastLog = millis();
    DateTime now = rtc.now();
    char ts[24];
    snprintf(ts, sizeof(ts), "%04d-%02d-%02d %02d:%02d:%02d",
             now.year(), now.month(), now.day(),
             now.hour(), now.minute(), now.second());
    Serial.print(ts);              Serial.print(',');
    Serial.print(millis() / 1000); Serial.print(',');
    Serial.print(ctrlT, 3);        Serial.print(',');
    Serial.print(farT, 3);         Serial.print(',');
    Serial.print(ctrlT - farT, 3); Serial.print(',');
    Serial.print(heaterOn ? 1 : 0); Serial.print(',');
    Serial.println(cycleCount);
  }

  delay(1000);
}
