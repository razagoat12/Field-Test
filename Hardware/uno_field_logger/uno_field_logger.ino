/*
 * uno_field_logger.ino - ISEF 26 PCM field test
 *
 * Reads 4 DS18B20 sensors every 2 s and prints one CSV line over USB.
 * serial_logger.py on the laptop saves every line to Hardware\logs.
 * RAW values only; calibration offsets (changes/calibration.md) are applied in analysis.
 *
 * Wiring: all 4 sensors in parallel on D2, 4.7k pull-up D2 to 5V, VDD 5V, GND GND.
 * Serial Monitor must be CLOSED when serial_logger.py runs (one program per port).
 *
 * Output:  elapsed_s,S0,S1,S2,S3     (-127 = disconnected, 85 = power-on value)
 */

#include <OneWire.h>
#include <DallasTemperature.h>

const int ONE_WIRE_BUS = 2;
const unsigned long PERIOD_MS = 2000;
const uint8_t N = 4;

// ROM addresses from the calibration run; reading by address keeps labels fixed.
DeviceAddress ADDR[N] = {
  {0x28, 0xBA, 0xC2, 0xB4, 0x00, 0x00, 0x00, 0xE8},   // S0
  {0x28, 0x09, 0x62, 0x75, 0x00, 0x00, 0x00, 0x33},   // S1
  {0x28, 0xB5, 0x35, 0x73, 0x00, 0x00, 0x00, 0x84},   // S2
  {0x28, 0xDD, 0xDA, 0x76, 0x00, 0x00, 0x00, 0xD2},   // S3
};

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
unsigned long nextRead = 0;

void setup() {
  Serial.begin(9600);
  delay(500);
  sensors.begin();
  sensors.setResolution(12);

  Serial.println(F("# uno field logger, 4 sensors, raw values"));
  for (uint8_t i = 0; i < N; i++) {
    Serial.print(F("# S"));
    Serial.print(i);
    Serial.print(' ');
    for (uint8_t b = 0; b < 8; b++) {
      if (ADDR[i][b] < 16) Serial.print('0');
      Serial.print(ADDR[i][b], HEX);
    }
    Serial.println();
  }
  Serial.println(F("# elapsed_s,S0,S1,S2,S3"));
  nextRead = millis();
}

void loop() {
  if ((long)(millis() - nextRead) < 0) return;
  nextRead += PERIOD_MS;

  sensors.requestTemperatures();
  Serial.print(millis() / 1000);
  for (uint8_t i = 0; i < N; i++) {
    Serial.print(',');
    Serial.print(sensors.getTempC(ADDR[i]), 4);
  }
  Serial.println();
}
