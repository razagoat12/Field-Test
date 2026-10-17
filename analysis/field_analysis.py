"""
field_analysis.py - field Days 1-3, Al Khobar (15, 16 and 17 Oct 2026).

Reads the clean logger CSVs and the Open-Meteo weather in Hardware/logs/ and writes:
  analysis/field_results.txt        every statistic quoted in the README
  assets/field_days_{light,dark}.png     all days on clock time, with air, sunlight and wind
  assets/field_summary_{light,dark}.png  per-day peak dT, evening cooling rate, slab mass loss

HOW THE DATA IS USED
  * Findings come from the FIRST 90 MINUTES of each day. Shadow periods (Day 2 from ~95 min,
    Day 3 from ~180 min) are shown and labelled.
  * NOTHING IS DROPPED. Every reading is plotted; full-run statistics are reported too,
    labelled as the limitation they are.
  * Ice offsets are added per sensor (docs/calibration.md). Station labels are the ones
    confirmed by finger test on 16 Oct 2026.
  * Pre-registered main number: per-day peak of each slab station minus the bare peak on the
    same day, mean, SD and t-based 95 % CI over the days.
  * Weather is MODEL data (Open-Meteo, 15 min), interpolated to each reading.
  * The evening cooling-rate comparison is post hoc.

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
        2: ("day2_2026-10-16.csv", "2026-10-16T11:47"),
        3: ("day3_2026-10-17.csv", "2026-10-17T11:45")}
WEATHER = ["weather_alkhobar_2026-10-15_16.csv", "weather_alkhobar_2026-10-17.csv"]
FINDINGS_MIN = 90
SHADOW_FROM_MIN = {2: 95, 3: 180}
SUN_MIN = 600.0
PAIRS = [("bare", "C40"), ("bare", "RBW"), ("bare", "C40+G"), ("RBW", "C40"), ("C40", "C40+G")]
MASS_G = {"RBW": (98, 98), "C40": (96, 94), "C40+G": (100, 89)}   # before, after; 1 g scale
MODEL_V2 = {"RBW": 0.8, "C40": 1.9, "C40+G": 2.1}                 # pre-registered, 2 cm slabs
MODEL_1CM = {"C40": 0.8}                                           # same model, as-built 1 cm
T95 = {2: 12.706, 3: 4.303, 4: 3.182, 5: 2.776}

THEMES = {
    "light": dict(surface="#fcfcfb", text="#0b0b0b", muted="#52514e", grid="#e4e3df", air="#0b0b0b",
                  sun="#d98e04", find="#2a78d6", shade="#000000", rule="#d98e04",
                  series={"bare": "#d1495b", "RBW": "#8a8880", "C40": "#2a78d6", "C40+G": "#6b4fbb"}),
    "dark": dict(surface="#1a1a19", text="#ffffff", muted="#c3c2b7", grid="#3a3936", air="#ffffff",
                 sun="#f2b134", find="#3987e5", shade="#ffffff", rule="#f2b134",
                 series={"bare": "#ef6f80", "RBW": "#b4b2a9", "C40": "#3987e5", "C40+G": "#9a86e0"}),
}


def load_day(fname):
    with open(os.path.join(LOGS, fname), encoding="utf-8") as f:
        rows = list(csv.DictReader(line for line in f if not line.startswith("#")))
    t = np.array([float(r["elapsed_s"]) for r in rows])
    temps = {NAME[c]: np.array([float(r[c]) for r in rows]) + OFFSET[c] for c in OFFSET}
    return t, temps


def load_weather():
    rows = []
    for fname in WEATHER:
        with open(os.path.join(LOGS, fname), encoding="utf-8") as f:
            rows += list(csv.DictReader(line for line in f if not line.startswith("#")))
    ts = np.array([datetime.fromisoformat(r["time"]).timestamp() for r in rows])
    return ts, {k: np.array([float(r[c]) for r in rows])
                for k, c in (("sun", "shortwave_Wm2"), ("air", "temp_C"),
                             ("wind", "wind_kmh"), ("cloud", "cloud_pct"))}


def hhmm(h):
    return f"{int(h):02d}:{int(round((h % 1) * 60)) % 60:02d}"


def cooling_rate(t, y, smooth=300):
    """Cooling rate (C/h) of a smoothed series; t in seconds."""
    ys = np.convolve(y, np.ones(smooth) / smooth, "same")
    return ys, -np.gradient(ys, t / 3600)


def style(ax, th):
    ax.set_facecolor(th["surface"])
    ax.grid(True, color=th["grid"], lw=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(colors=th["muted"], labelsize=8.5)
    for sp in ax.spines.values():
        sp.set_color(th["grid"])


def main():
    wts, w = load_weather()
    data = {}
    for d, (fname, start) in DAYS.items():
        t, temps = load_day(fname)
        s = datetime.fromisoformat(start)
        wx = {k: np.interp(s.timestamp() + t, wts, x) for k, x in w.items()}
        data[d] = (t, temps, wx, s.hour + s.minute / 60 + t / 3600)

    lines = []
    emit = lambda s="": (lines.append(s), print(s))
    emit("FIELD TEST, AL KHOBAR - back-surface temperature, ice-corrected (deg C)")
    emit("Slabs 14 x 7 x 1 cm. Positive dT = the SECOND station in the pair runs cooler.")
    emit("Weather = Open-Meteo model data.")
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
        if d == 3:
            emit("\n  Day 3: all stations in the sun all day before logging. C40 drops ~6 C at ~80 min")
            emit("  while the others keep heating, and stays ~8 C below RBW until ~180 min; the row")
            emit("  was checked every 30 min and C40 was not shaded. Light smudge of composite near")
            emit("  the C40 sensor afterwards, not stuck. All readings kept.")
            late = t >= t[-1] - 1800
            emit("  last 30 min (after sunset): " + ", ".join(
                f"{k} {temps[k][late].mean():.1f}" for k in NAME.values()))

    emit("")
    emit("=" * 72)
    emit("PRE-REGISTERED MAIN NUMBER: per-day peak minus partner's peak, same day; mean, SD,")
    emit("t-based 95 % CI (n = days). Last 5 min of each day excluded (packing up).")
    peaks = {}
    for d, (t, temps, wx, ch) in data.items():
        keep = t < t[-1] - 300
        peaks[d] = {k: temps[k][keep].max() for k in NAME.values()}
    for a, b in PAIRS:
        x = np.array([peaks[d][a] - peaks[d][b] for d in data])
        m, sd = x.mean(), x.std(ddof=1)
        h = T95[len(x)] * sd / np.sqrt(len(x))
        emit(f"  {a + ' - ' + b:16s} days {' '.join(f'{y:+5.1f}' for y in x)}   mean {m:+5.2f}"
             f"  SD {sd:4.2f}  95% CI [{m - h:+5.1f}, {m + h:+5.1f}]")

    emit("")
    emit("=" * 72)
    emit("EVENING COOLING RATE (C/h) at the same panel temperature after the row loses sun")
    emit("(post hoc; 10-min running mean). Latent release = slow cooling near 43-44 C.")
    for d in (2, 3):
        t, temps, wx, ch = data[d]
        k = t > SHADOW_FROM_MIN[d] * 60
        tt = t[k]
        inner = (tt > tt[0] + 360) & (tt < tt[-1] - 360)
        emit(f"  Day {d}:  " + "  ".join(f"{T} C" for T in (50, 46, 44, 42, 40)))
        for name in NAME.values():
            ys, rate = cooling_rate(tt, temps[name][k])
            cells = []
            for T in (50, 46, 44, 42, 40):
                sel = inner & (np.abs(ys - T) < 1)
                cells.append(f"{rate[sel].mean():5.1f}" if sel.any() else "    -")
            emit(f"    {name:6s} " + "  ".join(cells))

    emit("")
    emit("=" * 72)
    emit(f"MATCHED SUNLIGHT - sun >= {SUN_MIN:.0f} W/m2, all days pooled, shadow periods excluded")
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

    emit("")
    emit("=" * 72)
    emit("SLAB MASS over the campaign (~72 h in the sun; kitchen scale, 1 g)")
    for k, (m0, m1) in MASS_G.items():
        emit(f"  {k:6s} {m0} -> {m1} g   loss {100 * (m0 - m1) / m0:4.1f} %  (H7d limit 2 %)")
    with open(os.path.join(ROOT, "analysis", "field_results.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    treated = ["RBW", "C40", "C40+G"]
    for mode, th in THEMES.items():
        # ---- all days on clock time ----
        n = len(data)
        fig, axes = plt.subplots(2, n, figsize=(6 * n, 7.2), sharex="col", facecolor=th["surface"],
                                 gridspec_kw={"height_ratios": [3, 1.4]})
        for col, (d, (t, temps, wx, ch)) in enumerate(data.items()):
            top, bot = axes[0, col], axes[1, col]
            for ax in (top, bot):
                style(ax, th)
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
            if col == n - 1:
                bw.set_ylabel("wind, dotted (km/h)", color=th["muted"])
            step = 1.0 if ch[-1] - ch[0] > 5 else 0.5
            ticks = np.arange(np.ceil(ch[0] / step) * step, ch[-1] + 0.01, step)
            bot.set_xticks(ticks)
            bot.set_xticklabels([hhmm(x) for x in ticks])
            bot.set_xlabel("local time", color=th["muted"])
        axes[0, 0].set_ylabel("back-surface T, ice-corrected (°C)", color=th["muted"])
        axes[1, 0].set_ylabel("sunlight (W/m²)", color=th["sun"])
        leg = axes[0, 0].legend(frameon=False, ncol=5, fontsize=8.5, loc="lower left")
        for txt in leg.get_texts():
            txt.set_color(th["text"])
        fig.tight_layout()
        fig.savefig(os.path.join(ASSETS, f"field_days_{mode}.png"), dpi=150, facecolor=th["surface"])
        plt.close(fig)

        # ---- summary: per-day peak dT, evening cooling, mass ----
        fig, ax = plt.subplots(1, 3, figsize=(15, 4.6), facecolor=th["surface"],
                               gridspec_kw={"width_ratios": [1.4, 1.2, 1]})
        for a in ax:
            style(a, th)
        width = 0.24
        for j, d in enumerate(data):
            xs = np.arange(len(treated)) + (j - 1) * width
            vals = [peaks[d]["bare"] - peaks[d][k] for k in treated]
            ax[0].bar(xs, vals, width, color=[th["series"][k] for k in treated],
                      alpha=0.45 + 0.25 * j, edgecolor=th["muted"], lw=0.5)
            for x, v in zip(xs, vals):
                ax[0].text(x, v + (0.3 if v >= 0 else -0.9), f"D{d}", ha="center", fontsize=7.5,
                           color=th["muted"])
        for i, k in enumerate(treated):
            ax[0].plot([i - 0.38, i + 0.38], [MODEL_V2[k]] * 2, color=th["text"], lw=1.4, ls="--")
        ax[0].plot([0.62, 1.38], [MODEL_1CM["C40"]] * 2, color=th["text"], lw=1.4, ls=":")
        ax[0].axhline(2.0, color=th["rule"], lw=1.2)
        ax[0].axhline(0, color=th["muted"], lw=0.8)
        ax[0].set_ylim(-1.8, 13)
        ax[0].text(-0.45, 2.2, "H7 threshold 2 °C", fontsize=8, color=th["rule"])
        ax[0].set_xticks(range(len(treated)))
        ax[0].set_xticklabels(treated, color=th["text"])
        ax[0].set_ylabel("peak ΔT vs bare, same day (°C)\npositive = cooler", color=th["muted"])
        ax[0].set_title("(a) Peak cooling, Days 1–3  (dashed: model v2, 2 cm; dotted: 1 cm)",
                        loc="left", fontsize=9.5, color=th["text"])

        temps_axis = np.arange(39.0, 50.01, 0.5)
        for d, ls in ((2, "-"), (3, "--")):
            t, temps, wx, ch = data[d]
            k = (t > SHADOW_FROM_MIN[d] * 60) & (t < t[-1] - 600)
            tt = t[k]
            inner = (tt > tt[0] + 540) & (tt < tt[-1] - 540)
            for name in ("bare", "C40"):
                ys, rate = cooling_rate(tt, temps[name][k], smooth=450)
                r = [rate[inner & (np.abs(ys - T) < 0.75)].mean()
                     if np.any(inner & (np.abs(ys - T) < 0.75)) else np.nan for T in temps_axis]
                ax[1].plot(temps_axis, r, color=th["series"][name], ls=ls, lw=1.5,
                           label=f"{name}, Day {d}")
        ax[1].axvspan(42.5, 44.5, color=th["find"], alpha=0.1)
        ax[1].text(43.5, 1, "LA melting\nrange", ha="center", fontsize=8, color=th["muted"])
        ax[1].set_xlabel("panel back temperature (°C)", color=th["muted"])
        ax[1].set_ylabel("evening cooling rate (°C/h)", color=th["muted"])
        ax[1].set_ylim(0, 45)
        leg = ax[1].legend(frameon=False, fontsize=8)
        for txt in leg.get_texts():
            txt.set_color(th["text"])
        ax[1].set_title("(b) Cooling slows near the melting range", loc="left", fontsize=9.5,
                        color=th["text"])

        loss = [100 * (MASS_G[k][0] - MASS_G[k][1]) / MASS_G[k][0] for k in treated]
        ax[2].bar(treated, loss, color=[th["series"][k] for k in treated], width=0.55,
                  yerr=[100 / MASS_G[k][0] for k in treated], capsize=4, ecolor=th["muted"])
        for i, (k, l) in enumerate(zip(treated, loss)):
            ax[2].text(i, l + 100 / MASS_G[k][0] + 0.4, f"{l:.1f} %\n{MASS_G[k][0]}→{MASS_G[k][1]} g",
                       ha="center", fontsize=8, color=th["text"])
        ax[2].axhline(2.0, color=th["rule"], lw=1.2)
        ax[2].text(-0.4, 2.3, "H7d limit 2 %", fontsize=8, color=th["rule"])
        ax[2].set_ylim(0, 15)
        ax[2].set_xticks(range(len(treated)))
        ax[2].set_xticklabels(treated, color=th["text"])
        ax[2].set_ylabel("mass lost over the campaign (%)", color=th["muted"])
        ax[2].set_title("(c) Slab mass loss, ~72 h in the sun", loc="left", fontsize=9.5,
                        color=th["text"])
        fig.tight_layout()
        fig.savefig(os.path.join(ASSETS, f"field_summary_{mode}.png"), dpi=150, facecolor=th["surface"])
        plt.close(fig)
    print("\nWrote analysis/field_results.txt and assets/field_{days,summary}_{light,dark}.png")


if __name__ == "__main__":
    main()
