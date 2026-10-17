/*
 * Field station logger - ISEF 26 PCM project (calibration run + slab days)
 *
 * Reads the four DS18B20s BY THEIR ID, so every column is always the same station
 * (bare, RBW, C40, C40G) however the sensors are plugged in or ordered on the bus.
 * Prints one CSV row every 2 s: elapsed seconds, RTC clock time (if an RTC is wired),
 * and the four RAW temperatures (ice offsets are applied in the analysis, not here).
 *
 * Type into the Serial Monitor (line ending = "Newline") and press Enter:
 *   m            -> prints "#MOVE n" with the time (after moving the stations one spot)
 *   any text     -> prints "#NOTE text" with the time
 * A reminder to move the stations prints every MOVE_EVERY_MIN minutes (0 = off).
 *
 * Wiring: unchanged. All sensors on D2, 4.7k from D2 to 5V.
 * Optional RTC (DS3231): SDA -> A4, SCL -> A5. Without it the clock column shows "--".
 * A reading of -127 means that sensor was not found: check its wires.
 *
 * Libraries: OneWire, DallasTemperature, RTClib (all from Library Manager).
 */

#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <RTClib.h>

const int ONE_WIRE_BUS = 2;
const unsigned long INTERVAL_MS = 2000UL;     // one row every 2 s
const unsigned long MOVE_EVERY_MIN = 15;      // calibration: 15. Slab day: set to 0.

// Sensor IDs from the 16 Oct finger test. Order here = column order.
const char* NAMES[4] = {"bare", "RBW", "C40", "C40G"};
DeviceAddress ADDR[4] = {
  {0x28, 0xDD, 0xDA, 0x76, 0x00, 0x00, 0x00, 0xD2},   // bare  (old S3)
  {0x28, 0xB5, 0x35, 0x73, 0x00, 0x00, 0x00, 0x84},   // RBW   (old S2)
  {0x28, 0x09, 0x62, 0x75, 0x00, 0x00, 0x00, 0x33},   // C40   (old S1)
  {0x28, 0xBA, 0xC2, 0xB4, 0x00, 0x00, 0x00, 0xE8}    // C40G  (old S0)
};
const float ICE[4] = {1.3687, 1.8625, 1.3875, 1.6062};  // ice readings, for the header only

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
RTC_DS3231 rtc;
bool rtcOk = false;

unsigned long nextRead = 0;
unsigned long nextRemind = 0;
int moves = 0;

void print2(int v) {
  if (v < 10) Serial.print('0');
  Serial.print(v);
}

void printClock() {
  if (!rtcOk) { Serial.print(F("--")); return; }
  DateTime now = rtc.now();
  print2(now.hour()); Serial.print(':'); print2(now.minute()); Serial.print(':'); print2(now.second());
}

void printAddr(const uint8_t* a) {
  for (uint8_t i = 0; i < 8; i++) {
    if (a[i] < 16) Serial.print('0');
    Serial.print(a[i], HEX);
  }
}

void stampLine(const __FlashStringHelper* tag) {
  Serial.print(tag);
  Serial.print(F(" at "));
  Serial.print(millis() / 1000UL);
  Serial.print(F(" s, "));
  printClock();
}

void handleSerial() {
  static char buf[48];
  static uint8_t n = 0;
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n' || c == '\r') {
      if (n > 0) {
        buf[n] = 0;
        if (n == 1 && (buf[0] == 'm' || buf[0] == 'M')) {
          moves++;
          Serial.print(F("#MOVE "));
          Serial.print(moves);
          stampLine(F(""));
        } else {
          Serial.print(F("#NOTE "));
          Serial.print(buf);
          stampLine(F(""));
        }
        Serial.println();
      }
      n = 0;
    } else if (n < sizeof(buf) - 1) {
      buf[n++] = c;
    }
  }
}

void setup() {
  Serial.begin(9600);
  delay(500);
  sensors.begin();
  sensors.setResolution(12);
  sensors.setWaitForConversion(true);
  rtcOk = rtc.begin();

  Serial.println(F("# field_station_logger.ino - raw DS18B20 readings, by sensor ID"));
  for (int i = 0; i < 4; i++) {
    Serial.print(F("# ")); Serial.print(NAMES[i]); Serial.print(' ');
    printAddr(ADDR[i]);
    Serial.print(F("  ice reading ")); Serial.print(ICE[i], 4);
    Serial.println(sensors.isConnected(ADDR[i]) ? F("  OK") : F("  MISSING - check wires"));
  }
  if (!rtcOk) Serial.println(F("# no RTC found - clock column will be --; write the start time down"));
  else if (rtc.lostPower()) Serial.println(F("# WARNING: RTC lost power, clock is WRONG - write the start time down"));
  Serial.print(F("# started ")); printClock(); Serial.println();
  Serial.println(F("# type m + Enter after each move; any other text + Enter = note"));
  Serial.println(F("elapsed_s,clock,bare,RBW,C40,C40G"));

  nextRead = millis();
  nextRemind = millis() + MOVE_EVERY_MIN * 60000UL;
}

void loop() {
  handleSerial();

  if ((long)(millis() - nextRead) >= 0) {
    nextRead += INTERVAL_MS;
    sensors.requestTemperatures();
    Serial.print(millis() / 1000UL);
    Serial.print(',');
    printClock();
    for (int i = 0; i < 4; i++) {
      Serial.print(',');
      Serial.print(sensors.getTempC(ADDR[i]), 4);
    }
    Serial.println();
  }

  if (MOVE_EVERY_MIN > 0 && (long)(millis() - nextRemind) >= 0) {
    nextRemind += MOVE_EVERY_MIN * 60000UL;
    Serial.print(F("# *** time to move the stations one spot, then type m ***  "));
    printClock();
    Serial.println();
  }
}
