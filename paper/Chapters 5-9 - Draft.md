# 5. Discussion

> **Status.** Where the argument turns on outstanding data (SOAK, DSC, FTIR, SEM), both
> outcomes are written out and marked ⚠️ [PENDING], so only a deletion is needed.

## 5.1 What the retention surface shows

**Across a 20 °C span the network goes from holding four times its own mass of liquid acid to
failing at the lowest loading tested** (X(50) ≥ 80, X(60) = 43, X(70) < 20 wt %; §4.4.3). H1 is
supported and H2 not falsified. The predicted 55–68 °C service limit is consistent with the
data but only loosely tested: the data contain the predicted window and do not contradict it,
but do not place the limit to better than 10 °C.

The 50 °C result stands on its own. With the acid fully molten, twenty parts of wax held eighty
parts of liquid and lost 1.3 % in two hours. Rice bran wax structures triglyceride oils from
0.5 wt % (Wijarnprecha et al., 2018); the present data show the same network forming in a
**free fatty acid** melt, which, to our knowledge, had not been shown. The question of §2.3,
whether a wax network can hold a fatty-acid melt at all, is answered yes at 50 °C.

## 5.2 Reconciling the thermodynamic and mechanical measurements

The composite's liquidus is near **75 °C** (§4.2), yet from 50 wt % up it fails by 60 °C, while
much of its wax should still be solid. **The gap is a finding, not a discrepancy**: the melting
curve detects whether *any* solid remains, the leak test whether the solid forms a
**continuous** network. As crystals dissolve, the remainder can fall below the fraction needed
to stay connected across the specimen long before the last crystal disappears, and liquid then
drains past solid that is still present. Retention should therefore fail at a **critical solid
fraction**, not at the liquidus.

The composition series fits this qualitatively. More acid lowers the limit in two ways at once:
less wax to begin with, and more solvent to dissolve it. At 70 °C the 50–60 wt % specimens stayed
intact and leaked 7–10 %, while 70–80 wt % collapsed; whether this is a sharp percolation
threshold or a steep ramp is unresolved (§4.4.4).

**The ideal-mixing model underestimates how much wax stays solid.** It predicted a liquidus of
≈ 67 °C at 50 wt %, yet the 50 and 60 wt % specimens stayed intact at 70 °C, in line with the
≈ 75 °C water-bath liquidus. For chemically similar fatty acids, the same Schröder approach
predicts measured eutectics closely (Zhou et al., 2026); RBW is mostly long-chain esters, unlike
the acid dissolving it, so a departure from ideality is expected. **A critical solid fraction
would be more transferable than a temperature:** with the wax solubility curve from the DSC
series (§4.6 ⚠️ [PENDING]), the solid fraction in each cell of Table 4.5 could be computed, and
a single failure value would predict X(T) for any loading.

## 5.3 Time dependence: the two-hour limit is not the whole answer

After 25 cycles C40 lost **16.1 %**, eleven times its two-hour loss (§4.5). Whatever the cause,
**retention in this network is strongly time-dependent**, and every X(T) here is a two-hour
figure. This sets it apart from other composite classes: hexadecane / LDPE composites lost
0.10–3.64 % in the first hour and then levelled off within about 14 h (Khalaf Alshammari et al.,
2024), and paraffin / expanded-graphite composites held below 4 wt % over ten 1 h holds at 60 °C
(An et al., 2022). A 16 % loss after ten hours is of the order Wadee et al. (2025) report for
coated PCM granules only after **500 h** at 50 °C (11.4–14.1 %). The mechanism of §5.2 explains
why: a porous carrier's pores do not change with time, while a dissolving network can keep
coarsening and losing connectivity.

⚠️ [PENDING — SOAK.] Keep the paragraph that matches the result:

- *If SOAK ≈ CYC:* the loss is caused by sustained time at 60 °C; the network survives freezing
  and remelting, but not hours at temperature.
- *If SOAK < CYC by more than 1 pp:* each freeze–melt cycle disturbs the network beyond time
  alone, plausibly by recrystallisation into fewer, larger crystals. SEM on the cycled specimen
  (§4.8) is the direct test.

The "hollow at top" on all three cycled specimens points to **gravity-driven drainage**, the
small-scale version of the settling failure the untested tilted assay was designed to detect
(§3.5.2).

## 5.4 Is the acid–wax system a physical mixture? (H5)

⚠️ [PENDING — FTIR.] The thermal data already favour H5: the liquidus lies *above* the
ideal-mixing prediction, so the wax is less soluble than ideal, the opposite of what strong
acid–ester hydrogen bonding would produce. (The earlier contrary indication, γ ≈ 0.05, came from
the withdrawn run, §6.)

