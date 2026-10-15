"""
receive_logger.py - ISEF 26 PCM field test
Receives sensor lines posted by the ESP32 (esp32_field_logger.ino) over Wi-Fi
and appends them to a timestamped CSV in Hardware/logs. Each request is
written and flushed to disk as it arrives.

Run:  python receive_logger.py
Stop: Ctrl+C  (the CSV is already saved)

Standard library only, so nothing to install.
The laptop must stay on, awake, and on the same Wi-Fi as the ESP32.
"""

import datetime
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000
OUT_DIR = r"E:\ISEF 26\Hardware\logs"

os.makedirs(OUT_DIR, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
out_path = os.path.join(OUT_DIR, f"esp32_log_{stamp}.csv")
out = open(out_path, "a", encoding="utf-8", newline="")
lock = threading.Lock()
rows = 0


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        global rows
        if self.path != "/log":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8", errors="ignore")
        ts = datetime.datetime.now().isoformat(timespec="seconds")

        with lock:
            for line in body.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.startswith("#"):
                    out.write(f"# {ts} {line}\n")      # headers and addresses
                else:
                    out.write(f"{ts},{line}\n")        # elapsed_s,S0,S1,S2,S3
                    rows += 1
            out.flush()
            os.fsync(out.fileno())

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, format, *args):
        pass    # the CSV is the record; keep the console quiet


if __name__ == "__main__":
    out.write("pc_timestamp,elapsed_s,S0,S1,S2,S3\n")
    out.flush()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Listening on port {PORT}.")
    print(f"Writing to: {out_path}")
    print("Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\nStopped. {rows} readings saved to:\n{out_path}")
    finally:
        server.server_close()
        out.close()
