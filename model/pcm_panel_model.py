"""
Lumped thermal model of a PV panel with an LA/RBW composite PCM on its back surface.

Bridges the project's bench measurements to panel-scale behaviour, and deliberately
fixes two limitations of Durez & Waqas 2023 (Front. Energy Res.):
  1. It runs MULTI-DAY and reports whether the PCM re-solidifies each night (Durez ran a
     single cycle and so missed that a low-melting PCM never re-freezes in a hot climate).
  2. It models a melting BAND (composite melts ~43->75 C, measured) via the enthalpy
     method, not a single melting point as commercial paraffins allow.

Heat leaves the panel by convection AND long-wave radiation: the front face radiates to
the sky (Swinbank clear-sky temperature) and the ground; an exposed back face (bare
backsheet or composite outer face) radiates to surroundings at ambient. Two mountings:
  "open"      - back exposed to air (open rack)
  "insulated" - back against insulation (roof-integrated); the back path is conduction
                through the insulation plus the outer film, for bare and PCM cases alike.

The genetic-algorithm optimisation of Durez is intentionally NOT reproduced: the material
is already chosen, so there is nothing to optimise over. This script PREDICTS performance
for the chosen composite and outputs a falsifiable predicted field delta-T.

SCAFFOLD STATUS: physical properties below are LITERATURE / TBD placeholders except where
tagged MEASURED. The script runs today on placeholders + synthetic climate to verify the
PHYSICS (behaviour), not the numbers. Replace the PROPS block with DSC / conductivity values
when GIKI results land, then re-run for quantitative predictions.

Outputs (written to ./outputs/):
  - pcm_model_timeseries.csv   tidy per-timestep series
  - pcm_model_summary.txt       peak temps, delta-T, efficiency gain, re-solidification verdict, CAVEATS
  - pcm_model_curves.png        temperatures + liquid fraction over the simulated days

Run:      python pcm_panel_model.py
Requires: numpy, matplotlib
"""

import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "outputs")

# ---- shared dataviz palette (CVD-checked, matches la_regression.py) ----
C_TRIAL1 = "#2a78d6"   # blue
C_TRIAL2 = "#eb6834"   # orange
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_SOFT = "#52514e"
INK_MUTED = "#8a8880"

# =====================================================================
# CONFIG - edit the tagged values when measured data lands
# =====================================================================
# Composite PCM properties. Tags: MEASURED (in-house) / LITERATURE / TBD.
PROPS = {
    "T_solidus_C":   43.0,   # MEASURED  - onset, Session 4 (== pure LA melt)
    "T_liquidus_C":  75.0,   # MEASURED  - liquidus, Session 4 (~55/45 blend, n=1)
    "dH_J_per_g":    76.0,   # PREDICTED - 191 J/g x 0.40 for the C40 field composite; awaiting DSC
    "rho_kg_m3":    900.0,   # TBD       - between molten LA 850 and solid RBW ~975
    "cp_J_per_gK":    2.0,   # LITERATURE- generic organic PCM; awaiting DSC/measurement
    "k_W_mK":         0.2,   # LITERATURE- generic organic PCM; awaiting hot-wire at GIKI
}

# Panel / system. Small mono-Si panel per the proposal (buy 10-20 Wp, keep 4 matched).
PANEL_AREA_M2   = 0.10     # ~0.1 m^2 module face
PCM_THICK_M     = 0.02     # 2 cm field slabs (Oct 2026); same as paper v1 (§3.9.6)
ETA_REF         = 0.18     # reference electrical efficiency at STC
BETA_PER_C      = 0.0043   # -0.43 %/C RATED Pmp coefficient (module datasheet, Yadav et al. 2025) - NOT a field-measured value
T_REF_C         = 25.0     # reference cell temperature
ABS_TAU_ALPHA   = 0.90     # effective transmittance-absorptance product
# Panel thermal mass (glass+cell+tedlar), lumped. ~ areal heat capacity of a thin module.
PANEL_HEATCAP_J_per_m2K = 9000.0   # ~ order of a glass-fronted module per m^2
# Back-face convection to ambient. Applied IDENTICALLY in both cases (bare panel back,
# and the PCM container's outer face) so the comparison is fair - the only difference
# between the two runs is the PCM layer interposed on this same back path.
H_BACK_W_m2K    = 8.0      # sheltered back-surface convection coefficient