- *If no carbonyl shift is seen:* H5 survives; retention is governed by network mechanics alone
  (§5.2).
- *If a reproducible shift is seen, especially one growing with acid fraction:* H5 is falsified,
  and the interaction must be reconciled with the low solubility, for example as one too weak to
  raise solubility but visible spectroscopically.

## 5.5 Implications for deployment

The application constraint is a rear temperature of **55–60 °C** on clear days in northern
Pakistan, and well above that behind roof-integrated modules (§1; the field bare panel reached
64–76 °C). Against it:

1. **At 60 °C only loadings ≤ 40 wt % meet the criterion, and then only for two hours** (§4.4,
   §4.5).
2. **Containment costs more than half the storage.** At 40 wt %, the pre-registered rule gives
   ≈ 76 J/g against 191 J/g for neat acid ⚠️ [DSC value].
3. **On a roof-integrated module, mass matters more than conductivity or latent heat.** In the
   field, 1 cm slabs cooled the peak by ≈ 6.5 °C with or without the acid (§4.9), far more than
   model v2 predicted (+0.8 °C for 1 cm), and the model shows why the mounting matters: on an
   open rack the same layer insulates and warms the module (v1, −5.3 °C; Soares et al., 2020,
   measured the same effect), while against insulation storage dominates and conductivity barely
   matters (§4.10). Graphite at ≈ 3.8 wt % made the slab warmer and unstable rather than better.
   Where conductivity does matter, on an open rack, break-even needs *k* ≈ 0.8 W/m·K, and
   10–15 wt % expanded graphite in a fatty-acid eutectic raised *k* only 2.4–2.6-fold (Wang et
   al., 2022), to ≈ 0.5 W/m·K from the 0.2 W/m·K placeholder. Pressed expanded graphite reaches
   ≈ 16 W/m·K (Wang et al., 2024), but then holds the PCM by capillarity, making it a porous-carrier
   composite. In the same model a sharp-melting paraffin cools ≈ 25 times more than the composite
   at *k* = 1 W/m·K: the **32 °C-wide melting band**, more than the onset, limits the composite
   thermally.
4. **At 50 °C the material works well.** A shaded or ventilated installation, a milder climate
   or a non-PV thermal buffer whose peak stays near 50 °C is within the measured envelope.

**What the field test adds.** Most of the measured cooling is thermal mass, which the cheaper,
non-leaking wax delivers alone (6.7 °C against 6.5 °C for C40). The acid's latent heat showed
clearly on the hottest day, when the C40 module held near 55 °C for ≈ 1.5 h while the
wax-only module rose to 62–64 °C, and as slow evening cooling near 43 °C, but not on the two
milder days; its cost was ≈ 2 % of slab mass in three days. Panel bias was not
corrected, but after sunset the RBW and C40 panels converged to within ≈ 0.5 °C of bare, small
against the ≈ 6.5 °C effect (§6). **A wax slab is a credible passive peak-shaver for
roof-integrated modules; the acid is worth adding only if its latent margin can be shown across
many days with the slab contained.**

What can be claimed: an agricultural by-product forms a network that holds molten lauric acid at
high loading at 50 °C, its retention limit across the PV range is measured with its time
dependence attached, and on an insulated-back module a 1 cm slab lowered the peak by several
degrees on each of three days. What cannot: that the composite as formulated is a deployable,
long-life PV coolant. That would need a loading at or below about 40 wt %, a container that
tolerates slow drainage, and multi-week evidence on full-size modules.

## 5.6 Comparison with porous-carrier stabilisation

The two mechanisms of §2.2 should differ in the **shape** of their retention curves. Capillary
retention in a fixed pore geometry should be nearly flat with temperature above the melt and
level off with time. A dissolving network should lose retention progressively with temperature,
keep losing it with time, and end in collapse. **The present data show all three features of
the gelled case:** X(T) falls steeply with temperature, loss grows with time, and the highest
loadings collapse at 70 °C. By contrast, paraffin in an expanded-graphite / copolymer matrix
stayed below 4 wt % over ten 1 h holds at 60 °C (An et al., 2022), and pressed expanded graphite
held 80.8 wt % paraffin without leakage (Wang et al., 2024). No porous-carrier arm was run under
the same protocol, so the contrast is drawn against literature; measuring it side by side is the
most informative next experiment (§8).

---

# 6. Limitations

