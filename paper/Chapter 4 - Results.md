# 4. Results

> **Status.** §4.1–4.5 and §4.9–4.10 are complete. §4.6–4.8 (DSC, FTIR, SEM) and the SOAK arm
> are laid out with the tables they will carry and marked ⚠️ [PENDING]. Every number in §4.4
> comes from `Data Analysis/outputs/leak_matrix_results.txt`, every field number from
> `outputs/field_results.txt`, and every model number from `outputs/pcm_model_analysis.txt` and
> `outputs/pcm_model_summary.txt`; the scripts in `Data Analysis/` regenerate them. Items still
> to confirm are gathered at the end of the chapter.

---

## 4.1 Pure component melting points

Both components were heated in the water bath of §3.4 and read from a 1 °C glass thermometer,
which plateaued at **98 °C** in boiling water at the 450 m site (expected ≈ 98.5 °C), so no
correction was applied.

### Lauric acid

**Table 4.1.** Lauric acid, two heating trials (n = 2).

| | Mass | Pre-melt ramp | Onset | Plateau | Clear-melt |
|---|---|---|---|---|---|
| Trial 1 | 4.95 g | 1.33 °C/min | 43 °C | **43.0 °C, held 4.0 min** (8 readings) | 46.5 °C |
| Trial 2 | 5.12 g | 2.13 °C/min | 44 °C | none | 52 °C |

Melting onset is **43–44 °C**, matching the literature 43.8 °C within the thermometer's
resolution, so the supplied acid is taken as validated.

The trials also give a methodological result. Trial 2's ramp was steeper by **+0.80 °C/min**
(95 % CI 0.47–1.13; t(15) = 5.22, p = 0.0001; optimistic, §3.9.2). Through the transition,
Trial 1's rate of rise fell to **35 %** of its sensible rate and Trial 2's only to **86 %**:
Trial 2 outran the latent absorption. The onset moved by 1 °C between trials, the "fully
melted" reading by **5.5 °C**. Mass does not explain this, since the heavier Trial 2 should
have ramped more slowly. **Onsets and plateaus are robust; the visual clear-melt endpoint is
not**, which is why transitions are read from arrests and *k*<sub>eff</sub> dips throughout.

![Figure 4.1](../Data%20Analysis/outputs/la_heating_curves.png)

**Figure 4.1.** Lauric acid, Trials 1 and 2, with fitted pre-melt ramps and melt segments.
Trial 1 holds 43.0 °C for 4.0 min; Trial 2, ramped about 60 % faster, climbs straight through.
Dashed line: the 43.8 °C literature value.

### Rice bran wax

**Table 4.2.** Rice bran wax (batch PR 1798).

| | Mass | Method | Transition | Note |
|---|---|---|---|---|
| Trial 1 | 4.79 g | plateau | **73 °C**, flat 5.25 min (18 readings) | clear-melt 84 °C |
| Trial 2 | 4.45 g | plateau | apparent flat at 82 °C, 1.75 min | bath not logged; **not a melting arrest** (see Trial 3) |
| Trial 3 | not recorded | bath-logged *k*<sub>eff</sub> | **70–73 °C**, lowest *k*<sub>eff</sub> of six bands | no visible plateau; *k*<sub>eff</sub> highest at 79–83 °C |

**Table 4.3.** Trial 3, *k*<sub>eff</sub> by sample-temperature band (integrated form, §3.4).

| Band (°C) | 63–67 | 67–70 | **70–73** | 73–76 | 76–79 | 79–83 |
|---|---|---|---|---|---|---|
| *k*<sub>eff</sub> (min⁻¹) | 0.090 | 0.138 | **0.058** | 0.101 | 0.113 | 0.175 |

Two independent observables place the wax transition at **70–73 °C**: Trial 1's 5.25 min
plateau, and Trial 3's lowest *k*<sub>eff</sub> band (36 % below the next-lowest, 49 % below the
median of the others), visible only once the rate is divided by the still-rising bath–sample
difference. Trial 2's 82 °C flat did not reproduce: Trial 3 has its *highest* *k*<sub>eff</sub>
at 79–83 °C, so no latent heat was absorbed there, and the flat is attributed to heat input.

![Figure 4.2](../Data%20Analysis/outputs/fig_rbw.png)

**Figure 4.2.** Rice bran wax. (a) Plateau Trials 1 and 2, bath not logged; grey band, the
literature melting range. (b) Trial 3, bath logged: *k*<sub>eff</sub> by band; the 70–73 °C band
(orange) is the lowest.

The transition lies **about 5 °C below** the 77–79 °C of Dassanayake et al. (2009). A
thermometer offset is excluded by the boiling-point and lauric-acid checks. RBW is a mixture of
long-chain esters whose distribution depends on source and refining, so a lower-melting
fraction is plausible even at a stated 99 % grade. DSC on the raw wax is the arbiter (§4.6)
⚠️ [PENDING].

## 4.2 Composite melting behaviour (preliminary)

