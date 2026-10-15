/*
 * DS18B20 continuous logger - ISEF 26 PCM project
 *
 * Streams every sensor on the bus as CSV, once per interval, FOREVER.
 * It does NOT store anything on the Arduino - the PC-side logger
 * (serial_logger.py) writes the CSV to disk. This is what makes a
 * reliable 24 h run possible: the Uno's tiny RAM/EEPROM and its
 * auto-reset-on-serial-open cannot lose your data if the PC holds it.
 *
 * Wiring (same as the calibration sketch): all sensors parallel on D2,
 * 4.7k pull-up from D2 to 5V.  A reading of -127 / -128 means the read
 * FAILED - check that pull-up and the data wire first.
 *
 * Output format:
 *   # comment lines (sensor count, address map) - ignored by analysis
 *   elapsed_s,S0,S1,...     <- header
 *   12.3,29.06,29.01,...    <- data rows
 */

#include <OneWire.h>
#include <DallasTemperature.h>

const int ONE_WIRE_BUS = 2;
const unsigned long INTERVAL_MS = 10000UL;   // 10 s. Change if you want.

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

int nDevices = 0;
unsigned long nextRead = 0;

void printAddress(DeviceAddress a) {
  for (uint8_t i = 0; i < 8; i++) {
    if (a[i] < 16) Serial.print('0');
    Serial.print(a[i], HEX);
  }
}

void setup() {
  Serial.begin(9600);
  delay(500);
  sensors.begin();
  sensors.setResolution(12);               // 0.0625 C
  sensors.setWaitForConversion(true);
  nDevices = sensors.getDeviceCount();

  Serial.print(F("# sensors found: "));
  Serial.println(nDevices);
  if (nDevices == 0) {
    Serial.println(F("# NONE FOUND - check the 4.7k pull-up between D2 and 5V"));
  }
  DeviceAddress addr;
  for (int i = 0; i < nDevices; i++) {
    if (sensors.getAddress(addr, i)) {
      Serial.print(F("# index "));
      Serial.print(i);
      Serial.print(F(" = "));
      printAddress(addr);
      Serial.println();
    }
  }

  Serial.print(F("elapsed_s"));
  for (int i = 0; i < nDevices; i++) { Serial.print(F(",S")); Serial.print(i); }
  Serial.println();
}

void loop() {
  if ((long)(millis() - nextRead) >= 0) {
    nextRead += INTERVAL_MS;
    sensors.requestTemperatures();

    Serial.print(millis() / 1000.0, 1);
    for (int i = 0; i < nDevices; i++) {
      float t = sensors.getTempCByIndex(i);
      Serial.print(',');
      Serial.print(t, 2);                  // -127/-128 here = failed read
    }
    Serial.println();
  }
}