- **Material grade is supplier-stated.** The wax melted ≈ 5 °C below the literature range
  (§4.1), and gelation depends on ester composition; results describe batch PR 1798 until DSC
  resolves the grade.
- **A systematic error was found and corrected.** An early, incompletely mixed composite run
  gave internally consistent data, including a 10 min plateau at 48 °C, and survived four
  confound checks (melt transparency, blend provenance, a 24 h anneal, a solid network before
  heating). A service limit of ≈ 48 °C and a favourable interaction (γ ≈ 0.05) were inferred
  from it. Only a changed preparation exposed the fault; the properly mixed composite melted to
  75 °C, and the 48 °C result and everything derived from it were withdrawn. It is the reason
  the composition series used recorded masses and a fixed preparation (§3.2).
- **Instrument resolution.** A 1 °C thermometer for melting points; a 0.01 g balance on 4–5 g
  specimens (LOQ 0.64 %), so 20–60 wt % cannot be ranked at 50 °C (§4.4.2). Visual "fully
  melted" endpoints depend on heating rate (§4.1) and are not used.
- **Preliminary composite runs.** Masses were not recorded; the 75 °C liquidus rests on one
  properly mixed run (§4.2).
- **Specimen geometry.** 4.0–5.4 g pentagonal prisms, not the nominal 7 g; leakage percentages
  are specific to this surface-to-volume ratio.
- **Design resolution.** X(T) is located at one temperature only, the 60–70 wt % collapse
  boundary at 70 °C is unresolved, and the X(60) interval reflects n = 3 scatter and assumes
  linearity between compositions.
- **Hold time.** All X(T) values are two-hour values; leakage was measured at only 2 h and
  ≈ 10.6 h, so the shape of the leakage–time curve is unknown ⚠️ [update once SOAK reports].
- **Number of cycles.** Twenty-five cycles (≈ 10.6 h hot) is early-life behaviour against
  500–700-cycle studies and 500 h exposures (Wadee et al., 2025; Du et al., 2021, as cited in
  Zhou et al., 2026).
- **Supporting masses and second channel.** Dish, sealed-control and late-run blank masses are
  not yet analysed ⚠️ [TRANSCRIBE]; papers were not photographed, so leakage rests on gravimetry
  alone.
- **Handling after the oven.** Papers came straight from the box (corrected by blanks), no
  desiccator was used, and specimen temperature was not measured before weighing; a specimen
  not fully cooled reads falsely low, so a small error of this kind cannot be excluded.
- **Pour order.** Compositions were poured 20 → 80 wt %, so later pours spent up to ~15 min longer
  molten after a common > 1 h soak. The effect is argued to be negligible but is aliased with
  the composition trend ⚠️ [reverse-order recast: run / not run].
- **Identity of the escaped liquid.** Treating it as lauric acid is an assumption; at 60–70 °C it
  carries dissolved wax.
- **Scale and orientation.** Specimens were small and horizontal; gravitational separation in a
  tilted panel was not tested (§3.5.2). DSC supercooling does not transfer to panel scale (§3.7).
- **Field design.** Three days with one module per treatment, so every 95 % CI on the daily peak
  difference includes zero, and no crossover correction was possible. Whole stations were
  rotated, so panel and sensor bias stay tied to treatment, and the bare calibration run's log
  was not available. After sunset the slab stations read at most **0.14 °C (RBW), 0.54 °C (C40)
  and 1.26 °C (C40 + graphite)** warmer than bare. Because heat still leaving the slabs adds to
  that gap, it bounds a bias that would make a slab panel read too warm (correcting for it would
  only increase the measured cooling), but it cannot exclude a bias of the other sign or one
  that appears only in sunlight.
- **Field measurements.** Sensors were calibrated at the ice point only, with span differences at
  panel temperature uncorrected (§3.8). They sat between module and slab, so contact between
  sensor, module and a softening slab may change as the slab melts and settles (§4.9.2); earlier
  records placed them below the slab edge and were corrected (§3.6.1). Weather is
  model data. The slabs had no container and were held between module and board, so their mass
  change combines leakage, evaporation and handling loss; mass was read on a 1 g scale, so C40's
  2.1 % cannot be separated from the 2 % criterion. Slabs were 1 cm, not the predicted 2 cm, and
  mini panels are not full-size modules. The findings window, matched-sunlight comparison and
  evening cooling rates were added after the data were seen. H7c was not tested.