# Long-wave radiation
SIGMA           = 5.670e-8 # Stefan-Boltzmann constant, W/m^2.K^4
EPS_FRONT       = 0.85     # glass front face
EPS_BACK        = 0.85     # polymer backsheet
EPS_PCM         = 0.90     # wax composite outer face
TILT_DEG        = 35.0     # panel tilt from horizontal (sets sky/ground view factors)

# Mounting: "open" (back exposed to air) or "insulated" (back against insulation,
# the roof-integrated case). Insulation applies to bare and PCM cases alike.
MOUNTING        = "insulated"
INSUL_K_W_mK    = 0.035    # expanded polystyrene (thermocol)
INSUL_THICK_M   = 0.02     # 2 cm board

# Synthetic diurnal climate - Topi (GIKI, 34.1 N), October field window.
T_NIGHT_C   = 15.0
T_DAY_C     = 29.0
IRRAD_PEAK  = 800.0        # W/m^2 clear-sky midday peak
WIND_MS     = 2.0          # constant wind for the h_w correlation
SUNRISE_H   = 6.5
SUNSET_H    = 18.0

# Simulation controls
N_DAYS  = 3
DT_S    = 2.0              # explicit-Euler timestep


# =====================================================================
# Synthetic climate
# =====================================================================
def ambient_C(t_s):
    """Diurnal ambient temperature. Coolest ~just before sunrise, warmest mid-afternoon."""
    hod = (t_s / 3600.0) % 24.0
    mean = 0.5 * (T_DAY_C + T_NIGHT_C)
    amp = 0.5 * (T_DAY_C - T_NIGHT_C)
    # peak shifted to ~15:00, trough ~03:00
    return mean + amp * np.sin(2 * np.pi * (hod - 9.0) / 24.0)


def irradiance_Wm2(t_s):
    """Clear-sky daylight half-sine, zero at night."""
    hod = (t_s / 3600.0) % 24.0
    if hod < SUNRISE_H or hod > SUNSET_H:
        return 0.0
    frac = (hod - SUNRISE_H) / (SUNSET_H - SUNRISE_H)   # 0..1 across daylight
    return IRRAD_PEAK * np.sin(np.pi * frac)


def h_conv(wind_ms):
    """Wind convection coefficient (Durez Eq 1)."""
    return 5.8 + 3.7 * wind_ms


def T_sky_C(Tamb_C):
    """Clear-sky effective temperature, Swinbank (1963): T_sky = 0.0552 T_amb^1.5 (K)."""
    return 0.0552 * (Tamb_C + 273.15) ** 1.5 - 273.15


def rad_loss(eps, T_C, Tsurr_C, area):
    """Net long-wave radiation (W) from a surface at T_C to surroundings at Tsurr_C."""
    return eps * SIGMA * area * ((T_C + 273.15) ** 4 - (Tsurr_C + 273.15) ** 4)


def front_loss(T_C, Tamb_C, hw, area):
    """Front face: wind convection, plus radiation to sky and ground weighted by view factor."""
    c = np.cos(np.radians(TILT_DEG))
    f_sky, f_gnd = 0.5 * (1 + c), 0.5 * (1 - c)
    return (hw * area * (T_C - Tamb_C)
            + f_sky * rad_loss(EPS_FRONT, T_C, T_sky_C(Tamb_C), area)
            + f_gnd * rad_loss(EPS_FRONT, T_C, Tamb_C, area))


def back_loss(T_C, Tamb_C, eps, area):
    """
    Heat leaving the outermost back surface (bare backsheet, or the composite's outer face).
    open:      convection + radiation to surroundings at ambient.
    insulated: conduction through the insulation board in series with its outer film
               (convection + linearised radiation at 300 K).
    """
    if MOUNTING == "open":
        return H_BACK_W_m2K * area * (T_C - Tamb_C) + rad_loss(eps, T_C, Tamb_C, area)
    h_film = H_BACK_W_m2K + 4 * 0.90 * SIGMA * 300.0 ** 3
    U = 1.0 / (INSUL_THICK_M / INSUL_K_W_mK + 1.0 / h_film)
    return U * area * (T_C - Tamb_C)


