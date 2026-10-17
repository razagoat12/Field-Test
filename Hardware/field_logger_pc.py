"""
field_logger_pc.py - ISEF 26 field test logger (runs on the laptop)

Records every line the Arduino prints, stamped with the laptop's real clock time, to a CSV
that is flushed after every line. Works with whatever DS18B20 sketch is on the Uno
(ds18b20_logger.ino or the calibration sketch) - the Arduino line is stored unchanged.

While it runs, type into this window and press Enter:
    m            -> marks "MOVE" (you just moved the stations one spot)
    anything     -> saved as a note, e.g.  cloud over panel 3   or   started shade
A reminder prints every --move-every minutes (0 = no reminders).

Run (calibration, move every 15 min):   python field_logger_pc.py --move-every 15
Run (slab day, no moves):               python field_logger_pc.py
Choose the port yourself if needed:     python field_logger_pc.py --port COM17
Stop: Ctrl+C  (the file is already saved)

Requires pyserial:  pip install pyserial
Close the Arduino Serial Monitor first - only one program can use the port.
"""

import argparse
import datetime
import os
import sys
import threading
import time

try:
    import serial
    from serial.tools import list_ports
except ImportError:
    sys.exit("pyserial not installed. Run:  pip install pyserial")

parser = argparse.ArgumentParser()
parser.add_argument("--port", help="e.g. COM17 (Windows) or /dev/tty.usbmodem1101 (Mac)")
parser.add_argument("--baud", type=int, default=9600)
parser.add_argument("--move-every", type=float, default=0, help="reminder interval, minutes")
parser.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs"))
args = parser.parse_args()

port = args.port
if not port:
    ports = [p.device for p in list_ports.comports()]
    if not ports:
        sys.exit("No serial port found. Is the Arduino plugged in?")
    port = ports[0] if len(ports) == 1 else input(f"Ports found: {ports}\nType the port to use: ").strip()

os.makedirs(args.out, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
path = os.path.join(args.out, f"field_{stamp}.csv")
out = open(path, "w", encoding="utf-8", newline="")
out.write(f"# field_logger_pc.py, port {port}, started {datetime.datetime.now().isoformat(timespec='seconds')}\n")
out.write("pc_time,arduino_line\n")
out.flush()
lock = threading.Lock()


def write(text):
    now = datetime.datetime.now().isoformat(timespec="seconds")
    with lock:
        out.write(f'{now},"{text}"\n')
        out.flush()
    return now


def keyboard():
    moves = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if line.lower() == "m":
            moves += 1
            t = write(f"#MOVE {moves}")
            print(f"  >> MOVE {moves} marked at {t[11:]}")
        else:
            t = write(f"#NOTE {line}")
            print(f"  >> note saved at {t[11:]}")


def reminders():
    while args.move_every > 0:
        time.sleep(args.move_every * 60)
        print(f"\a  *** {datetime.datetime.now():%H:%M} - time to move the stations, then type m + Enter ***")


print(f"Opening {port} @ {args.baud} ...")
try:
    ser = serial.Serial(port, args.baud, timeout=3)
except serial.SerialException as e:
    sys.exit(f"Could not open {port}: {e}\nIs the Serial Monitor still open?")
time.sleep(2)  # the Uno resets when the port opens
print(f"Logging to {path}")
print("Type m + Enter after each move; type any note + Enter to save it. Ctrl+C to stop.\n")
threading.Thread(target=keyboard, daemon=True).start()
threading.Thread(target=reminders, daemon=True).start()

rows = 0
try:
    while True:
        raw = ser.readline()
        if not raw:
            continue
        line = raw.decode("ascii", errors="ignore").strip()
        if not line or not any(ch.isdigit() for ch in line) and not line.startswith("#"):
            continue  # skip garbage / empty lines
        write(line.replace('"', "'"))
        rows += 1
        if rows % 30 == 0:
            print(f"{datetime.datetime.now():%H:%M:%S}  {line}")
except KeyboardInterrupt:
    pass
finally:
    ser.close()
    out.close()
    print(f"\nStopped. {rows} lines saved to {path}")