> **Preliminary.** Masses were not recorded for the water-bath composite runs, so their
> compositions are approximate. The quantified version is the composition-series melting test
> on specimens set aside at casting ⚠️ [PENDING — run / not run?] and the DSC series (§4.6).

The properly mixed run (≈ 55 wt % lauric acid, bath logged, heated continuously) melts over
**43 → 75 °C**.

**Table 4.4.** Composite (≈ 55 wt % LA), *k*<sub>eff</sub> by band, and relative to the run's
maximum.

| Band (°C) | 38–43 | **43–45** | **45–47** | **47–50** | 50–57 | 57–67 | 67–75 |
|---|---|---|---|---|---|---|---|
| *k*<sub>eff</sub> (min⁻¹) | 0.091 | **0.028** | **0.048** | **0.030** | 0.171 | 0.497 | 0.201 |
| relative | 0.18 | **0.06** | **0.10** | **0.06** | 0.34 | 1.00 | 0.40 |

Melting proceeds in **two stages** (Table 4.4, Figure 4.3). From **43 to 50 °C the acid melts**:
*k*<sub>eff</sub> falls to 6–10 % of its maximum, so most incoming heat goes into latent form.
From **50 to 75 °C the residual wax dissolves**, absorbing little heat but visibly: 90 % melted
at 72 °C, 5 % solid at 73 °C, fully melted at **75 °C**. The bath was still 13 °C hotter at the
end, so 75 °C is a genuine completion, not an equilibrium ceiling.

![Figure 4.3](../Data%20Analysis/outputs/fig_composite.png)

**Figure 4.3.** Properly mixed composite (≈ 55 wt % lauric acid). (a) Bath and sample
temperatures with the visual milestones. (b) *k*<sub>eff</sub> by band relative to its maximum;
the 43–50 °C bands (orange) are where the acid melts.

A second, lower-acid run was not a clean replicate (different mixing, pre-warmed bath, heat cut
mid-run, stopped at 77 °C "almost" melted). Its main absorption moved to **54–58 °C** and its
liquidus is bounded at **≥ 77 °C**, as a lower acid fraction should give. Both runs put the last
solid in the **mid-70s °C**. The pre-registered ideal-mixing liquidus is **≈ 67 °C at 50 wt %**;
the observed **≈ 75 °C at ≈ 55 wt %** is at least 8 °C higher, so the wax is *less* soluble in
molten lauric acid than ideal mixing predicts (§5.2). Bulk latent heat is thus delivered at
43–50 °C, inside the PV window, while solid wax persists above it; whether that solid
**retains** the liquid is a mechanical question answered in §4.4.

## 4.3 Absence of a useful eutectic

The ideal-mixing model put the eutectic at **43.72 °C**, indistinguishable from pure lauric
acid. Composite onsets were **43, 43 and 44 °C** in three runs (one being the withdrawn,
poorly mixed run, whose onset still reflects the acid). No melting-point depression is seen. A
*useful* eutectic, in the fatty-acid sense of a melting point well below either component
(lauric/stearic acid at 31.2 °C; Wang et al., 2022), does not form. The wax dilutes latent heat
roughly in proportion to the acid fraction (≈ 95 J/g at 50 wt % on the 191 J/g × *w* rule, to be
checked by DSC, §4.6). The wax's role is containment only.

---

## 4.4 Retention versus temperature

### 4.4.1 Completeness of the matrix

The full design was run: **63 specimens**, none voided. Initial masses were **4.0–5.4 g**
(mean 4.73 ± 0.34 g), not the nominal 7 g. Six specimens **collapsed**, all replicates of 70 and
80 wt % at 70 °C, and are recorded as definitive fails without a leakage value (§3.3.7). The
call was not borderline: the largest loss among the 57 intact specimens was **10.6 %**, the
smallest among the collapsed **42.3 %**.

Three supporting items are incomplete. **Dish, sealed-control and 60/70 °C blank masses** are
in the notebook but not yet in the analysed workbook ⚠️ [TRANSCRIBE], so the cross-check
(§4.4.5) currently covers paper gain only. **Stain-area photographs** were not taken.
**Long-hold behaviour** awaits the SOAK arm (§4.5) ⚠️ [PENDING]; until then all values here are
**two-hour** leakage, not equilibrium values. The primary measurement, specimen mass loss, needs
none of these.

### 4.4.2 Leakage across the matrix

**Table 4.5.** Leakage after a two-hour hold, % of initial specimen mass, mean ± SD (n = 3),
range in brackets. **Bold** marks a mean that fails the ≤ 2 wt % criterion.