- **External instruments.** DSC, FTIR and SEM were run by facility staff ⚠️ [PENDING results].
- **Thermal model.** ΔH, density, heat capacity and conductivity are placeholders; the model is
  lumped (layer Biot number 0.8), runs on a synthetic climate, and uses an order-of-magnitude
  module heat capacity. It is a pre-registered statement of expected behaviour, not a
  quantitative forecast, and it underestimated the field cooling by a factor of three or more.
- **Sample sizes.** Lauric acid melting n = 2; rice bran wax n = 3 (one superseded); properly
  mixed composite n = 1; retention matrix n = 3 per cell (63); cycling n = 3 cycled and n = 2
  soaked ⚠️; field 3 days, one module per treatment.

---

# 7. Conclusions

1. **Rice bran wax forms a network that holds molten lauric acid:** at 50 °C every composite
   from 20 to 80 wt % lost ≤ 1.3 % in two hours (X(50) ≥ 80 wt %), to our knowledge the first
   such measurement for a natural-wax network holding a free fatty acid.
2. **The retention limit falls steeply across the PV range:** X(60) = 43 wt % (95 % CI 41–46) and
   X(70) < 20 wt %, with 70–80 wt % collapsing at 70 °C; leakage rose with temperature and
   loading (p < 10⁻⁵). H1 is supported and H2 not falsified.
3. **Retention fails mechanically, well below the ≈ 75 °C liquidus,** consistent with loss of
   network connectivity rather than complete dissolution of the wax.
4. **There is no useful eutectic:** the 43–44 °C onset matches pure lauric acid; the wax
   contributes containment only.
5. **Retention is strongly time-dependent:** over 25 cycles (≈ 10.6 h at 60 °C) C40 lost
   16.1 ± 0.5 %, eleven times its two-hour loss. ⚠️ [PENDING — SOAK: cycling or time.]
6. ⚠️ [PENDING — DSC: H3, latent heat against acid fraction; the wax melting point.]
   ⚠️ [PENDING — FTIR: H5.] ⚠️ [PENDING — SEM: H6.]
7. **Mounting decides whether a PCM layer cools or heats a module:** the pre-registered model
   predicted warming on an open rack (−5.3 °C) and cooling against insulation (+1.9 °C), and the
   composite's 32 °C-wide melting band is its main thermal handicap.
8. **In the field, a 1 cm slab lowered the peak of an insulated-back mini module by several
   degrees, mostly through thermal mass:** C40 by 6.5 ± 5.2 °C and wax alone by 6.7 ± 3.7 °C over
   three days in Al Khobar, above the 2 °C threshold on the mean but not statistically
   established (95 % CI includes zero). The acid's latent heat held C40 ≈ 8 °C below wax alone
   for ≈ 1.5 h on the hottest day but gave no margin on the two milder days (H7a, as
   pre-registered, not supported), graphite made the slab warmer and unstable (H7b falsified), and over
   three days C40 lost 2.1 %, wax 0 % and C40 + graphite 11 % (H7d: C40 at the limit, graphite
   fails).

Together, the results put a quantified ceiling on a passive-cooling material made from an
agricultural residue: it works at 50 °C, is marginal at 60 °C and fails at 70 °C, and its
two-hour figures overstate retention under sustained heat. Behind a roof-integrated module, even
the wax alone shaved several degrees off the daily peak.

---

# 8. Future work

- **A hold-time series (highest priority).** Fresh C40 at 60 °C withdrawn at 0.5, 1, 2, 4 and
  10 h, tying the matrix and soak results into one leakage–time curve; then at 50 °C and across
  loadings, so X(T) carries its hold time.
- **Locate the limit.** Test at 55 and 65 °C and at 45 and 65 wt %, plus a composition between 60
  and 70 wt % at 70 °C to tell a step from a ramp.
- **Critical solid fraction.** Build the phase diagram from the DSC series and test whether
  failure occurs at one solid fraction (§5.2).
- **A porous-carrier arm** (lauric acid in expanded perlite or diatomite) under the identical
  protocol, to measure the curve-shape difference of §5.6.
- **C40 against C40 + graphite in the oven** at 60 and 70 °C, and conductivity by transient
  hot-wire, to tell whether graphite weakens the network; a hybrid (acid in a graphite or porous
  carrier, wax as a secondary gelator) may suit open-rack modules.
- **The tilted settling assay** of §3.5.2.
- **A longer field campaign:** several modules per treatment, a bare calibration day, sensors at
  the slab centre and on its outer face (H7c), contained slabs, an on-site pyranometer, full-size
  modules, and the C40 − wax margin as the primary outcome.

---

# 9. Acknowledgements