# =====================================================================
# Enthalpy-method PCM (melting BAND)
# =====================================================================
# Volumetric properties
_RHO = PROPS["rho_kg_m3"]
_CP = PROPS["cp_J_per_gK"] * 1000.0            # J/kg.K
_LATENT = PROPS["dH_J_per_g"] * 1000.0         # J/kg
_TS = PROPS["T_solidus_C"]
_TL = PROPS["T_liquidus_C"]
_PCM_MASS = _RHO * PANEL_AREA_M2 * PCM_THICK_M  # kg

# Enthalpy reference: H = 0 J/kg at T_solidus, fully solid.
# Below solidus:      sensible only.
# solidus..liquidus:  sensible + latent spread linearly over the band (mushy).
# Above liquidus:     sensible + all latent absorbed.
_H_AT_SOLIDUS = 0.0
_H_AT_LIQUIDUS = _CP * (_TL - _TS) + _LATENT    # J/kg


def T_and_LF_from_H(H):
    """Invert specific enthalpy H (J/kg, ref 0 at solidus) -> (T_C, liquid_fraction)."""
    if H <= _H_AT_SOLIDUS:
        return _TS + H / _CP, 0.0
    if H >= _H_AT_LIQUIDUS:
        return _TL + (H - _H_AT_LIQUIDUS) / _CP, 1.0
    # mushy band: solve H = cp*(T-Ts) + latent*(T-Ts)/(Tl-Ts)
    slope = _CP + _LATENT / (_TL - _TS)         # J/kg per K within the band
    T = _TS + H / slope
    LF = (T - _TS) / (_TL - _TS)
    return T, min(max(LF, 0.0), 1.0)


# =====================================================================
# Two-node lumped simulation
# =====================================================================
def simulate(use_pcm):
    """
    March the panel (and, if use_pcm, the PCM node) with explicit Euler.
    Returns dict of numpy arrays sampled once per minute.
    """
    total_s = int(N_DAYS * 24 * 3600)
    n_steps = int(total_s / DT_S)
    sample_every = int(60.0 / DT_S)             # store 1/min

    UA_pcm = PROPS["k_W_mK"] * PANEL_AREA_M2 / PCM_THICK_M   # panel<->PCM conductance (W/K)

    # initial state: everything at the pre-dawn ambient, PCM fully solid at that T
    T_amb0 = ambient_C(0.0)
    T_panel = T_amb0
    # PCM specific enthalpy so that T_pcm == T_amb0 (solid region, H<0 allowed)
    H_pcm = (T_amb0 - _TS) * _CP
    T_pcm, LF = T_and_LF_from_H(H_pcm)

    ts, Tamb_s, Irr_s, Tpanel_s, Tpcm_s, LF_s, eta_s = [], [], [], [], [], [], []

    Cpanel = PANEL_HEATCAP_J_per_m2K * PANEL_AREA_M2   # J/K for the panel node
    hw = h_conv(WIND_MS)

    for i in range(n_steps):
        t = i * DT_S
        Tamb = ambient_C(t)
        S = irradiance_Wm2(t)

        # panel energy balance (W)
        q_solar = ABS_TAU_ALPHA * S * PANEL_AREA_M2
        q_front = front_loss(T_panel, Tamb, hw, PANEL_AREA_M2)
        if use_pcm:
            # panel conducts into the PCM layer (series resistance k/thickness)
            q_back = UA_pcm * (T_panel - T_pcm)
        else:
            # bare panel: back sheds heat through the SAME back boundary the PCM's outer face uses
            q_back = back_loss(T_panel, Tamb, EPS_BACK, PANEL_AREA_M2)

        dTpanel = (q_solar - q_front - q_back) / Cpanel
        T_panel += dTpanel * DT_S

        if use_pcm:
            # PCM node: gains conduction from panel, sheds from its outer face to ambient
            # via the SAME back boundary the bare panel uses (fair comparison)
            q_out = back_loss(T_pcm, Tamb, EPS_PCM, PANEL_AREA_M2)
            q_to_pcm = q_back            # what entered the PCM from the panel
            dH_total = (q_to_pcm - q_out) * DT_S         # J stored in the PCM
            H_pcm += dH_total / _PCM_MASS                # -> per kg
            T_pcm, LF = T_and_LF_from_H(H_pcm)

        if i % sample_every == 0:
            eta = ETA_REF * (1.0 - BETA_PER_C * (T_panel - T_REF_C))
            ts.append(t / 3600.0)
            Tamb_s.append(Tamb)
            Irr_s.append(S)
            Tpanel_s.append(T_panel)
            Tpcm_s.append(T_pcm if use_pcm else float("nan"))
            LF_s.append(LF if use_pcm else float("nan"))
            eta_s.append(eta)

    return {
        "t_h": np.array(ts),
        "T_amb": np.array(Tamb_s),
        "irr": np.array(Irr_s),
        "T_panel": np.array(Tpanel_s),
        "T_pcm": np.array(Tpcm_s),
        "LF": np.array(LF_s),
        "eta": np.array(eta_s),
    }