| wt % LA | 50 °C | 60 °C | 70 °C |
|---|---|---|---|
| 20 | 0.1 ± 0.1 [0.0–0.2] | 0.6 ± 0.6 [0.2–1.3] | **2.5 ± 0.7** [1.9–3.1] |
| 30 | 0.3 ± 0.1 [0.2–0.4] | 0.8 ± 0.3 [0.5–1.1] | **3.2 ± 0.5** [2.7–3.7] |
| 40 | 0.4 ± 0.5 [0.0–1.0] | 1.5 ± 0.3 [1.2–1.8] | **3.5 ± 0.6** [3.1–4.2] |
| 50 | 0.3 ± 0.3 [0.0–0.6] | **3.2 ± 1.2** [2.3–4.6] | **7.2 ± 1.7** [5.6–8.9] |
| 60 | 0.3 ± 0.2 [0.2–0.6] | **3.2 ± 0.8** [2.3–3.8] | **10.0 ± 0.7** [9.2–10.6] |
| 70 | 0.7 ± 0.4 [0.2–1.0] | **3.8 ± 0.9** [3.0–4.8] | **collapsed** (3/3) |
| 80 | 1.3 ± 0.7 [0.6–1.9] | **6.9 ± 1.8** [5.0–8.6] | **collapsed** (3/3) |

*At 50 °C only 5 of 21 specimens reached the LOQ of 0.64 %; the 20–60 wt % values there cannot
be ranked. At 60 °C 18 of 21 did, and at 70 °C all 15 intact specimens.*

![Figure 4.4](../Data%20Analysis/outputs/leak_matrix_composition.png)

**Figure 4.4.** Leakage against lauric-acid loading at 50, 60 and 70 °C. Small points:
individual specimens; large points: means ± SD (n = 3); crosses: specimens that collapsed at
70 °C, shown in a separate band because they have no leakage value. Dashed line: the 2 wt %
criterion.

**At 50 °C every composition passes** (highest mean 1.3 % at 80 wt %). **At 60 °C the series
splits:** 20–40 wt % pass at 0.6–1.5 %, while every specimen from 50 wt % up fails; leakage is
nearly flat across 50–70 wt % (3.2–3.8 %) and doubles at 80 wt %. **At 70 °C nothing passes:**
leakage climbs from 2.5 % to 10.0 % across 20–60 wt %, and 70–80 wt % collapse.

![Figure 4.5](../Data%20Analysis/outputs/leak_matrix_temperature.png)

**Figure 4.5.** Mean leakage against temperature, one line per composition. Every composition
leaks more at each step up in temperature.

### 4.4.3 The retention limit X(T)

**Table 4.6.** Retention limit X(T), interpolated as in §3.3.8. The bootstrap interval captures
replicate scatter only and assumes linearity between adjacent compositions.

| Temperature | X(T), wt % LA | Bracketing pair | Bootstrap 95 % CI |
|---|---|---|---|
| 50 °C | **≥ 80** | top of tested range passes | not bracketed |
| 60 °C | **43.0** | 40 wt % pass (1.47 %) / 50 wt % fail (3.22 %) | 41.2–46.4 |
| 70 °C | **< 20** | bottom of tested range fails (2.45 %) | not bracketed |

![Figure 4.6](../Data%20Analysis/outputs/leak_matrix_xt.png)

**Figure 4.6.** The primary result: retention limit X(T) against temperature. Filled circles,
the pre-registered 2 % criterion; grey squares, a 5 % criterion (sensitivity check, not
pre-registered). Arrows mark limits outside the 20–80 wt % range tested.

**The retention limit falls from above 80 wt % at 50 °C to 43 wt % at 60 °C and below 20 wt % at
70 °C.** Only X(60) is located; the others are bounds. The 2 % line is strict for a mostly-acid
composite: assuming the escaped liquid is lauric acid (not analysed), every intact specimen kept
at least ~83 % of its acid after two hours. A 5 % criterion moves X(60) to **74 wt %** (CI 71–77)
and locates X(70) at **44 wt %** (CI 43–47); it shows how much the headline depends on the line
and does not replace the pre-registered value.

### 4.4.4 Statistical tests

One-sided permutation tests (seed 20261003, 10⁵ resamples); collapsed specimens rank above all
measured values.

- **Temperature.** JT stratified by composition = 187.5 of a possible 189 (**p < 10⁻⁵**); each
  step alone, 50 → 60 °C (U = 61.5 of 63) and 60 → 70 °C (U = 63 of 63), p < 10⁻⁵. The mean rose
  at **7 of 7** compositions at each step (sign test p = 0.008).
- **Composition.** Leakage rises with loading at every temperature (JT p = 0.0004 at 50 °C,
  p < 10⁻⁵ at 60 and 70 °C), and the trend persists within the 20–60 wt % specimens that stayed
  intact (p < 10⁻⁵ at 70 °C, 2 × 10⁻⁵ at 60 °C), so it is not an artefact of the collapsed cells.
- **Collapse.** At 70 °C, 6 of 6 specimens at ≥ 70 wt % collapsed against 0 of 15 at ≤ 60 wt %
  (Fisher p = 2 × 10⁻⁵). This is **descriptive only**, since the split was read off the data;
  whether failure at 70 °C is a step or a steep ramp is not resolved.

### 4.4.5 Measurement validity

