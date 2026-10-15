"""
serial_logger.py - ISEF 26 PCM project
Reads the DS18B20 logger stream from the Arduino and writes it to a
timestamped CSV on the PC, one line at a time, flushing after each row
so a crash or unplug never loses more than the last reading.

Run:  python serial_logger.py
Stop: Ctrl+C  (the CSV is already fully saved)

Requires pyserial:  pip install pyserial
Only ONE program can own the COM port at a time - close the Arduino
Serial Monitor / Serial Plotter before running this.
"""

import csv
import datetime
import os
import sys
import time

try:
    import serial  # pyserial
except ImportError:
    sys.exit("pyserial not installed. Run:  pip install pyserial")

PORT = "COM3"           # <-- your Uno is on COM3
BAUD = 9600
OUT_DIR = r"E:\ISEF 26\Hardware\logs"

os.makedirs(OUT_DIR, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
out_path = os.path.join(OUT_DIR, f"cooling_log_{stamp}.csv")

print(f"Opening {PORT} @ {BAUD}...")
try:
    ser = serial.Serial(PORT, BAUD, timeout=3)
except serial.SerialException as e:
    sys.exit(f"Could not open {PORT}: {e}\n"
             f"Is the Serial Monitor still open? Is the board on {PORT}?")

time.sleep(2)           # the Uno resets when the port opens; let it boot
ser.reset_input_buffer()

print(f"Logging to: {out_path}")
print("Ctrl+C to stop.\n")

rows = 0
with open(out_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["pc_timestamp", "arduino_line"])  # arduino_line holds elapsed_s,S0,S1,...
    try:
        while True:
            raw = ser.readline().decode(errors="ignore").strip()
            if not raw:
                continue
            ts = datetime.datetime.now().isoformat(timespec="seconds")
            w.writerow([ts, raw])
            f.flush()
            os.fsync(f.fileno())            # force to disk - survives power loss
            rows += 1
            # show comments and every 30th data row so the console isn't a flood
            if raw.startswith("#") or rows % 30 == 0:
                print(f"{ts}  {raw}")
    except KeyboardInterrupt:
        print(f"\nStopped. {rows} lines written to:\n{out_path}")
    finally:
        ser.close()