⚠️ [FILL] We thank `[supervisor name]` for supervision and `[chemistry teacher name]` for
supervising all heated laboratory work (§3.10); the Chemistry Laboratory of Cadet College
Hasanabdal for bench and oven time; `[GIKI department / facility and staff names]` for DSC, FTIR
and SEM access; and `[anyone else who gave lab time, materials, photographs or review]`.
Materials were obtained from Bioshop PK (lauric acid) and Aogubio Co., Ltd. (rice bran wax,
batch PR 1798).

---

# Appendix A. Panel model equations

The module (glass, cells, backsheet) is one node at *T*<sub>m</sub> with areal heat capacity
*C*″; the composite is a second node with specific enthalpy *H*. For module area *A*,

$$
C'' A\,\frac{\mathrm{d}T_m}{\mathrm{d}t} = (\tau\alpha)\,S(t)\,A - q_f - q_b ,
$$

$$
q_f = h_w A\,(T_m - T_a) + \varepsilon_f \sigma A\left[F_s\left(T_m^4 - T_\text{sky}^4\right) + F_g\left(T_m^4 - T_a^4\right)\right],
\qquad h_w = 5.8 + 3.7\,V ,
$$

with $F_s = (1+\cos\beta)/2$, $F_g = (1-\cos\beta)/2$ for tilt β,
$T_\text{sky} = 0.0552\,T_a^{1.5}$ (Swinbank, 1963), and radiative temperatures in kelvin. The
back-path heat flow is

$$
q_b^\text{bare} = B(T_m, \varepsilon_b), \qquad
q_b^\text{PCM} = \frac{kA}{L}\,(T_m - T_c), \qquad
m\,\frac{\mathrm{d}H}{\mathrm{d}t} = q_b^\text{PCM} - B(T_c, \varepsilon_c),
$$

with composite mass *m* = ρ*AL* and back boundary

$$
B_\text{open}(T, \varepsilon) = h_b A\,(T - T_a) + \varepsilon \sigma A\left(T^4 - T_a^4\right),
\qquad
B_\text{insulated}(T) = U A\,(T - T_a), \quad
U = \left[\frac{L_i}{k_i} + \frac{1}{h_b + 4\varepsilon_i \sigma T_0^3}\right]^{-1},
$$

where $T_0$ = 300 K and $\varepsilon_i$ = 0.90, giving *U* ≈ 1.5 W/m²·K for 20 mm of expanded
polystyrene. Temperature and liquid fraction follow from *H* (zero at the solidus) with the
latent heat released linearly across [*T*<sub>s</sub>, *T*<sub>l</sub>]:

$$
T_c =
\begin{cases}
T_s + H/c_p, & H \le 0,\\[2pt]
T_s + \dfrac{H}{c_p + \Delta H/(T_l - T_s)}, & 0 < H < H_l,\\[6pt]
T_l + (H - H_l)/c_p, & H \ge H_l,
\end{cases}
\qquad H_l = c_p (T_l - T_s) + \Delta H,
\qquad f = \frac{T_c - T_s}{T_l - T_s}\ \text{(clipped to [0, 1])}.
$$

The synthetic climate is $T_a(t) = 22 + 7\sin\!\left[2\pi(t_h - 9)/24\right]$ °C and
$S(t) = 800\,\sin\!\left[\pi(t_h - 6.5)/11.5\right]$ W/m² between 06:30 and 18:00, zero
otherwise; efficiency is $\eta = \eta_\text{ref}\left[1 - \beta\,(T_m - 25)\right]$. Parameters
are in Table 3.1.

# Appendix B. Leak-test handling and decision rules

**Paper conditioning (protocol).** All papers dried together at 105 °C for 1 h, cooled in a
desiccator and stored over silica gel; two blanks per run (three if conditioning is omitted),
which must agree to ~0.01 g. *As run: papers used from the box, two blanks per run.*

**Weighing.** Balance warmed 30 min, levelled, zeroed, re-zeroed every ten weighings with drift
logged; gloves and forceps throughout. Each mass is the mean of three separate placements
(uncertainty ≈ ±0.006 g); a spread above 0.02 g stops weighing. After the hold, specimens cool
30 min in a desiccator and are weighed only once a co-located dummy with a sensor reads ambient,
within 60 s of opening. *As run: 30 min on the bench, temperature not measured.*

**Oven.** Preheated ≥ 45 min; all ten positions loaded in under 30 s in the pre-generated random
order; the loaded shelf photographed as the position map; the door not reopened for two hours.