**Mass balance.** For intact specimens losing ≥ 0.03 g (n = 41), paper gain against specimen
loss has slope **0.87** and **r = 0.976** (Figure 4.7). The paper recovered **84 %, 91 % and
89 %** of the loss at 50, 60 and 70 °C; the small unaccounted remainder (mean 0.004, 0.011 and
0.028 g) grows with temperature, consistent with evaporation or liquid running past the paper.
The dish and sealed-control masses will separate the two ⚠️ [UPDATE once transcribed]. Either
way, the primary figure measures liquid leaving the specimen, not paper moisture or handling.

![Figure 4.7](../Data%20Analysis/outputs/leak_matrix_mass_balance.png)

**Figure 4.7.** Paper gain against specimen loss for all 63 specimens (left) and intact
specimens only (right), with the 1 : 1 line.

**Run-to-run variation.** No oven run read systematically high or low (within-cell permutation
p = 0.62, 0.62, 0.69). Pooled within-cell SDs (0.38, 1.0 and 0.9 % at 50, 60 and 70 °C) are
small against the differences between temperatures.

**Collapsed specimens** left 47–58 % (70 wt %) and 26–36 % (80 wt %) of their mass as residue,
and their papers gained 2.0–3.1 g. These are recorded as "collapsed, leakage not separable" and
used nowhere as leakage values.

### 4.4.6 Outcome against the pre-registered hypotheses

- **H1 (retention depends on loading): supported.** Pass and fail both occur; at 60 °C the
  series divides between 40 and 50 wt %.
- **H2 (service limit): not falsified.** Every composition leaks more at each temperature step.
  The 2 % crossing lies **between 50 and 60 °C for 50–80 wt %** and **between 60 and 70 °C for
  20–40 wt %**; both intervals overlap the predicted 55–68 °C, but three temperatures cannot
  locate the crossing within them. The result is consistent with the prediction, not a test of
  it at that resolution.
- **H3–H6** depend on DSC, FTIR and SEM (§4.6–4.8) and, for H4's retention component, on cycling
  (§4.5). **H7** is reported in §4.9.

---

## 4.5 Thermal cycling stability (C40)

### 4.5.1 What was run

C40 was cycled as the highest loading passing at 60 °C. Logged hot legs ran 24–28 min and sum to
**634 min (≈ 10.6 h)** over 25 cycles (the workbook's 609 min omits cycle 18, whose logged times
give 25 min). Three cool legs were short of the 25 min target (6 min after cycles 7 and 18, 4 min
after cycle 22); whether the specimens were dull white before re-entry is ⚠️ [CONFIRM]. Whether
the cycled specimens came from the original casting is ⚠️ [CONFIRM]; the baseline comparison is
valid only for the same casting. The SOAK arm (2 × C40, 634 min at 60 °C) is ⚠️ [PENDING].

### 4.5.2 Result

**Table 4.7.** C40 after 25 melt–freeze cycles at 60 °C (≈ 10.6 h total hot time).

| Specimen | m₀ (g) | m₁ (g) | Leakage % | Paper gain (g) | Dish gain (g) | Transfer % | Closure (g) | Appearance |
|---|---|---|---|---|---|---|---|---|
| CYC-1 | 5.04 | 4.22 | 16.3 | 0.45 | 0.18 | 12.5 | 0.19 | intact, hollow at top |
| CYC-2 | 4.99 | 4.17 | 16.4 | 0.40 | 0.28 | 13.6 | 0.14 | intact, hollow at top |
| CYC-3 | 4.31 | 3.64 | 15.5 | 0.39 | 0.27 | 15.3 | 0.01 | intact, hollow at top |
| **Mean ± SD** | | | **16.1 ± 0.5** | | | 13.8 | 0.11 | 0/3 collapsed |
| SOAK (n = 2) | ⚠️ | ⚠️ | **[PENDING]** | | | | | |
| Baseline, 2 h (n = 3) | | | **1.5 ± 0.3** | | | | | intact |

*Transfer % is not yet blank-corrected ⚠️ [enter BLANK-CYC masses].*

**The cycled specimens lost 16.1 ± 0.5 %, eleven times the two-hour baseline (1.47 ± 0.33 %).**
If the escaped liquid is lauric acid, that is ≈ 40 % of the acid present, against ≈ 4 % after two
hours. None collapsed, but all three had a hollow in the upper face, consistent with liquid
draining downward. The dishes gained 0.18–0.28 g; without them Transfer would have recovered
about half the loss, with them 77–99 %. Two specimens exceed the 0.4-point Leakage–Transfer flag
and are kept, as §3.3.7 requires.

![Figure 4.8](../Data%20Analysis/outputs/fig_cycling.png)

**Figure 4.8.** C40 at 60 °C: leakage after the 2 h matrix hold and after 25 melt–freeze cycles
(≈ 10.6 h hot). Points: individual specimens; bars: mean ± SD. The soak arm is pending.

### 4.5.3 What the comparison can and cannot yet say

