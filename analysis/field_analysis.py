"""
field_analysis.py - field Days 1 and 2, Al Khobar (15 and 16 Oct 2026).

Reads the clean logger CSVs and the Open-Meteo weather in Hardware/logs/ and writes:
  analysis/field_results.txt       every statistic quoted in the README
  assets/field_days_light.png      both days on clock time, with air temperature,
  assets/field_days_dark.png       sunlight and wind

HOW THE DATA IS USED
  * Findings come from the FIRST 90 MINUTES of each day: the hottest period, and on
    Day 2 the period before a shadow crosses the row (from ~95 min, 13:22).
  * NOTHING IS DROPPED. Every reading is plotted; full-run statistics are reported too,
    labelled as the limitation they are.
  * Ice offsets are added per sensor (docs/calibration.md). Station labels are the ones
    confirmed by finger test on 16 Oct 2026.
  * Weather is MODEL data (Open-Meteo, 15 min), interpolated to each reading. It is used
    to tell cloud from shadow, to express panels as a rise above air temperature, and to
    compare stations at matched sunlight (>= 600 W/m2, both days pooled, shadow excluded).

Run from the repo root:  python analysis/field_analysis.py
Requires: numpy, matplotlib
"""

import csv
import os
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS = os.path.join(ROOT, "Hardware", "logs")
ASSETS = os.path.join(ROOT, "assets")

OFFSET = {"S0_graphite": -1.6062, "S1_c40": -1.3875, "S2_rbw": -1.8625, "S3_bare": -1.3687}
NAME = {"S3_bare": "bare", "S2_rbw": "RBW", "S1_c40": "C40", "S0_graphite": "C40+G"}
DAYS = {1: ("pilot_2026-10-15.csv", "2026-10-15T13:30"),
        2: ("day2_2026-10-16.csv", "2026-10-16T11:47")}
WEATHER = "weather_alkhobar_2026-10-15_16.csv"
FINDINGS_MIN = 90
SHADOW_FROM_MIN = {2: 95}
SUN_MIN = 600.0
PAIRS = [("bare", "C40"), ("bare", "RBW"), ("bare", "C40+G"), ("RBW", "C40"), ("C40", "C40+G")]

THEMES = {
    "light": dict(surface="#fcfcfb", text="#0b0b0b", muted="#52514e", grid="#e4e3df", air="#0b0b0b",
                  sun="#d98e04", find="#2a78d6", shade="#000000",
                  series={"bare": "#d1495b", "RBW": "#8a8880", "C40": "#2a78d6", "C40+G": "#6b4fbb"}),
    "dark": dict(surface="#1a1a19", text="#ffffff", muted="#c3c2b7", grid="#3a3936", air="#ffffff",
                 sun="#f2b134", find="#3987e5", shade="#ffffff",
                 series={"bare": "#ef6f80", "RBW": "#b4b2a9", "C40": "#3987e5", "C40+G": "#9a86e0"}),
}


def load_day(fname):
    with open(os.path.join(LOGS, fname), encoding="utf-8") as f:
        rows = list(csv.DictReader(line for line in f if not line.startswith("#")))
    t = np.array([float(r["elapsed_s"]) for r in rows])
    temps = {NAME[c]: np.array([float(r[c]) for r in rows]) + OFFSET[c] for c in OFFSET}
    return t, temps


def load_weather():
    with open(os.path.join(LOGS, WEATHER), encoding="utf-8") as f:
        rows = list(csv.DictReader(line for line in f if not line.startswith("#")))
    ts = np.array([datetime.fromisoformat(r["time"]).timestamp() for r in rows])
    return ts, {k: np.array([float(r[c]) for r in rows])
                for k, c in (("sun", "shortwave_Wm2"), ("air", "temp_C"),
                             ("wind", "wind_kmh"), ("cloud", "cloud_pct"))}


def hhmm(h):
    return f"{int(h):02d}:{int(round((h % 1) * 60)) % 60:02d}"