**Precision.** LOD one balance increment (mean 0.21 % of m₀), LOQ three (mean 0.64 %); leakage
reported to 0.1 %. An earlier fixed 0.4 % "below detection" threshold, derived for 5–7 g
specimens, was replaced by these per-specimen limits when the 50 °C block showed the specimens
were lighter than nominal. The |Leakage − Transfer| > 0.4 % flag is about two increments wide on
the specimens cast; on disagreement the checks are, in order: large closure (evaporation; consult
the sealed control), liquid off the paper, blank correction applied, anything weighed warm.

**Rules fixed and dated before the first run.**

| Rule | Decision |
|---|---|
| Collapse | Specimen not separable from its paper intact → record "collapsed", leave Leakage blank, record a definitive **fail** at that temperature. Never reported as a number. |
| Oven excursion | Displayed temperature outside setpoint ± 1 °C at any checkpoint, or any alarm / unplanned door opening → **void the whole run** (all seven specimens). No salvage of individual specimens. |
| Handling loss | Specimen dropped, chipped, or in contact with anything but its own paper → void that specimen, record why. |
| Defective specimen | Visible void, crack or skin defect → excluded before any run. |
| Blank drift | \|Δm_blank\| > 0.03 g → conditioning failed; void that run's cross-checks, keep primary leakage numbers, flag them as uncorroborated. |
| Replicates | All three reported. No outlier dropped without a documented physical cause from the rules above. |

**Stopping point.** The 50 °C series was completed and examined before committing material to 60
and 70 °C.

# Appendix C. Samples requested for external analysis

**DSC.** Core set: raw RBW (batch PR 1798), pure lauric acid and composites at 30, 50 and 70 wt %;
extended to 20, 40, 60 and 80 wt % and cycled C40 if instrument time allows. Pans loaded molten,
so that a 5–10 mg sample represents a composite that is heterogeneous when solid. Programme
20 → 90 → 20 → 90 °C at 1–2 °C/min under N₂ (slow, because the features lie a few degrees
apart). Recorded per sample: mass, pan type, atmosphere, onset, peak and end temperatures and
enthalpy of every transition; supercooling = melting onset − crystallisation onset, compared at
matched mass and cooling rate.

**FTIR (ATR).** Pure lauric acid, raw RBW, composites at 30, 50 and 70 wt % at minimum (all seven
if time allows) and cycled C40 if submitted, as a composition series. Bands: acid C=O near
1700 cm⁻¹, wax-ester C=O near 1735 cm⁻¹, O–H 2500–3300 cm⁻¹. Raw spectra exported.

**SEM.** Sputter-coated fresh fracture surfaces of raw RBW, one 20–30 wt % and one 70–80 wt %
composite, and uncycled and cycled C40 if submitted. One spare C40 specimen is kept unheated as
the reference, and the cycled piece is taken only after its final weighing. Network density and
needle length measured in ImageJ (n ≥ 30 features).

---

# References

Author–year list. Every DOI was resolved against Crossref or DataCite on 17 October 2026;
works without a DOI were checked against the publisher, repository or report record.