Hot time differs between the arms, so the increase cannot yet be attributed to cycling. Linear
accumulation at the two-hour rate would give **≈ 7.8 %** over 10.6 h, half the observed loss,
and hold-time curves for other composite classes flatten rather than rise linearly (Khalaf
Alshammari et al., 2024). The **SOAK arm** decides ⚠️ [PENDING]:

- **SOAK ≈ CYC (within 1 pp):** the loss is caused by time at 60 °C, not by melting and
  freezing, and the two-hour X(T) is an early-time value.
- **SOAK < CYC by more than 1 pp:** repeated phase change loosens the network beyond hot time.
- **SOAK > baseline in either case:** retention at 60 °C is time-dependent, and X(T) must carry
  its hold time.

**H4, retention component: not met by the literal criterion** (≥ 5 % drift; leakage rose from
1.5 % to 16.1 %). Attribution awaits SOAK. The enthalpy, onset and supercooling components come
from DSC (§4.6) and the new-band criterion from FTIR (§4.7). The tilted settling assay was not
run (§3.5.2); the "hollow at top" is the small-scale version of the failure it was designed to
detect.

---

## 4.6 Thermal properties by DSC

⚠️ [PENDING — GIKI results.] Programme as requested (§3.7, Appendix C); ⚠️ [confirm the
programme actually run from the facility report].

**Table 4.8.** DSC results (second heat unless stated).

| Sample | Onset (°C) | Peak (°C) | ΔH (J/g) | Predicted ΔH = 191 × *w* (J/g) | Crystallisation onset (°C) | Supercooling (°C) |
|---|---|---|---|---|---|---|
| Raw RBW (PR 1798) | | | | — | | |
| Pure lauric acid | | | | 191 | | |
| C30 | | | | 57 | | |
| C40 *(optimum, if submitted)* | | | | 76 | | |
| C50 | | | | 96 | | |
| C70 | | | | 134 | | |
| C40 after cycling *(if submitted)* | | | | 76 | | |

Statements to make once the data are in:

1. **Wax melting point:** does DSC confirm the 70–73 °C arrest (§4.1) or the 77–79 °C literature
   value?
2. **H3:** ΔH against *w*(LA) with the zero-intercept 191 J/g line. A slope 4–7 % low is the
   expected offset (§1); H3 is falsified only by **non-linearity** beyond scatter.
3. **Hidden transitions** between the acid and wax melts.
4. **H4, supercooling:** composite against neat acid at matched mass and cooling rate.
5. **H4, enthalpy drift:** cycled against uncycled C40, criterion < 5 %.

## 4.7 Spectroscopic analysis (FTIR / ATR)

⚠️ [PENDING — GIKI results.] Samples: pure LA, raw RBW, composites `[30 / 50 / 70 or all
seven]`, cycled C40.

**Table 4.9.** Carbonyl band positions (cm⁻¹).

| Sample | Acid C=O (~1700) | Ester C=O (~1735) | Shift vs pure component | New bands? |
|---|---|---|---|---|
| Pure LA | | — | — | — |
| Raw RBW | — | | — | — |
| C30 / C50 / C70 | | | | |
| C40 cycled | | | | |

Statements to make: **H5**, whether the composite spectrum is a superposition (a carbonyl shift
growing with composition would indicate acid–ester hydrogen bonding; check also the
2500–3300 cm⁻¹ O–H region); **H4**, whether new bands appear after cycling, including any
oxidation from the staggered oven residence at casting.

## 4.8 Microstructure (SEM)

⚠️ [PENDING — run / not run.] Samples: raw RBW, one low- and one high-LA composite, uncycled and
cycled C40. Statements to make: **H6**, network density and needle length (ImageJ, n ≥ 30)
against pass/fail in Table 4.5; and whether the cycled network is coarser. If SEM was not
obtained, H6 is reported as **untested**, not failed.

---

## 4.9 Field evaluation

Three days were logged in Al Khobar (15–17 October 2026) with four insulated-back mini panels:
bare, RBW alone, C40 and C40 + graphite, each slab 14 × 7 × 1 cm (§3.6). Every reading is kept:
6,514 on Day 1 (from 13:30), 7,417 on Day 2 (from 11:47) and 12,725 on Day 3 (from 11:45, past
sunset), with no gaps or failed reads. Modelled cloud never exceeded 7 %. No panel correction
is applied (§6).

![Figure 4.9](../Data%20Analysis/outputs/field_days.png)

**Figure 4.9.** Back-surface temperature of the four stations on each day, ice-corrected, with
modelled air temperature (dashed), sunlight and wind (Open-Meteo model data). Blue: the first
90 min (findings window, post hoc). Grey: the row in shadow (Day 2 from ≈ 95 min; Day 3 from
≈ 180 min). No reading is removed.

**Table 4.10.** Pre-registered main number: each slab station's daily peak subtracted from the
bare station's (positive = cooler than bare), and slab mass over the three days outdoors (1 g
scale).