# =====================================================================
# Run both cases + derive metrics
# =====================================================================
def main():
    global MOUNTING
    os.makedirs(OUT, exist_ok=True)

    base = simulate(use_pcm=False)
    pcm = simulate(use_pcm=True)

    lines = []

    def emit(s=""):
        lines.append(s)
        print(s)

    # ---- metrics ----
    peak_base = float(np.nanmax(base["T_panel"]))
    peak_pcm = float(np.nanmax(pcm["T_panel"]))
    dT_peak = peak_base - peak_pcm
    eta_gain_mean = float(np.nanmean(pcm["eta"] - base["eta"]))
    eta_gain_pct = 100.0 * eta_gain_mean / ETA_REF

    # daylight-only mean panel-temperature reduction (where cooling matters)
    day_mask = pcm["irr"] > 1.0
    dT_day_mean = float(np.nanmean(base["T_panel"][day_mask] - pcm["T_panel"][day_mask]))

    # re-solidification: minimum LF reached each night (expect ~0 if it re-freezes)
    t_h = pcm["t_h"]
    nightly_min_LF = []
    for d in range(N_DAYS):
        # "night" window of day d: 18:00 of day d to 06:00 of day d+1
        lo = d * 24 + 18.0
        hi = d * 24 + 30.0
        m = (t_h >= lo) & (t_h < hi)
        if np.any(m):
            nightly_min_LF.append(float(np.nanmin(pcm["LF"][m])))
    resolidifies = all(x < 0.05 for x in nightly_min_LF) if nightly_min_LF else False

    peak_LF = float(np.nanmax(pcm["LF"]))
    peak_pcm_T = float(np.nanmax(pcm["T_pcm"]))

    # ---- summary text ----
    emit("=" * 66)
    emit("PV + LA/RBW COMPOSITE PCM - lumped thermal model")
    emit("=" * 66)
    emit(f"Simulated: {N_DAYS} days, synthetic Topi-October climate "
         f"({T_NIGHT_C:.0f}-{T_DAY_C:.0f} C, peak {IRRAD_PEAK:.0f} W/m2)")
    emit(f"Composite: melt band {_TS:.0f}-{_TL:.0f} C, dH {PROPS['dH_J_per_g']:.0f} J/g, "
         f"k {PROPS['k_W_mK']:.2f} W/mK, layer {PCM_THICK_M*1000:.0f} mm, "
         f"mass {_PCM_MASS*1000:.0f} g")
    if MOUNTING == "open":
        emit(f"Mounting: open back (convection + radiation), tilt {TILT_DEG:.0f} deg")
    else:
        emit(f"Mounting: back against {INSUL_THICK_M*1000:.0f} mm insulation "
             f"(k {INSUL_K_W_mK} W/mK) - roof-integrated case, tilt {TILT_DEG:.0f} deg")
    emit("")
    emit("--- Thermal / electrical ---")
    emit(f"Peak back-surface, no PCM : {peak_base:5.1f} C")
    emit(f"Peak back-surface, PCM    : {peak_pcm:5.1f} C")
    emit(f"Peak reduction (delta-T)  : {dT_peak:5.1f} C   <- predicted field peak drop")
    emit(f"Daylight mean T reduction : {dT_day_mean:5.1f} C")
    emit(f"Mean efficiency gain      : {eta_gain_mean*100:5.2f} pts "
         f"({eta_gain_pct:+.1f}% relative)")
    emit(f"H7 target (>= 2 C drop)   : {'MET' if dT_peak >= 2.0 else 'NOT met'}")
    emit("")
    emit("--- Re-solidification (the multi-day check Durez omitted) ---")
    emit(f"Peak liquid fraction      : {peak_LF:.2f}  "
         f"({'fully melts' if peak_LF > 0.95 else 'partial melt'})")
    emit(f"Nightly minimum LF        : "
         + ", ".join(f"{x:.2f}" for x in nightly_min_LF))
    emit(f"Re-solidifies each night  : {'YES - resets daily' if resolidifies else 'NO - saturates'}")
    emit("")
    emit("--- Leakage risk (composite temperature vs C40 bench retention) ---")
    emit(f"Peak composite temperature: {peak_pcm_T:5.1f} C")
    emit("C40 bench result (2 h)    : 0.40% loss at 50 C, 1.47% at 60 C (pass <= 2%), "
         "3.51% at 70 C (fail)")
    emit(f"Verdict                   : "
         + ("inside the tested pass range" if peak_pcm_T <= 60.0
            else "between 60 and 70 C - untested gap" if peak_pcm_T <= 70.0
            else "above 70 C - C40 FAILS retention here"))
    emit("")
    emit("--- Mounting comparison (same composite, same climate) ---")
    mounting_saved = MOUNTING
    emit(f"{'mounting':>10} {'bare peak':>10} {'PCM peak':>9} {'deltaT':>8} {'PCM max T':>10}")
    for mnt in ("open", "insulated"):
        MOUNTING = mnt
        b = simulate(use_pcm=False)
        p = simulate(use_pcm=True)
        bp, pp = float(np.nanmax(b["T_panel"])), float(np.nanmax(p["T_panel"]))
        emit(f"{mnt:>10} {bp:>8.1f} C {pp:>7.1f} C {bp-pp:>+7.1f} {float(np.nanmax(p['T_pcm'])):>8.1f} C")
    MOUNTING = mounting_saved
    emit("")
    emit("--- Sensitivity to thermal conductivity (the graphite question) ---")
    emit(f"k is the dominant unknown (placeholder {PROPS['k_W_mK']:.1f} W/mK). "
         f"Bare-panel peak fixed at {peak_base:.1f} C.")
    emit(f"{'k (W/mK)':>9} {'PCM peak':>9} {'deltaT':>8} {'peak LF':>8}")
    k_saved = PROPS["k_W_mK"]
    for k in (0.2, 0.5, 1.0, 2.0, 6.0):
        PROPS["k_W_mK"] = k
        p = simulate(use_pcm=True)
        pk = float(np.nanmax(p["T_panel"]))
        emit(f"{k:>9.1f} {pk:>8.1f} C {peak_base-pk:>+7.1f} {float(np.nanmax(p['LF'])):>8.2f}")
    PROPS["k_W_mK"] = k_saved
    emit("Interpretation: deltaT > 0 means the composite panel runs cooler than bare. Low k")
    emit("adds thermal resistance on the back path; whether storage outweighs it depends on")
    emit("how much the bare back can shed on its own - see the mounting comparison above.")
    emit("")
    emit("--- CAVEATS ---")
    emit("* Synthetic climate, not measured Topi weather - swap in real hourly data.")
    emit("* dH, rho, cp, k are LITERATURE/TBD placeholders pending DSC + hot-wire at GIKI;")
    emit("  the composite liquidus (75 C) and solidus (43 C) are MEASURED (n=1, Session 4,")
    emit("  ~55/45 blend - the C40 liquidus is not yet measured).")
    emit("* Lumped 2-node model: no in-layer gradient, no natural convection in the melt,")
    emit("  panel heat capacity is an order-of-magnitude estimate.")
    emit("* Radiation: Swinbank clear-sky temperature; back surroundings taken at ambient;")
    emit("  emissivities assumed (glass 0.85, backsheet 0.85, wax 0.90).")
    emit("* Convection correlation (Durez Eq 1) is for full-size modules; mini panels shed")
    emit("  heat more easily, so absolute temperatures here are likely high.")
    emit("* NOT yet field-validated. This run verifies BEHAVIOUR, not quantitative values.")
    emit("* delta-T above is a pre-registered PREDICTION to test against the October field run.")

    with open(os.path.join(OUT, "pcm_model_summary.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # ---- energy-conservation spot check (reported, not printed to summary) ----
    # (implicit in the Euler march; a gross check is that temps stay physical)

    # ---- timeseries CSV ----
    with open(os.path.join(OUT, "pcm_model_timeseries.csv"), "w", newline="",
              encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["t_hours", "T_ambient_C", "irradiance_Wm2",
                    "T_panel_noPCM_C", "T_panel_PCM_C", "T_pcm_C",
                    "liquid_fraction", "eta_noPCM", "eta_PCM"])
        for i in range(len(pcm["t_h"])):
            w.writerow([f"{pcm['t_h'][i]:.4f}",
                        f"{pcm['T_amb'][i]:.2f}",
                        f"{pcm['irr'][i]:.1f}",
                        f"{base['T_panel'][i]:.2f}",
                        f"{pcm['T_panel'][i]:.2f}",
                        f"{pcm['T_pcm'][i]:.2f}",
                        f"{pcm['LF'][i]:.3f}",
                        f"{base['eta'][i]:.4f}",
                        f"{pcm['eta'][i]:.4f}"])

    # ---- figure ----
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6.5), sharex=True,
                                   facecolor=SURFACE)
    for ax in (ax1, ax2):
        ax.set_facecolor(SURFACE)
        for s in ax.spines.values():
            s.set_color(INK_MUTED)
        ax.tick_params(colors=INK_SOFT)
        ax.grid(True, color="#e6e5e2", linewidth=0.7)

    ax1.plot(pcm["t_h"], pcm["T_amb"], color=INK_MUTED, lw=1.3, label="Ambient")
    ax1.plot(base["t_h"], base["T_panel"], color=C_TRIAL2, lw=1.8, label="Back-surface, no PCM")
    ax1.plot(pcm["t_h"], pcm["T_panel"], color=C_TRIAL1, lw=1.8, label="Back-surface, with PCM")
    ax1.set_ylabel("Temperature (C)", color=INK)
    ax1.set_title("PV back-surface temperature: composite PCM vs bare panel",
                  color=INK, loc="left", fontsize=11)
    ax1.legend(frameon=False, fontsize=8, labelcolor=INK_SOFT)

    ax2.plot(pcm["t_h"], pcm["LF"], color=C_TRIAL1, lw=1.8)
    ax2.axhline(0.0, color=INK_MUTED, lw=0.8, ls="--")
    ax2.axhline(1.0, color=INK_MUTED, lw=0.8, ls="--")
    ax2.set_ylim(-0.08, 1.08)
    ax2.set_ylabel("Liquid fraction", color=INK)
    ax2.set_xlabel("Time (hours)", color=INK)
    ax2.set_title("PCM liquid fraction - does it re-solidify each night?",
                  color=INK, loc="left", fontsize=11)
    # day/night shading
    for d in range(N_DAYS):
        ax2.axvspan(d*24 + SUNSET_H, d*24 + 24 + SUNRISE_H, color="#00000008")

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "pcm_model_curves.png"), dpi=200, facecolor=SURFACE)
    plt.close(fig)

    print()
    print(f"Wrote outputs to: {OUT}")


if __name__ == "__main__":
    main()