- Aelenei, L., Pereira, R., Gonçalves, H. & Athienitis, A. (2014). Thermal performance of a hybrid BIPV-PCM: modeling, design and experimental investigation. *Energy Procedia* 48, 474–483. https://doi.org/10.1016/j.egypro.2014.02.056
- Ali, H. M., Mahmood, M., Bashir, M. A., Ali, M. & Siddiqui, A. M. (2016). Outdoor testing of photovoltaic modules during summer in Taxila, Pakistan. *Thermal Science* 20(1), 165–173. https://doi.org/10.2298/TSCI131216025A
- Amber, K. P., Akram, W., Bashir, M. A., Khan, M. S. & Kousar, A. (2021). Experimental performance analysis of two different passive cooling techniques for solar photovoltaic installations. *Journal of Thermal Analysis and Calorimetry* 143(3), 2355–2366. https://doi.org/10.1007/s10973-020-09883-6
- An, Z., Chen, H., Du, X., Shi, T. & Zhang, D. (2022). Preparation and performance analysis of form-stable composite phase change materials with different EG particle sizes and mass fractions for thermal energy storage. *ACS Omega* 7(38), 34436–34448. https://doi.org/10.1021/acsomega.2c04101
- Barrera, C. J. R., Umadhay, M. D., Canson, J. C. & Larroder, A. C. (2020). Use of 1:7 rice bran wax to rice bran oil mixture as phase change material in increasing the efficiency of photovoltaic cells. *Publiscience* 3(1), 101–104. Philippine Science High School – Western Visayas Campus (no DOI).
- Dassanayake, L. S. K., Kodali, D. R., Ueno, S. & Sato, K. (2009). Physical properties of rice bran wax in bulk and organogels. *Journal of the American Oil Chemists' Society* 86(12), 1163–1173. https://doi.org/10.1007/s11746-009-1464-6
- Desgrosseilliers, L., Whitman, C. A., Groulx, D. & White, M. A. (2013). Dodecanoic acid as a promising phase-change material for thermal energy storage. *Applied Thermal Engineering* 53(1), 37–41. https://doi.org/10.1016/j.applthermaleng.2012.12.031
- Du, W., Fei, H., He, Q., Wang, L., Pan, Y. & Liu, J. (2021). Preparation and properties of capric acid–stearic acid-based ternary phase change materials. *RSC Advances* 11(40), 24938–24948. https://doi.org/10.1039/D1RA03925C (cited as reported by Zhou et al., 2026)
- Durez, A., Ali, M., Waqas, A., Nazir, K. & Kumarasamy, S. (2023). Modelling and optimization of phase change materials (PCM)-based passive cooling of solar PV panels in multi climate conditions. *Frontiers in Energy Research* 11, 1121138. https://doi.org/10.3389/fenrg.2023.1121138
- El Kassar, R., Al Takash, A., Faraj, J., Khaled, M. & Ramadan, H. S. (2025). Phase change materials for enhanced photovoltaic panels performance: a comprehensive review and critical analysis. *Energy and Built Environment* 6(4), 655–675. https://doi.org/10.1016/j.enbenv.2024.02.004
- Fan, Z., Zhao, Y., Liu, X., Shi, Y. & Jiang, D. (2022). Thermal properties and reliabilities of lauric acid-based binary eutectic fatty acid as a phase change material for building energy conservation. *ACS Omega* 7(18), 16097–16108. https://doi.org/10.1021/acsomega.2c01420
- FAO (2025). *FAOSTAT: Crops and livestock products* (rice, paddy, 2023). Food and Agriculture Organization of the United Nations. https://www.fao.org/faostat/en/#data/QCL (accessed October 2026)
- Fraunhofer ISE (n.d.). *Building-integrated photovoltaics (BIPV)*. Fraunhofer Institute for Solar Energy Systems ISE. https://www.ise.fraunhofer.de/en/business-areas/solar-power-plants-and-integrated-photovoltaics/integrated-photovoltaics/building-integrated-photovoltaics-bipv.html (accessed 17 October 2026)
- Hasan, A., McCormack, S. J., Huang, M. J. & Norton, B. (2010). Evaluation of phase change materials for thermal regulation enhancement of building integrated photovoltaics. *Solar Energy* 84(9), 1601–1612. https://doi.org/10.1016/j.solener.2010.06.010
- Huang, M. J., Eames, P. C. & Norton, B. (2004). Thermal regulation of building-integrated photovoltaics using phase change materials. *International Journal of Heat and Mass Transfer* 47(12–13), 2715–2733. https://doi.org/10.1016/j.ijheatmasstransfer.2003.11.015
- Huang, M. J., Eames, P. C. & Norton, B. (2006). Phase change materials for limiting temperature rise in building integrated photovoltaics. *Solar Energy* 80(9), 1121–1130. https://doi.org/10.1016/j.solener.2005.10.006
- Khalaf Alshammari, N., Trigui, A. & Hassani, R. (2024). Thermal and mechanical performance assessment of composite (CPCM) for energy storage. *Heliyon* 10(17), e37212. https://doi.org/10.1016/j.heliyon.2024.e37212
- King, D. L., Boyson, W. E. & Kratochvil, J. A. (2004). *Photovoltaic Array Performance Model*. Report SAND2004-3535, Sandia National Laboratories, Albuquerque, NM. https://www.osti.gov/biblio/919131
- Lide, D. R. (ed.) (2009). *CRC Handbook of Chemistry and Physics*, 90th edn. CRC Press, Boca Raton, FL.
- Rashid, M., Yousif, M., Rashid, Z., Muhammad, A., Altaf, M. & Mustafa, A. (2023). Effect of dust accumulation on the performance of photovoltaic modules for different climate regions. *Heliyon* 9(12), e23069. https://doi.org/10.1016/j.heliyon.2023.e23069
- REN21 (2025). *Renewables 2025 Global Status Report Collection — Snapshot: Pakistan*. REN21 Secretariat, Paris. https://www.ren21.net/gsr-2025/snapshots/pk/ (accessed 17 October 2026)
- Sarı, A. (2005). Eutectic mixtures of some fatty acids for low temperature solar heating applications: thermal properties and thermal reliability. *Applied Thermal Engineering* 25(14–15), 2100–2107. https://doi.org/10.1016/j.applthermaleng.2005.01.010
- Sharaf, M., Yousef, M. S. & Huzayyin, A. S. (2022). Review of cooling techniques used to enhance the efficiency of photovoltaic power systems. *Environmental Science and Pollution Research* 29(18), 26131–26159. https://doi.org/10.1007/s11356-022-18719-9
- Sharma, A., Tyagi, V. V., Chen, C. R. & Buddhi, D. (2009). Review on thermal energy storage with phase change materials and applications. *Renewable and Sustainable Energy Reviews* 13(2), 318–345. https://doi.org/10.1016/j.rser.2007.10.005
- Soares, N., Costa, J. J., Gaspar, A. R., Matias, T., Simões, P. N. & Durães, L. (2020). Can movable PCM-filled TES units be used to improve the performance of PV panels? Overview and experimental case-study. *Energy and Buildings* 210, 109743. https://doi.org/10.1016/j.enbuild.2019.109743
- Stropnik, R. & Stritih, U. (2016). Increasing the efficiency of PV panel with the use of PCM. *Renewable Energy* 97, 671–679. https://doi.org/10.1016/j.renene.2016.06.011
- Sun, M., Sun, F., Di, H., Wu, C., Sheng, H., Lin, L. & Wang, Q. (2024). High value utilization of waste peanut shell: prepared novel shape stable composite phase change materials with high thermal conductivity. *Materials Today Sustainability* 26, 100707. https://doi.org/10.1016/j.mtsust.2024.100707
- Swinbank, W. C. (1963). Long-wave radiation from clear skies. *Quarterly Journal of the Royal Meteorological Society* 89(381), 339–348. https://doi.org/10.1002/qj.49708938105
- Wadee, A., Walker, P., McCullen, N. & Ferrandiz-Mas, V. (2025). The effect of thermal cycling on the thermal and chemical stability of paraffin phase change materials (PCMs) composites. *Materials and Structures* 58(1), 25. https://doi.org/10.1617/s11527-024-02556-y
- Wang, J.-X., Mao, Y. & Miljkovic, N. (2024). Nano-enhanced graphite/phase change material/graphene composite for sustainable and efficient passive thermal management. *Advanced Science* 11(38), 2402190. https://doi.org/10.1002/advs.202402190
- Wang, Z., Huang, G., Jia, Z., Gao, Q., Li, Y. & Gu, Z. (2022). Eutectic fatty acids phase change materials improved with expanded graphite. *Materials* 15(19), 6856. https://doi.org/10.3390/ma15196856
- Wijarnprecha, K., Aryusuk, K., Santiwattana, P., Sonwai, S. & Rousseau, D. (2018). Structure and rheology of oleogels made from rice bran wax and rice bran oil. *Food Research International* 112, 199–208. https://doi.org/10.1016/j.foodres.2018.06.005
- Yadav, D., Yadav, S. K., Varma, V., Khatoon, S., Singh, J., Singh, R. B., Hasnain, S. M. M., Paramasivam, P. & Tufa, M. A. (2025). Experimental analysis of elevated temperature and soiling loss on the rooftop PV modules performance under composite climatic conditions. *Scientific Reports* 15, 42035. https://doi.org/10.1038/s41598-025-25846-z
- Zalba, B., Marín, J. M., Cabeza, L. F. & Mehling, H. (2003). Review on thermal energy storage with phase change: materials, heat transfer analysis and applications. *Applied Thermal Engineering* 23(3), 251–283. https://doi.org/10.1016/S1359-4311(02)00192-8
- Zhou, D., Zhou, F., Yuan, J., Liu, Z. & Liu, Y. (2026). Phase diagrams and thermal properties of fatty acid ternary eutectic mixtures for latent heat thermal energy storage. *Materials* 19(2), 356. https://doi.org/10.3390/ma19020356
- Zhou, M., Li, B., Wu, A., Hu, Z., Zhou, L., Hu, H. & Fu, D. (2025). Preparation of a two-phase gel system based on gelatin hydrogel and beeswax/rice bran wax oleogel and eutectic phase behavior of beeswax and rice bran wax in soybean oil. *LWT* 215, 117306. https://doi.org/10.1016/j.lwt.2024.117306
- Zippenfenig, P. (2023). *Open-Meteo.com Weather API* [computer software]. Zenodo. https://doi.org/10.5281/zenodo.7970649