| Station | Day 1 | Day 2 | Day 3 | Mean ± SD | 95 % CI (n = 3) | Mass before → after | Mass loss |
|---|---|---|---|---|---|---|---|
| Bare peak (°C) | 63.6 | 69.9 | 76.1 | — | — | — | — |
| B — RBW alone | +6.2 | +3.2 | +10.7 | **+6.7 ± 3.7** | −2.6 to +16.0 | 98 → 98 g | **0 %** |
| C — C40 | +6.1 | +1.6 | +11.9 | **+6.5 ± 5.2** | −6.3 to +19.4 | 96 → 94 g | **2.1 %** (±≈ 1 %) |
| D — C40 + graphite | +4.5 | −0.2 | +8.1 | **+4.1 ± 4.2** | −6.2 to +14.5 | 100 → 89 g + fragments | **11 %** |
| C − B (latent over mass) | −0.1 | −1.7 | +1.2 | −0.2 ± 1.4 | −3.8 to +3.4 | | |
| D − C (graphite) | −1.7 | −1.8 | −3.8 | −2.4 ± 1.2 | −5.4 to +0.6 | | |

![Figure 4.10](../Data%20Analysis/outputs/field_summary.png)

**Figure 4.10.** (a) Daily peak ΔT against bare for each slab (D1–D3), with the pre-registered
v2 prediction for 2 cm slabs (dashed) and the same model at the as-built 1 cm (dotted, C40);
orange, the 2 °C H7 threshold. (b) Evening cooling rate against module temperature after the row
loses sun, bare and C40, Days 2 (solid) and 3 (dashed); blue band, lauric acid's melting range
(post hoc). (c) Slab mass loss; bars ±1 g; orange, the 2 % H7d limit.

### 4.9.1 Peak cooling (H7)

The C40 slab lowered the daily peak by **6.5 °C** on average, more on hotter days: 1.6 °C on Day
2, 6.1 °C on Day 1 and 11.9 °C on Day 3, when bare reached 76.1 °C. The bare panel had the
highest peak every day except Day 2, when the graphite station exceeded it by 0.2 °C.

**H7: the mean exceeds the pre-registered 2 °C threshold, but the effect is not statistically
established.** On the field pre-registration's criterion (falsified if mean ΔT < 2 °C) H7 is
met. On the stricter condition of §1.2 it is not established: the design had no crossover, so
no crossover correction is possible, and with three days and one module per treatment the 95 %
CI (−6.3 to +19.4 °C) includes zero. The direction was the same on all three days. The measured
mean is more than three times the v2 prediction for a 2 cm slab (+1.9 °C) and eight times the
+0.8 °C the same model gives for 1 cm.

At matched sunlight (≥ 600 W/m², post hoc) the slab panels averaged 6.0 °C (C40), 5.4 °C (RBW)
and 3.5 °C (C40 + graphite) cooler than bare. In the evening the order reversed as the slabs
released stored heat (Day 3, last 30 min: bare 29.7 °C, RBW 30.9 °C, C40 30.3 °C, C40 + graphite
31.1 °C).

### 4.9.2 Latent heat over thermal mass (H7a)

**Across the three days, wax alone cooled the peak as much as C40 (C − B = −0.2 ± 1.4 °C), so
H7a, as pre-registered, is not supported. On the hottest day, however, the acid's latent heat
is visible: from 80 min until the row lost sun, C40 held near 55 °C while wax alone climbed to
62–64 °C.**

**Table 4.11.** Day 3, ice-corrected module rear temperature (°C, 2 min means), minutes after
11:45. Negative C − B means C40 cooler than wax alone.

| Minute | 40 | 75 | 82 | 100 | 120 | 150 | 175 |
|---|---|---|---|---|---|---|---|
| Bare | 68.8 | 63.1 | 65.8 | 64.7 | 64.4 | 64.0 | 59.8 |
| B — RBW alone | 59.7 | 57.8 | 60.2 | 61.2 | 62.2 | 63.6 | 61.7 |
| C — C40 | 63.1 | 61.0 | 54.6 | 54.6 | 54.6 | 54.7 | 52.0 |
| C − B | +3.4 | +3.2 | −5.6 | −6.6 | −7.6 | −8.9 | −9.7 |

- **Day 3, 13:05–14:45.** For the first 78 min C40 ran 1–5 °C *warmer* than wax alone. At
  ≈ 80 min its reading fell ≈ 6 °C in about four minutes while the other three kept heating,
  then held almost flat at 54.6–54.7 °C for over an hour, **≈ 8 °C cooler than wax alone and
  ≈ 10 °C cooler than bare** (95–180 min means: C40 54.1 °C, RBW 62.4 °C, bare 63.6 °C) until
  the row lost sun (Table 4.11). The row was checked every 30 min and the C40 station was not
  shaded, and after sunset the C40 and wax stations read within 0.54 °C of bare, so panel bias
  cannot account for an 8 °C gap. A module temperature held flat while its neighbours keep
  heating is the signature of latent absorption at the interface the sensor reads, and the
  slab's latent capacity, 96 g × ≈ 76 J/g ≈ 7 kJ, is of the order needed if most of the acid
  melted in this window. The abruptness of the initial fall suggests that the softening slab
  also settled into closer contact with the module and sensor (a light smudge of composite was
  later found around the sensor); contact and latent heat cannot be separated with these data.
  On Days 1 and 2 no such margin appeared (C40 0.1 and 1.7 °C warmer than wax at peak).
