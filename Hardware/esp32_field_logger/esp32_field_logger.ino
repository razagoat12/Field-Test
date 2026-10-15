/*
 * esp32_field_logger.ino - ISEF 26 PCM field test
 *
 * Reads 4 DS18B20 sensors every 2 s and POSTs each reading line to
 * receive_logger.py on the laptop over Wi-Fi.
 *
 * Logs RAW values only. Calibration offsets (changes/calibration.md) are
 * applied in analysis, so the raw record is never altered.
 *
 * If Wi-Fi or the laptop is down, lines are kept in RAM (up to BUF_MAX)
 * and sent together when the link returns. RAM is lost on power loss.
 *
 * Wiring: all 4 sensors in parallel on GPIO 4.
 *         4.7 kOhm pull-up from GPIO 4 to 3.3 V.
 *         Sensor VDD to 3.3 V, GND to GND.
 *
 * Needs: ESP32 board package (Espressif), libraries OneWire and
 *        DallasTemperature (already installed for the Uno).
 */

#include <WiFi.h>
#include <HTTPClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>

// ---- EDIT THESE -----------------------------------------------------------
const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASS = "YOUR_WIFI_PASSWORD";
// Laptop IP from `ipconfig` (IPv4 address on the Wi-Fi adapter).
const char* LOG_URL   = "http://192.168.1.50:8000/log";
// ---------------------------------------------------------------------------

const int ONE_WIRE_PIN = 4;
const unsigned long PERIOD_MS = 2000;   // one reading every 2 s
const int N_SENSORS = 4;                // S0..S3
const int BUF_MAX = 300;                // ~10 min of readings held in RAM

// ROM addresses from the calibration run (changes/calibration.md).
// Reading by address keeps each sensor's label fixed whatever the bus order.
DeviceAddress ADDR[N_SENSORS] = {
  {0x28, 0xBA, 0xC2, 0xB4, 0x00, 0x00, 0x00, 0xE8},   // S0
  {0x28, 0x09, 0x62, 0x75, 0x00, 0x00, 0x00, 0x33},   // S1
  {0x28, 0xB5, 0x35, 0x73, 0x00, 0x00, 0x00, 0x84},   // S2
  {0x28, 0xDD, 0xDA, 0x76, 0x00, 0x00, 0x00, 0xD2},   // S3
};

OneWire oneWire(ONE_WIRE_PIN);
DallasTemperature sensors(&oneWire);

String pending[BUF_MAX];
int pendingCount = 0;
unsigned long nextRead = 0;

// ---------------------------------------------------------------------------

void queueLine(const String& s) {
  if (pendingCount == BUF_MAX) {          // full: drop the oldest line
    for (int i = 1; i < BUF_MAX; i++) pending[i - 1] = pending[i];
    pendingCount--;
  }
  pending[pendingCount++] = s;
}

void connectWifi() {
  Serial.print("Wi-Fi connecting");
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  unsigned long t0 = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - t0 < 15000) {
    delay(250);
    Serial.print('.');
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.print(" connected, IP ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println(" failed, will retry");
  }
}

// POSTs all pending lines in one request. Clears the buffer only on HTTP 200.
void flushPending() {
  if (pendingCount == 0) return;
  if (WiFi.status() != WL_CONNECTED) return;

  String body;
  for (int i = 0; i < pendingCount; i++) {
    body += pending[i];
    body += '\n';
  }

  HTTPClient http;
  http.begin(LOG_URL);
  http.setTimeout(2000);
  http.addHeader("Content-Type", "text/plain");
  int code = http.POST(body);
  http.end();

  if (code == 200) {
    pendingCount = 0;
  } else {
    Serial.print("POST failed, code ");
    Serial.print(code);
    Serial.print(", buffered ");
    Serial.println(pendingCount);
  }
}

void printAddress(const uint8_t* a) {
  for (int b = 0; b < 8; b++) {
    if (a[b] < 16) Serial.print('0');
    Serial.print(a[b], HEX);
  }
}

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("\nESP32 field logger starting");

  sensors.begin();
  sensors.setResolution(12);            // 0.0625 C

  // Header lines go to the receiver as "#" comments.
  queueLine("# ESP32 field logger, 4 sensors, raw values");
  for (int i = 0; i < N_SENSORS; i++) {
    String line = "# S" + String(i) + " ";
    for (int b = 0; b < 8; b++) {
      if (ADDR[i][b] < 16) line += '0';
      line += String(ADDR[i][b], HEX);
    }
    queueLine(line);
    Serial.print("S");
    Serial.print(i);
    Serial.print(" ");
    printAddress(ADDR[i]);
    Serial.println();
  }
  queueLine("# elapsed_s,S0,S1,S2,S3");

  connectWifi();
  flushPending();
  nextRead = millis();
}

void loop() {
  if (millis() - nextRead < PERIOD_MS) return;   // steady 2 s schedule
  nextRead += PERIOD_MS;

  if (WiFi.status() != WL_CONNECTED) connectWifi();

  sensors.requestTemperatures();        // blocks about 750 ms at 12 bit

  String line = String(millis() / 1000);
  for (int i = 0; i < N_SENSORS; i++) {
    float t = sensors.getTempC(ADDR[i]);   // -127 = disconnected, 85 = power-on
    line += ',';
    line += String(t, 4);
  }
  queueLine(line);
  Serial.println(line);

  flushPending();
}
