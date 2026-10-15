"""
plot_pilot.py - figures for the 15 Oct 2026 pilot run.

Reads Hardware/logs/pilot_2026-10-15.csv and writes light and dark versions of
two figures to assets/:
  pilot_temperatures_*.png  back-surface temperature of the four stations
  pilot_delta_*.png         each PCM station minus the bare station

Values are corrected with the ice offsets from docs/calibration.md before the
differences are taken. A 60 s centred rolling mean smooths the 0.0625 C steps.

Run from the repo root:  python analysis/plot_pilot.py
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "Hardware", "logs", "pilot_2026-10-15.csv")
OUT = os.path.join(ROOT, "assets")

OFFSETS = {"S0_bare": -1.6062, "S1_rbw": -1.3875,
           "S2_composite": -1.8625, "S3_graphite": -1.3687}
LABELS = {"S0_bare": "Bare", "S1_rbw": "RBW alone",
          "S2_composite": "Composite", "S3_graphite": "Composite + graphite"}

THEMES = {
    "light": dict(surface="#fcfcfb", text="#0b0b0b", muted="#52514e", grid="#e4e3df",
                  series={"S0_bare": "#52514e", "S1_rbw": "#2a78d6",
                          "S2_composite": "#eb6834", "S3_graphite": "#1baf7a"}),
    "dark": dict(surface="#1a1a19", text="#ffffff", muted="#c3c2b7", grid="#3a3936",
                 series={"S0_bare": "#c3c2b7", "S1_rbw": "#3987e5",
                         "S2_composite": "#d95926", "S3_graphite": "#199e70"}),
}


def load():
    df = pd.read_csv(CSV, comment="#")
    df["time"] = pd.to_datetime("2026-10-15 " + df["clock_approx"])
    df = df.set_index("time")
    for col, off in OFFSETS.items():
        df[col] = (df[col] + off).rolling("60s", center=True).mean()
    return df


def style(ax, t):
    ax.set_facecolor(t["surface"])
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(t["muted"])
    ax.tick_params(colors=t["muted"], labelsize=10, length=0, pad=6)
    ax.grid(axis="y", color=t["grid"], linewidth=0.8)
    ax.set_axisbelow(True)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.xaxis.set_major_locator(mdates.MinuteLocator(byminute=[0, 30]))


def end_labels(ax, df, cols, t, fmt):
    # direct labels at the right end, nudged apart so they don't collide
    lo, hi = ax.get_ylim()
    gap = (hi - lo) * 0.065
    last = sorted(((df[c].dropna().iloc[-1], c) for c in cols), reverse=True)
    prev = None
    for y, c in last:
        yl = y if prev is None else min(y, prev - gap)
        prev = yl
        ax.plot([df.index[-1]], [y], "o", ms=5, color=t["series"][c],
                mec=t["surface"], mew=1.5, zorder=4)
        ax.annotate(f"{LABELS[c]}  {fmt(y)}", xy=(df.index[-1], y), xycoords="data",
                    xytext=(1.015, yl), textcoords=("axes fraction", "data"),
                    va="center", fontsize=10, color=t["text"], annotation_clip=False)


def fig_temperatures(df, mode):
    t = THEMES[mode]
    fig, ax = plt.subplots(figsize=(11, 5), dpi=160, facecolor=t["surface"])
    style(ax, t)
    cols = list(LABELS)
    for c in cols:
        ax.plot(df.index, df[c], color=t["series"][c], linewidth=2, label=LABELS[c],
                solid_capstyle="round")
    ax.set_ylabel("Back-surface temperature (°C)", color=t["muted"], fontsize=10)
    ax.set_title("Pilot run, 15 Oct 2026: four panels in sun, partly cloudy",
                 loc="left", color=t["text"], fontsize=13, pad=26)
    ax.text(0, 1.03, "Calibrated, 60 s rolling mean. Start time approximate (13:30).",
            transform=ax.transAxes, color=t["muted"], fontsize=9.5)
    leg = ax.legend(loc="upper right", frameon=False, fontsize=10, ncol=2)
    for txt in leg.get_texts():
        txt.set_color(t["text"])
    end_labels(ax, df, cols, t, lambda v: f"{v:.1f} °C")
    fig.subplots_adjust(left=0.08, right=0.75, top=0.86, bottom=0.1)
    fig.savefig(os.path.join(OUT, f"pilot_temperatures_{mode}.png"), facecolor=t["surface"])
    plt.close(fig)


def fig_delta(df, mode):
    t = THEMES[mode]
    fig, ax = plt.subplots(figsize=(11, 4.6), dpi=160, facecolor=t["surface"])
    style(ax, t)
    d = pd.DataFrame(index=df.index)
    cols = ["S1_rbw", "S2_composite", "S3_graphite"]
    for c in cols:
        d[c] = df[c] - df["S0_bare"]
    ax.axhline(0, color=t["muted"], linewidth=1.2)
    ax.text(df.index[int(len(df) * 0.52)], 0.35, "bare panel = 0", color=t["muted"], fontsize=9.5)
    for c in cols:
        ax.plot(d.index, d[c], color=t["series"][c], linewidth=2, label=LABELS[c],
                solid_capstyle="round")
    ax.set_ylabel("Station minus bare (°C)", color=t["muted"], fontsize=10)
    ax.set_title("Below zero = cooler than the bare panel",
                 loc="left", color=t["text"], fontsize=13, pad=26)
    ax.text(0, 1.03, "Not yet corrected for panel-to-panel differences (needs the two all-bare days).",
            transform=ax.transAxes, color=t["muted"], fontsize=9.5)
    leg = ax.legend(loc="upper right", frameon=False, fontsize=10, ncol=3)
    for txt in leg.get_texts():
        txt.set_color(t["text"])
    end_labels(ax, d, cols, t, lambda v: f"{v:+.1f} °C")
    fig.subplots_adjust(left=0.08, right=0.75, top=0.85, bottom=0.11)
    fig.savefig(os.path.join(OUT, f"pilot_delta_{mode}.png"), facecolor=t["surface"])
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    data = load()
    for m in THEMES:
        fig_temperatures(data, m)
        fig_delta(data, m)
    print("Figures written to", OUT)