- **Evening freezing (Figure 4.10b, post hoc).** On Day 2, C40 cooled at **5.9 and 4.5 °C/h at
  44 and 42 °C**, against 14.1 and 23.7 °C/h for bare at the same temperatures. On Day 3 the
  contrast was weaker (C40 8.7 and 6.1; bare 10.2 and 12.4 °C/h), and RBW and C40 + graphite
  also slowed near 42 °C. This is the freezing arrest H4 predicts at bulk scale.

**H7c** (melt by day, freeze by night, from outer-face sensors) was not tested: no outer-face
sensors were fitted. The evening cooling rates are indirect evidence only.

### 4.9.3 Graphite (H7b)

**Graphite did not help.** C40 + graphite was hotter than C40 at peak every day (by 1.7, 1.8 and
3.8 °C; −2.4 ± 1.2 °C, CI −5.4 to +0.6), the opposite of H7b and of the model's negligible
difference. By H7b's own criterion (CI includes 0) it is falsified. The slab partly collapsed
and flowed on Day 2 after ≈ 105 min above 68 °C and broke apart by the end of Day 3 (Figure
4.11c). Lost contact with the module, rather than conductivity, is the likely reason it cooled
less. Whether graphite itself weakens the network is untested: the side-by-side oven hold of C40
and C40 + graphite has not been run ⚠️ [PENDING — C40 vs C40 + graphite oven test at 60 and
70 °C, §3.6.2].

### 4.9.4 Retention in service (H7d)

Over three days outdoors, with module peaks of 60–76 °C, wax alone lost nothing measurable (98 →
98 g), C40 lost **2.1 %** (96 → 94 g) and C40 + graphite **11 %** (100 → 89 g plus fragments)
(Figure 4.11). **C40 sits at the 2 % limit and cannot be separated from it on a 1 g scale; C40 +
graphite clearly fails H7d.** Because wax alone lost nothing, C40's loss is attributable to the
acid. In the oven C40 lost 1.47 % in 2 h at 60 °C, 3.51 % in 2 h at 70 °C and 16.1 % over 25
cycles; the field slab lost far less over far longer, but it was heated from one face, cooled
nightly and held against a board rather than on absorbent paper, so the figures are not directly
comparable. It is the first multi-day retention measurement for this composite in service.

![Figure 4.11](../Data%20Analysis/outputs/fig_photo_slabs.jpg)

**Figure 4.11.** Slabs after the campaign. (a) A cast slab, 14 × 7 cm, 1 cm thick. (b) The C40
slab on the scale at 94 g (96 g before), intact. (c) The C40 + graphite slab at 89 g (100 g
before), broken, above its board, which shows a graphite print where the slab sat and composite
pooled along the lower edge. Photographs taken by the authors.

### 4.9.5 What the field result can and cannot support

It supports: a 1 cm rice-bran-wax slab, with or without lauric acid, lowered the peak of an
insulated-back mini module by several degrees in Al Khobar's October sun on each of three days;
on the hottest day the acid held the C40 module ≈ 8 °C below the wax-only module for ≈ 1.5 h;
C40 kept its mass to ≈ 2 % over three days outdoors; graphite as dispersed here harmed both
cooling and stability. It does not support a statistically established effect, a latent-heat
margin over thermal mass on every day, or transfer of the absolute numbers to full-size
modules (§6).

---

## 4.10 Panel-scale thermal model: analysis

The model of §3.9.6 is assessed here against the field result, then analysed to show which
properties its prediction depends on. The analysis sweeps are post hoc and do not replace the
prediction.

### 4.10.1 Version 2 against the field

For the insulated-back design actually run, v2 predicted C40 **+1.9 °C** cooler than bare at
peak (2 cm), wax alone +0.8 °C, and graphite no detectable change. The field gave **+6.5 °C**
(C40) and **+6.7 °C** (wax) with 1 cm slabs, for which the model gives only +0.8 °C. **The model
got the sign right and the size wrong by a factor of three or more, and its predicted latent
margin of C40 over wax (≈ 1.1 °C) was not seen on average.** Three model features plausibly
explain the shortfall: its module heat capacity (9000 J/m²·K) and convection correlation are for
full-size modules, whereas a 1 W mini panel has little thermal mass of its own, so a slab of
comparable mass dominates; it ran on a climate 12–18 °C cooler than Al Khobar's; and its
properties are placeholders. The model predicted that composite and graphite slabs would melt
partly by day and re-solidify by night (peak liquid fraction 0.25, 0.00 every dawn); the evening
cooling arrest near 43 °C (§4.9.2) is consistent with that.

