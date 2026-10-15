/*
 * DS18B20 calibration sketch - ISEF 26 PCM project
 *
 * Prints every sensor on the bus, by unique address, every 2 s.
 * Bundle all sensor tips together so they are at the SAME temperature,
 * then read at three reference points (see the calibration protocol).
 *
 * Wiring: all sensors parallel on D2, 4.7k pull-up from D2 to 5V.
 * No RTC needed for calibration.
 */

#include <OneWire.h>
#include <DallasTemperature.h>

const int ONE_WIRE_BUS = 2;
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

int nDevices = 0;

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
  sensors.setResolution(12);          // 0.0625 C
  nDevices = sensors.getDeviceCount();

  Serial.println(F("# DS18B20 calibration"));
  Serial.print(F("# sensors found: "));
  Serial.println(nDevices);

  if (nDevices == 0) {
    Serial.println(F("# NONE FOUND - check the 4.7k pull-up between D2 and 5V"));
  }

  // print the address map once, so you can label each physical probe
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

  // CSV header
  Serial.print(F("elapsed_s"));
  for (int i = 0; i < nDevices; i++) {
    Serial.print(F(",S"));
    Serial.print(i);
  }
  Serial.println(F(",mean,spread"));
}

void loop() {
  sensors.requestTemperatures();

  float sum = 0, lo = 999, hi = -999;
  Serial.print(millis() / 1000);

  for (int i = 0; i < nDevices; i++) {
    float t = sensors.getTempCByIndex(i);
    Serial.print(',');
    Serial.print(t, 4);               // 4 dp - do not round during calibration
    sum += t;
    if (t < lo) lo = t;
    if (t > hi) hi = t;
  }

  if (nDevices > 0) {
    Serial.print(',');
    Serial.print(sum / nDevices, 4);
    Serial.print(',');
    Serial.print(hi - lo, 4);         // spread = worst sensor-to-sensor disagreement
  }
  Serial.println();

  delay(2000);
}
