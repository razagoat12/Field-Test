/*
 * RTC test sketch - ISEF 26 PCM project
 *
 * Works with DS3231 and DS1307 modules (RTClib auto-handles both;
 * pick the matching class below).
 *
 * Wiring (I2C):
 *   RTC VCC -> 5V
 *   RTC GND -> GND
 *   RTC SDA -> A4
 *   RTC SCL -> A5
 *
 * Library: "RTClib" by Adafruit (Library Manager).
 *
 * What a PASS looks like:
 *   - "RTC found"
 *   - time prints every second and INCREMENTS
 *   - unplug USB for a minute, plug back in: time is still correct
 *     (that proves the backup battery works)
 */

#include <Wire.h>
#include <RTClib.h>

RTC_DS3231 rtc;          // <-- if your module is a DS1307, change to: RTC_DS1307 rtc;

void setup() {
  Serial.begin(9600);
  delay(500);

  if (!rtc.begin()) {
    Serial.println(F("RTC NOT FOUND - check SDA->A4, SCL->A5, VCC, GND"));
    while (1) delay(1000);
  }
  Serial.println(F("RTC found"));

  if (rtc.lostPower()) {
    Serial.println(F("RTC lost power - setting to sketch compile time"));
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }
}

void loop() {
  DateTime now = rtc.now();
  char buf[25];
  snprintf(buf, sizeof(buf), "%04d-%02d-%02d %02d:%02d:%02d",
           now.year(), now.month(), now.day(),
           now.hour(), now.minute(), now.second());
  Serial.println(buf);
  delay(1000);
}