### 4.10.2 Version 1 and why a layer can heat a module

The first prediction (open rack, convection only, ΔH 95 J/g) gave **−5.3 °C**: the layer made
the module hotter (Figure 4.12). Its composite peaked at only **48.4 °C**, used **28.8 kJ** of
**171 kJ** latent capacity (liquid fraction 0.17) and re-solidified every night. The reason is
the back path. On an open rack, the 2 cm layer adds 0.100 m²K/W in series with a 0.125 m²K/W
convective film, cutting steady rear conductance by **44 %**, while its storage acts only near
the peak. Against insulation the rear is already resistive, so the slab adds little resistance
and its storage dominates (§3.9.6). **Mounting decides the sign,** which is why the field test
used insulated backs, and why an open-rack PCM unit made modules hotter in Soares et al. (2020).

![Figure 4.12](../Data%20Analysis/outputs/fig_model_timeseries.png)

**Figure 4.12.** Model v1 (open rack, pre-registered first) over three synthetic clear October
days. (a) Bare module, module with a 2 cm composite layer, and composite node, with the measured
melting band shaded. (b) Composite liquid fraction; night shaded.

**Numerical check.** Halving the timestep from 30 s to 1 s changes the peak ΔT by 0.001 °C. The
real approximation is lumping: the layer Biot number is 0.80, so the panel-side face would run
above the lumped temperature and melt somewhat more, making the lumped result mildly pessimistic
about melting.

### 4.10.3 Sensitivity to conductivity, latent heat and thickness (v1, post hoc)

On the open rack, conductivity dominates (Figure 4.13): peak ΔT rises from −9.7 °C at
*k* = 0.1 W/m·K to **break-even at *k* ≈ 0.8 W/m·K** and +1.7 °C at 6 W/m·K, never reaching 2 °C at
2 cm and 95 J/g. At *k* = 0.2 W/m·K every combination of latent heat (50–191 J/g) and thickness
(0.5–5 cm) warms the module; at *k* = 1.0 W/m·K the 2 °C target needs **ΔH ≥ 150 J/g at 3 cm or
191 J/g at 2 cm**, essentially neat lauric acid (Figure 4.14). On the insulated back (v2), by
contrast, *k* from 0.2 to 6 W/m·K moves peak ΔT only between +1.6 and +2.2 °C.

![Figure 4.13](../Data%20Analysis/outputs/fig_model_k.png)

**Figure 4.13.** Model v1 (open rack), post-hoc sensitivity to composite conductivity at 2 cm and
95 J/g: peak and daylight-mean ΔT (positive = cooling, left axis) and peak liquid fraction (right
axis). Dotted line: the pre-registered placeholder.

![Figure 4.14](../Data%20Analysis/outputs/fig_model_grid.png)

**Figure 4.14.** Model v1 (open rack), post-hoc sensitivity of peak ΔT to latent heat and layer
thickness at *k* = 0.2 W/m·K (left) and 1.0 W/m·K (right). Blue, cooling; red, warming.

### 4.10.4 Benchmark against a sharp-melting paraffin

With RT44-like properties (43–44 °C, 250 J/g, 800 kg/m³, 2 cm), the same open-rack model also
warms the module at *k* = 0.2 W/m·K (−3.75 °C) but cools it by **+9.9 °C** at *k* = 1.0 W/m·K,
melting fully, where the composite gives +0.4 °C. **The composite's 32 °C-wide melting band, not
its onset, is its main thermal handicap:** the latent heat arrives too slowly and too high. The
large RT44 reduction of Durez et al. (2023) is not reproduced at *k* = 0.2 W/m·K, pointing to
differences in climate and in how the back boundary and layer resistance are treated.

⚠️ [PENDING — re-run v2 with measured ΔH (DSC) and *k* (hot-wire), and on Al Khobar weather, as a
post-hoc check.]

---

## Chapter 4 — items to confirm before submission

| Item | Feeds | Status |
|---|---|---|
| Dish, sealed-control and 60/70 °C blank masses → workbook, then re-run and update §4.4.5 | §4.4.1, §4.4.5 | transcribe |
| SOAK arm (2 × C40, 634 min at 60 °C) | §4.4, §4.5, H4 | to run |
| BLANK-CYC masses | §4.5 Transfer % | enter |
| C40 casting batch; short cool legs after cycles 7, 18, 22 | §4.5.1 | confirm |
| Reverse-pour recast | §3.3.8, §6 | run, or move to §8 |
| Composition-series melting specimens | §4.2 | confirm whether run |
| GIKI: DSC / FTIR / SEM | §4.6–4.8, H3–H6 | awaiting |
| C40 vs C40 + graphite oven test (60, 70 °C) | §4.9.3, H7b | to run |
| Model re-run with measured ΔH and *k* | §4.10 | after GIKI |
| UN30 datasheet uniformity; balance make/model; uniform 24 h anneal; GIKI as-run details | Ch. 3 | record / confirm |