def main():
    wts, w = load_weather()
    data = {}
    for d, (fname, start) in DAYS.items():
        t, temps = load_day(fname)
        s = datetime.fromisoformat(start)
        abs_t = s.timestamp() + t
        wx = {k: np.interp(abs_t, wts, x) for k, x in w.items()}
        data[d] = (t, temps, wx, s.hour + s.minute / 60 + t / 3600)

    lines = []
    emit = lambda s="": (lines.append(s), print(s))
    emit("FIELD TEST, AL KHOBAR - back-surface temperature, ice-corrected (deg C)")
    emit("Positive dT = the SECOND station in the pair runs cooler. Weather = Open-Meteo model data.")
    for d, (t, temps, wx, ch) in data.items():
        emit("")
        emit("=" * 72)
        emit(f"DAY {d}: start {DAYS[d][1][11:]}, {len(t)} readings, {t[-1] / 3600:.2f} h")
        for label, mask in ((f"FINDINGS - first {FINDINGS_MIN} min ({hhmm(ch[0])}-"
                             f"{hhmm(ch[0] + FINDINGS_MIN / 60)})", t <= FINDINGS_MIN * 60),
                            ("FULL RUN - limitation, shown for transparency", np.ones_like(t, bool))):
            emit(f"\n  {label}")
            emit(f"  weather: sun {wx['sun'][mask].mean():.0f} W/m2, air {wx['air'][mask].mean():.1f} C, "
                 f"wind {wx['wind'][mask].mean():.1f} km/h, cloud {wx['cloud'][mask].max():.0f} % max")
            emit("  peaks: " + ", ".join(f"{k} {temps[k][mask].max():.1f}" for k in NAME.values()))
            emit("  mean rise above air: " + ", ".join(
                f"{k} {np.mean(temps[k][mask] - wx['air'][mask]):.1f}" for k in NAME.values()))
            for a, b in PAIRS:
                emit(f"  {a + ' - ' + b:16s} mean dT {np.mean(temps[a][mask] - temps[b][mask]):+6.2f}"
                     f"   peak dT {temps[a][mask].max() - temps[b][mask].max():+6.2f}")
        emit("\n  minutes above 60 / 65 / 68 C: " + ", ".join(
            f"{k} {np.sum(temps[k] > 60) * 2 / 60:.0f}/{np.sum(temps[k] > 65) * 2 / 60:.0f}/"
            f"{np.sum(temps[k] > 68) * 2 / 60:.0f}" for k in NAME.values()))
    emit("")
    emit("=" * 72)
    emit(f"MATCHED SUNLIGHT - sun >= {SUN_MIN:.0f} W/m2, both days pooled, Day 2 shadow excluded")
    pooled = {k: [] for k in NAME.values()}
    for d, (t, temps, wx, ch) in data.items():
        keep = wx["sun"] >= SUN_MIN
        if d in SHADOW_FROM_MIN:
            keep &= t < SHADOW_FROM_MIN[d] * 60
        emit(f"  Day {d}: {int(keep.sum())} readings")
        for k in pooled:
            pooled[k].append(temps[k][keep])
    pooled = {k: np.concatenate(v) for k, v in pooled.items()}
    for a, b in PAIRS:
        emit(f"  {a + ' - ' + b:16s} mean dT {np.mean(pooled[a] - pooled[b]):+6.2f}")
    with open(os.path.join(ROOT, "analysis", "field_results.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    for mode, th in THEMES.items():
        fig, axes = plt.subplots(2, 2, figsize=(13, 7.2), sharex="col", facecolor=th["surface"],
                                 gridspec_kw={"height_ratios": [3, 1.4]})
        for col, (d, (t, temps, wx, ch)) in enumerate(data.items()):
            top, bot = axes[0, col], axes[1, col]
            for ax in (top, bot):
                ax.set_facecolor(th["surface"])
                ax.grid(True, color=th["grid"], lw=0.7)
                ax.tick_params(colors=th["muted"], labelsize=8.5)
                for sp in ax.spines.values():
                    sp.set_color(th["grid"])
                ax.axvspan(ch[0], ch[0] + FINDINGS_MIN / 60, color=th["find"], alpha=0.08)
                if d in SHADOW_FROM_MIN:
                    ax.axvspan(ch[0] + SHADOW_FROM_MIN[d] / 60, ch[-1], color=th["shade"], alpha=0.06)
            top.text(ch[0] + 0.03, 75.5, "findings (90 min)", fontsize=8.5, color=th["muted"])
            if d in SHADOW_FROM_MIN:
                top.text(ch[0] + SHADOW_FROM_MIN[d] / 60 + 0.03, 75.5, "shadow on row (limitation)",
                         fontsize=8.5, color=th["muted"])
            for k in NAME.values():
                top.plot(ch, temps[k], color=th["series"][k], lw=1.2, label=k)
            top.plot(ch, wx["air"], color=th["air"], lw=1.0, ls="--", label="air (model)")
            top.set_ylim(28, 78)
            top.set_title(f"Day {d}, {DAYS[d][1][:10]}, Al Khobar", loc="left", fontsize=11, color=th["text"])
            bot.plot(ch, wx["sun"], color=th["sun"], lw=1.5)
            bot.set_ylim(0, 900)
            bw = bot.twinx()
            bw.plot(ch, wx["wind"], color=th["muted"], lw=1.0, ls=":")
            bw.set_ylim(0, 20)
            bw.tick_params(colors=th["muted"], labelsize=8.5)
            for sp in bw.spines.values():
                sp.set_color(th["grid"])
            if col == 1:
                bw.set_ylabel("wind, dotted (km/h)", color=th["muted"])
            ticks = np.arange(np.ceil(ch[0] * 2) / 2, ch[-1] + 0.01, 0.5)
            bot.set_xticks(ticks)
            bot.set_xticklabels([hhmm(x) for x in ticks])
            bot.set_xlabel("local time (start approximate)", color=th["muted"])
        axes[0, 0].set_ylabel("back-surface T, ice-corrected (°C)", color=th["muted"])
        axes[1, 0].set_ylabel("sunlight (W/m²)", color=th["sun"])
        leg = axes[0, 0].legend(frameon=False, ncol=5, fontsize=8.5, loc="lower left")
        for txt in leg.get_texts():
            txt.set_color(th["text"])
        fig.tight_layout()
        fig.savefig(os.path.join(ASSETS, f"field_days_{mode}.png"), dpi=150, facecolor=th["surface"])
        plt.close(fig)
    print("\nWrote analysis/field_results.txt and assets/field_days_{light,dark}.png")


if __name__ == "__main__":
    main()
