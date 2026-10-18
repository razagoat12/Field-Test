# Temperature-Dependent Retention of Molten Lauric Acid in a Rice Bran Wax Matrix for Photovoltaic Thermal Management

Ahmad Hassan Raza (70114), Student at Cadet College Hasanabdal, Distt Attock, Punjab, Pakistan.
Ayaan Kaazmi (70091), Student at Cadet College Hasanabdal, Distt Attock, Punjab, Pakistan.

Category: Energy — Sustainable Materials and Design (ENSM)

> **Draft status (17 October 2026).** Retention matrix, cycled arm and field campaign are
> complete. DSC, FTIR, SEM, the continuous-soak (SOAK) arm and a side-by-side oven test of C40
> against C40 + graphite are pending and marked ⚠️. Protocol detail is in Appendices A–C
> (end of Chapters 5–9). Container-compatibility (coupon) testing is out of scope.

---

## Abstract

Photovoltaic (PV) modules lose about 0.43 % of their power per °C, and roof-integrated modules,
with no rear ventilation, run hottest. A phase-change material (PCM) behind the module can cap
the peak passively, but once molten it leaks. We measured how much molten lauric acid (melting
point 43.8 °C) a network of rice bran wax, a rice-milling by-product, retains, and up to what
temperature. Seven composites of 20–80 wt % lauric acid, cast under one thermal history, were
held for two hours at 50, 60 and 70 °C (n = 3) against a pre-registered ≤ 2 wt % loss
criterion. Every composition passed at 50 °C. At 60 °C the retention limit was 43 wt % (95 % CI
41–46); at 70 °C none passed and the 70–80 wt % specimens collapsed. Melting onset matched pure
lauric acid, so no useful eutectic formed, and retention failed well below the ≈ 75 °C
liquidus. After 25 melt–freeze cycles at 60 °C, the 40 wt % composite (C40) lost 16.1 %, eleven
times its two-hour loss. Outdoors in Al Khobar over three days, 1 cm slabs behind
insulated-back mini panels lowered the daily peak rear temperature by 6.5 °C (C40) and 6.7 °C
(wax alone) on average, above the pre-registered 2 °C threshold, although with three days every
95 % confidence interval included zero. C40 lost 2.1 % of its mass outdoors. The wax holds
molten acid well at 50 °C, but in the PV operating range retention depends strongly on
temperature and time.

⚠️ [PENDING — SOAK and DSC: add one sentence each when results arrive, keeping ≤ 250 words.]

**Keywords:** phase change material, shape stabilisation, rice bran wax, lauric acid,
oleogel, leakage, building-integrated photovoltaics, waste valorisation

---

# 1. Introduction

A photovoltaic module turns most of the sunlight it absorbs into heat, and its output falls
as it warms. Crystalline-silicon modules are rated at about **−0.43 % per °C** of maximum
power above 25 °C; on a North Indian rooftop, cell temperatures peaked at **64.0 °C** and
temperature alone cost **9.6 %** of output (Yadav et al., 2025). Northern Pakistan is
similar: at Taxila, near the study site, hourly-average module temperatures ran at
**34–50 °C** through May–July (Ali et al., 2016), and a reference module at Mirpur reached
**64 °C** at 960 W/m² (Amber et al., 2021). A clear-sky rear temperature of **55–60 °C**, the
range used throughout this work, is therefore routine, and it falls on a fast-growing fleet:
Pakistan added 583 MW of net-metered rooftop PV in 2022–23 and 1,181 MW in 2023–24 (REN21,
2025).

**Roof-integrated modules are the worst case, and the one this study targets.** A module built
into a roof or façade (building-integrated PV, BIPV) has its rear closed against the building.
Sandia's module-temperature model puts an insulated-back module about **44 °C** above ambient
at 800 W/m² and 2 m/s wind, against about **20 °C** on an open rack (King et al., 2004).
Buildings are also where PV concentrates: about **75 %** of installed PV in Germany is on
buildings (Fraunhofer ISE, n.d.). Rear ventilation and fins are unavailable when the rear is
the building envelope, which is why PCM regulation of PV began with BIPV (Huang et al., 2004,
2006; Hasan et al., 2010).

A **phase-change material (PCM)** melting near the operating temperature absorbs latent heat
at almost constant temperature and releases it overnight. Reported PV temperature reductions
are mostly **5–20 °C**, with efficiency gains of up to **16 %** (Sharaf et al., 2022). A recent
review names the barriers to practical use as low conductivity, limited storage, **leakage**
and price (El Kassar et al., 2025). This work addresses leakage. The standard remedy, shape
stabilisation, uses either a rigid porous carrier or a gelling network (§2.2); the second is
far less explored and is the one examined here.

**Rice bran wax (RBW)** is a by-product of rice-bran-oil refining. Pakistan, the world's
ninth-largest rice producer (about 14.8 Mt of paddy in 2023; FAO, 2025), has it as a domestic
residue. RBW gels vegetable oils at a few weight per cent and melts at **77–79 °C**,
ΔH = 190.5 J/g (Dassanayake et al., 2009), far above the PV window, so its network could stay
solid while a lower-melting PCM inside it does the buffering. That PCM is **lauric acid**,
which melts at **43.8 °C** (Lide, 2009; DSC studies report 43.3–43.9 °C). Its ΔH is taken as
**191 J/g** in the pre-registered predictions, while independent DSC puts it nearer
**178–184 J/g** (Fan et al., 2022; Desgrosseilliers et al., 2013), so H3 is likely 4–7 % high.
The material system was fixed first: the question is whether an RBW network can retain a
molten *fatty acid*, and lauric acid is the fatty acid that melts inside the window.

This study prepares seven RBW / lauric-acid composites, measures how much molten acid each
retains after a fixed hold at three temperatures, reports the retention limit against
predictions recorded in advance, and tests the composite behind roof-integrated mini panels
outdoors. It addresses UN Sustainable Development Goals 7, 12 and 13.

## 1.1 The research programme and its predictions

The project is a **first characterisation**, competing on experimental control rather than
fabrication quality. Three predictions were recorded **before** any retention measurement:
an ideal-mixing (Schröder–van Laar) **liquidus of ≈ 67 °C at 50 wt % lauric acid** (66–68 °C
across an assumed wax molar mass of 600–900 g/mol, a larger uncertainty than the enthalpy
value); a **network service limit of 55–68 °C**; and an **in-window latent heat of
≈ 191 J/g × (lauric-acid mass fraction)**.

Five exploratory water-bath runs came first; masses were not recorded, so they are
characterisation only. One appeared to show the composite fully liquid at **48 °C**; a properly
mixed replicate placed the liquidus near **75 °C**, and the 48 °C reading, traced to an
incompletely mixed sample, was withdrawn with everything inferred from it (§6). That is why
the preparation below is fixed tightly.

## 1.2 Objective and hypotheses

**Primary objective.** Measure the **retention limit X(T)**, the maximum lauric-acid mass
fraction retained at **≤ 2 wt % mass loss** after a two-hour hold, at **50, 60 and 70 °C**
across **20–80 wt % lauric acid**, and plot X(T) against temperature.

**Secondary objectives.** Locate the composite melting range and establish whether a *useful*
eutectic forms; obtain latent heat versus composition by DSC; test for acid–wax chemical
interaction by FTIR; relate retention to crystal-network density by SEM; and test the composite
behind a module outdoors.

Hypotheses were stated with numeric predictions before measurement (H1–H7 with this paper;
H7a–H7d in the field pre-registration of 14 October 2026, quoted as written):

| # | Hypothesis | Prediction as stated | Falsified if |
|---|---|---|---|
| **H1** | Retention depends on loading | ≤ 2 wt % loss at 50, 60, 70 °C up to a threshold lauric-acid loading | No composition meets ≤ 2 wt % at any temperature, or all do |
| **H2** | The network has a service limit | Retention ceases within **55–68 °C** | Retention at 60 and 70 °C is statistically indistinguishable from 50 °C across all compositions |
| **H3** | Latent heat scales with acid fraction | ΔH ≈ 191 J/g × *w*(LA), roughly linear | DSC enthalpy departs from linearity beyond scatter |
| **H4** | Cycling stability and nucleation | Melting onset, enthalpy and retention drift **< 5 %** over 20–25 melt–freeze cycles, with no new FTIR bands; and the composite crystallises with **less supercooling** than pure lauric acid at matched DSC scale and cooling rate, wax crystals acting as heterogeneous nucleation sites | Drift ≥ 5 %, new FTIR bands appear, or composite crystallisation onset ≤ neat-acid onset |
| **H5** | No chemical interaction | FTIR ≈ superposition of components; no carbonyl shift | A reproducible carbonyl shift appears |
| **H6** | Structure controls property | Compositions failing the leak test show lower SEM crystal-network density and/or shorter mean needle length than those passing; density coarsens after 25 cycles (ImageJ, n ≥ 30 features) | No correlation across the composition series |
| **H7** | Field cooling | The optimised composite reduces back-surface temperature by **≥ 2 °C** against a matched bare panel under October conditions | ΔT < 2 °C, or indistinguishable from zero after crossover correction |
| **H7a** | The composite runs **cooler than the plain RBW slab** of the same thickness. The difference is the contribution of melting (latent heat) over and above added mass | — | Composite is not cooler than RBW (95 % CI includes 0) |
| **H7b** | C40 + graphite runs cooler than C40 | — | 95 % CI of (graphite − C40) includes 0 |
| **H7c** | The composite melts by day and re-solidifies by night (outer-face sensors, between slab and board) | — | Outer face never passes 43 °C, or stays above it before dawn |
| **H7d** | Each slab loses **≤ 2 wt %** over the 4 days | — | Any slab loses > 2 wt % |

*Notes on the field rows.* The field pre-registration falsifies H7 if "Mean ΔT < 2 °C". The
stricter H7 condition above assumed a crossover design; the design as run had no crossover
(§3.6.2), so that correction cannot be made and the zero test is applied without it. H7a was
dropped in Version 2 and reinstated on 15 October when a wax-only slab was made. H7c was not
tested, because no outer-face sensors were fitted. The campaign ran three days, not four.

**Not hypothesised: electrical efficiency gain.** The expected 0.8–2 % relative gain is
smaller than the power scatter of unmatched mini panels, and no irradiance was measured on
site, so efficiency is reported only as a derived quantity (temperature coefficient × ΔT).

The central hypothesis (H1–H2) is **refuted** if retention at 60 °C and 70 °C is statistically
indistinguishable from retention at 50 °C across every composition.

---

# 2. Literature review

Background is treated thematically (§2.1–2.2); the directly relevant prior work is then
compared in one table (§2.3), and the gap stated (§2.4).

## 2.1 PV thermal loss and the case for passive PCM cooling

A relative power loss of about **0.45 % per °C** above 25 °C is the commonly quoted figure
(Stropnik & Stritih, 2016, as cited in Durez et al., 2023). Yadav et al. (2025) give the
realised effect for a 500 Wp North Indian array through one June: 64.0 °C peak cell
temperature and 12.0 % average daily efficiency loss, 9.6 % of it from temperature alone and
20.4 % with soiling, which accumulated at 0.43 % per day. (The paper uses 0.43 both for the
rated %/°C coefficient and for the daily soiling rate; the two must not be conflated.) Active
cooling recovers more but adds pumps, power draw and maintenance. Among passive options a PCM
acts specifically on the mid-day **peak**, which is why it is adopted here.

## 2.2 PCM leakage and the two shape-stabilisation mechanisms

Organic PCMs, paraffins and fatty acids, are the practical near-ambient choice, and loss of
the melt is their recurring deployment failure (Zalba et al., 2003; Sharma et al., 2009).
Containment works either by **porous confinement**, in which capillarity holds the liquid in
a rigid open-pore carrier, or by **network gelation**, in which a few weight per cent of a
crystalline gelator builds a space-filling mesh. Their temperature dependence should differ
in kind: a gelled network holds liquid only while it stays *continuous*, so as its crystals
dissolve into the melt on heating, retention should fail progressively, possibly well below
the temperature at which the last crystal disappears. Whether the two mechanisms' retention
curves differ in *shape*, not merely position, is open, and this project's data address it.

## 2.3 Prior work

**Table 2.1.** Directly relevant prior work and how each differs from the present study.

| Source | PCM / liquid | Matrix or container | Setting | Key finding | Difference from this work |
|---|---|---|---|---|---|
| Dassanayake et al. (2009) | RBW, bulk and oil organogel | — | material | RBW melts at 77–79 °C, ΔH ≈ 190.5 J/g; strong oil gelator through long-chain wax esters | Liquid is an oil; no storage or retention data |
| Wijarnprecha et al. (2018) | Rice bran oil | RBW, 0.5–25 wt % | food oleogel | Gels oil from **0.5 wt %**; interlinked wax needles up to 50 μm long | Oil, not a free fatty acid; texture, not storage; no leakage test |
| Zhou et al. (2025) | Soybean oil | RBW + beeswax | food oleogel | Eutectic behaviour between the two waxes | Partner is a wax; no storage or retention data |
| Barrera et al. (2020) | RBW in rice bran oil, 1:7 v/v | aluminium container | PV under a xenon lamp, 45 min | Melts at **30.06 °C**, ΔH **34.95 J/g**; efficiency 18.776 % vs 18.544 % bare | Oil carrier melts below the PV window and dilutes latent heat; efficiency, not retention |
| Wang et al. (2022) | Lauric/stearic eutectic, 31.2 °C at 7:3 | 1–15 wt % expanded graphite | material | Conductivity ×2.4–2.6 at 10–15 wt %; no leakage test | Rigid porous confinement, not a dissolving network |
| Sun et al. (2024) | Stearic acid | peanut-shell carbon | material | ≈ 0.53 W/m·K (×3.2), low leakage | Capillary carrier; the *comparison* mechanism here |
| Sarı (2005); Fan et al. (2022) | Lauric-acid binary eutectics | — | material | Pure lauric acid **43.93 °C, 178.11 J/g**; eutectics stable on cycling | Basis for lauric-acid properties and H4; no wax matrix |
| Durez et al. (2023) | Commercial PCMs at 21, 35, 44 °C | modelled layer | PV model, Bahawalpur, Apr–Aug | 21 °C PCM gives best seasonal efficiency | Deliberate deviation, argued below |
| Huang et al. (2004, 2006) | RT25 paraffin | finned aluminium container | BIPV, experiment + 2-D model | Limits temperature rise by > 30 °C vs a flat plate | Contained; 25 °C melting for a temperate climate; fins for conductivity |
| Hasan et al. (2010) | Five PCMs, 25 ± 4 °C | containers | BIPV, indoor | −18 °C for 30 min; −10 °C held 5 h at 1000 W/m² | Temperate melting point; contained; no containment measure |
| Aelenei et al. (2014) | commercial PCM | BIPV façade unit | building, field | Max. electrical and thermal efficiency 10 % and 12 % | System-level; PCM integrity not studied |
| Soares et al. (2020) | RT 22 HC paraffin | 25 mm aluminium units | open rack, Coimbra, 5 August days | PCM modules ran **14–21 °C hotter**, made 3.3–6.5 % less energy | Open rack, where the units blocked rear cooling; the reason the field test here uses an insulated back |

**Barrera et al. (2020)** is the only prior study of RBW as a PV PCM. Its authors added wax to
rice bran oil, which melts near 15 °C, "to increase the melting point to be within the
accepted range", and reached only 30 °C. Replacing the oil with a fatty acid addresses that
limitation and raises a containment question an oil system never faced: can a wax network
hold a *fatty-acid* melt? (*Publiscience* is a high-school student journal; the study is
treated as motivating prior art.)

**Deviation from Durez et al. (2023).** Their model favours a 21 °C PCM over the 35 and
44 °C materials. This project uses a 44 °C-class PCM on three grounds. (i) Their model starts
each simulation with the PCM solid and does not treat re-solidification, and a 21 °C material
cannot refreeze on Bahawalpur summer nights (June mean minimum **29 °C**; Rashid et al.,
2023), whereas lauric acid has about 15 °C of margin. (ii) They optimise seasonal efficiency;
this work targets the mid-day peak, and a 21 °C PCM is molten by mid-morning. (iii) The melting
point here follows from the material question. Practice agrees: RT42, a ~42 °C paraffin, is the
PCM mostly used in summer conditions (Sharaf et al., 2022) and among the most effective pure
PCMs for PV, with a 14.4 % efficiency gain (El Kassar et al., 2025). Two features of the Durez
model are adopted: its one-dimensional, conduction-only enthalpy formulation and its PCM
conductivity of **0.2 W/m·K** (§3.9.6).

## 2.4 Gap and aims

- **No RBW / free-fatty-acid composite has been characterised** for thermal storage. A July
  2026 search of ScienceDirect, ACS, PubMed Central, RSC Advances and Wiley (*rice bran wax*,
  *lauric acid*, *fatty acid*, *phase change material*, *eutectic*, *shape stabilis(z)ation*)
  found RBW only as an oil oleogelator and, in Barrera et al., in an oil carrier.
- **No retention-versus-temperature data exist for a natural-wax network holding a molten
  fatty acid**, to the best of our knowledge (the search was oriented toward phase-behaviour
  rather than leakage terms).
- **No hold-time series exists for a gelled-network composite**, though it is routine for
  other classes. Khalaf Alshammari et al. (2024) weighed hexadecane / LDPE composites hourly
  for 20 h at 50 °C, using the same (M₀ − Mₙ)/M₀ quantity as here; losses were 0.10–3.64 %
  after 1 h and flattened after about 14 h. An et al. (2022) applied ten 1 h holds at 60 °C
  to paraffin / expanded-graphite composites and stayed below 4 wt %.
- **Post-cycling assessment is mostly calorimetric.** Wadee et al. (2025) ran 700 cycles with
  DSC and FTIR and tested leakage separately by 500 h at 50 °C; Du et al. (2021, as cited in
  Zhou et al., 2026) report 500-cycle stability on calorimetric grounds. For a natural-wax /
  fatty-acid network neither measurement exists.
- **No container-free, bio-derived PCM has been tested on an insulated-back module.** BIPV–PCM
  work holds commercial ~25 °C PCMs in containers (Table 2.1); added to an open-rack module, a
  PCM unit made it hotter (Soares et al., 2020).

This study therefore measures X(T) for RBW / lauric-acid composites at 50, 60 and 70 °C,
re-measures retention after ≈ 10.6 h of accumulated heating so that the limit carries its
hold time (§4.5), and tests the composite without a container behind insulated-back modules,
measuring both module temperature and slab mass. Testing PCM on BIPV is not new; testing a
container-free, waste-derived composite there, with its retention measured, is. No beneficial
eutectic is claimed (§4.3).

---

# 3. Research methodology

The core method is a **gravimetric retention (leak) test** in the form widely used for
shape-stabilised PCMs (heated hold, filter-paper capture, leakage as (M₀ − Mₙ)/M₀ × 100;
Khalaf Alshammari et al., 2024; An et al., 2022). The two-way mass balance, sealed control and
pre-declared decision rules were added for this study.

**Variables.**

| Type | Variable |
|---|---|
| Independent | Composition (20, 30, 40, 50, 60, 70, 80 wt % lauric acid); hold temperature (50, 60, 70 °C); cycle number (0, 25); field station (bare, RBW, C40, C40 + graphite) |
| Dependent | Specimen mass loss (%), the retention measure; melting onset and *k*<sub>eff</sub> dips; ΔH, onset and supercooling by DSC; FTIR band positions; SEM network density and needle length; module back-surface temperature; slab mass loss |
| Controlled | Specimen geometry and mass range; thermal history (melt, mix, pour, cool, 24 h anneal); 2 h hold; 30 min cooling before weighing; balance warm-up and re-zero schedule; module type, tilt and orientation; insulated back, open-circuit leads and sensor position, identical on every module; slab size |

All preparation was carried out in the Chemistry Laboratory, Cadet College Hasanabdal. DSC,
FTIR and SEM are performed as a facility service at ⚠️ [GIKI Topi, Swabi — confirm].

## 3.1 Materials

| Material | Supplier | Grade | Batch | Role |
|---|---|---|---|---|
| Lauric acid | Bioshop PK | 99 % (supplier-stated) | — | PCM |
| Rice bran wax | Aogubio Co., Ltd. | 99 % (supplier-stated) | PR 1798 | Matrix / gelator |

Neither grade was verified independently (§6). All compositions are quoted on a **mass basis**
from the balance readings actually recorded.

## 3.2 Composite preparation

Seven compositions were prepared, **20–80 wt % lauric acid** in 10 wt % steps, balance RBW
(Figure 3.1). The protocol was: melt the RBW at **85 ± 2 °C** until clear; add the acid in two
or three portions; hold **20 min at 85 °C** with periodic stirring, never above 100 °C;
settle 5 min; re-weigh (a loss > 0.5 % flags overheating); pour into pre-warmed moulds to
uniform depth, setting aside ~10 g of each as a melting-point specimen; cool on one surface
without forcing; anneal **24 h** at room temperature.

**As run.** Melting and holding used a **Memmert UN30** natural-convection oven at 85 °C, not
a water bath, and every composition soaked for more than 1 h at 85 °C before pouring. Casting
masses were recorded (for example, C20: 11.98 g lauric acid and 48.05 g RBW), and nine
specimens were cast per composition. All seven are taken to have had the same 24 h anneal
⚠️ [CONFIRM — recorded as outstanding in the Session 6 log].

**One casting session.** Cooling rate sets crystal structure, which sets retention, so all
compositions were cast in one session under identical cooling. **Recorded deviation:** the
melt solidified within ~1 min, so the compositions were poured **one at a time, 20 → 80 wt %**,
the rest held at 85 °C. The extra residence (≤ ~15 min, after a common > 1 h soak) is argued to
be negligible, but because the order was monotonic with composition it is aliased with the
composition trend (§6).

![Figure 3.1](../Data%20Analysis/outputs/fig_photo_lab.jpg)

**Figure 3.1.** Laboratory work. (a) Materials: rice bran wax (batch PR 1798, foil bag), lauric
acid, filter paper, specimen dishes and the mini panels. (b) Molten compositions in the Memmert
UN30 oven at 85 °C, with the silicone specimen moulds pre-warming below. (c) Water-bath
heating-curve set-up (§3.4). (d) Weighing specimens on the 0.01 g balance (§3.3.5).
Photographs: ⚠️ [credit line — confirm who took each photograph].

## 3.3 Retention (leak) test

### 3.3.1 Design

A full factorial of **7 compositions × 3 temperatures × 3 replicates = 63 specimens**, each
used once.

- **Temperatures.** 50 °C is above lauric acid's melt but below significant wax dissolution;
  60 °C is a representative module rear temperature; 70 °C approaches the ~75 °C composite
  liquidus. The set brackets failure rather than avoiding it.
- **Blocking by oven run.** Each run holds one replicate of all seven compositions (plus two
  blank papers and one sealed control), giving **nine runs**. Run-to-run variation therefore
  enters the error bar, and compositions are always compared within a shared load.
- **Randomisation.** Shelf positions within each run, and specimen-to-cell assignment, were
  randomised and recorded.

If specimens ran short, replicates were to be protected at the expense of temperatures
(a complete n = 3 curve at two temperatures before any n = 1 work at a third).

### 3.3.2 Specimens and geometry

Leakage is a surface process, so the surface-to-volume ratio must be constant. Specimens were
cast in one silicone mould, as **regular pentagonal prisms** (nominal cavity 19 mm across,
17 mm deep; the protocol's "cube"). Spot-checks on 12 specimens measured 1.85–1.95 cm across and
1.5–1.8 cm high. Masses were **4.0–5.4 g, mean 4.73 ± 0.34 g (n = 63)**, against a nominal 7 g.
Specimens with a visible void, crack or skin defect were excluded before any run.

### 3.3.3 Oven and temperature control

Holds used the **Memmert UN30** oven, which displays chamber temperature to 0.1 °C under PID
control, so dial offset and temporal cycling are controlled by the instrument. Spatial
variation is handled by using the centre of one mid-height shelf and by position
randomisation; the manufacturer's spatial uniformity is ⚠️ [CITE — UN30 datasheet
temperature uniformity]. The air flap was set once. The displayed temperature was logged
before loading, on door closure, on recovery to within 1 °C of setpoint (which starts the
two-hour hold), every 30 min, and at unloading.

### 3.3.4 Filter paper and blanks

Whatman No. 1 paper carries ~6 % water, which it loses in a warm oven. The protocol dried all
papers at 105 °C and stored them over silica gel; **as run, papers were used straight from the
box**, and the moisture correction rests on **two blank papers per run** (the protocol asked
for three when drying was omitted). Two paper batches were used (mean dry mass 0.83 g at 50 °C;
1.02–1.03 g at 60–70 °C); only each paper's own before-and-after difference enters any
calculation.

### 3.3.5 Procedure

On a balance of 0.01 g readability ⚠️ [CONFIRM — make/model], warmed and re-zeroed every ten
weighings, the dish (m<sub>d0</sub>), paper (m<sub>p0</sub>) and specimen (m₀) were each
weighed **three times and averaged**. Each was assembled dish → paper → specimen. All positions
were loaded in under 30 s with one door opening, and the oven was not opened during the
two-hour hold. Afterwards, specimen, paper and dish were re-weighed by the same method
(m₁, m<sub>p1</sub>, m<sub>d1</sub>); the sealed control was weighed before and after every run.

**As run, no desiccator was used:** specimens cooled **30 min on the bench**, and their
temperature was not measured before weighing (§6). The papers were **not photographed**, so
the planned stain-area channel was not obtained. Full handling rules are in Appendix B.

### 3.3.6 Calculations and controls

$$
\text{Leakage}\,(\%) = \frac{m_0 - m_1}{m_0}\times 100 \qquad \text{(primary)}
$$

$$
\text{Transfer}\,(\%) = \frac{(m_{p1} - m_{p0} - \Delta m_\text{blank}) + (m_{d1} - m_{d0})}{m_0}\times 100 \qquad \text{(cross-check)}
$$

$$
\text{Closure}\,(\text{g}) = (m_0 + m_{p0} + m_{d0}) - (m_1 + m_{p1} + m_{d1}) \qquad \text{(unaccounted mass)}
$$

**Leakage** is the primary result and, because the specimen is non-hygroscopic, independent
of paper moisture. **Transfer** recovers the lost mass on paper and dish (liquid runs down
the prism sides past the paper edge, so the dish is weighed too). **Closure** is mass that left
as vapour or was spilled. A **sealed control** (one specimen in a screw-cap vial, re-used across
all runs) bounds evaporation directly. Whether two-hour leakage has plateaued is addressed by
the soak arm of §3.5.

**Pass criterion:** mean Leakage ≤ **2 wt %** over three replicates, reported as mean ± SD.

### 3.3.7 Precision and decision rules

On 4.0–5.4 g specimens one balance increment is 0.19–0.24 % of m₀. The **limit of detection**
is one increment (mean 0.21 %), the **limit of quantitation (LOQ)** three (mean **0.64 %**);
values below LOQ are reported but not ranked. The 2 % criterion is 9–11 increments. Decision
rules fixed before the first run (Appendix B) cover collapse (a specimen that cannot be lifted
from its paper intact is a definitive **fail** with no leakage value), oven excursions (void the
whole run), handling loss, defective specimens, blank drift and replicates (none dropped
without a documented physical cause). The Leakage–Transfer threshold of 0.4 % is a diagnostic
flag, never grounds for exclusion.

### 3.3.8 Analysis and headline output

**X(T)** is obtained by linear interpolation between the bracketing compositions:

$$
X(T) = C_\text{pass} + (C_\text{fail} - C_\text{pass})\,\frac{2 - L_\text{pass}}{L_\text{fail} - L_\text{pass}}
$$

where C<sub>pass</sub> is the highest composition with mean leakage L<sub>pass</sub> ≤ 2 % and
C<sub>fail</sub> the next one up. Its uncertainty is a bootstrap interval (2 × 10⁴ resamples
within cells).

**Statistics.** One-sided permutation tests (10⁵ resamples, fixed seed) against ordered
alternatives: a Jonckheere–Terpstra (JT) test for the composition trend at each temperature;
a JT test stratified by composition for temperature, with stratified Mann–Whitney tests for
each step and an exact sign test on cell means; and a within-cell permutation test for
run-to-run variation. Collapsed specimens rank above every measured value but are never
assigned a number. A two-way ANOVA is not claimed at this replication.

**Pour-order control.** The protocol specified recasting 20 and 80 wt % in reverse order and
testing at 60 °C ⚠️ [Confirm whether the recast was run. If not, move it to §8 and keep the
argued basis in §6.]

## 3.4 Supporting thermal characterisation

Melting behaviour is characterised by **indirect water-bath heating** with one sensor in the
sample and one in the bath (Figure 3.1c). For purely sensible heating the sample's rate is
proportional to the driving difference, so

$$
k_\text{eff} = \frac{\mathrm{d}T_\text{sample}/\mathrm{d}t}{T_\text{bath} - T_\text{sample}}
$$

is roughly constant, and a **dip in k<sub>eff</sub>** marks heat going into latent form, locating
a transition too broad to show as a plateau. Over each band [*a*, *b*] it is evaluated in
integrated form, k<sub>eff</sub> = (T<sub>j</sub> − T<sub>i</sub>) / ∫(T<sub>bath</sub> −
T<sub>sample</sub>) d*t*, by the trapezoid rule (`Data Analysis/paper_figures.py`). Runs start
from a cold bath and heat continuously to complete melting. The water-bath composite runs lack
recorded masses and are preliminary (§1.1).

## 3.5 Thermal cycling stability

A material that passes a two-hour hold has not been shown to survive a season, so H4 is tested
by repeated melt–freeze cycling of **C40**, the highest loading that passes at 60 °C (§4.4),
cast in the same mould ⚠️ [Casting batch: the original Session 6 casting, or a new one? A new
casting needs its own 2 h baseline specimens.]

### 3.5.1 Cycling protocol

| Arm | n | Treatment |
|---|---|---|
| **CYC** | 3 | 25 cycles: ~25 min in the oven at 60 °C, then cooled on the bench until the surface is dull white (acid frozen), minimum 25 min |
| **SOAK** | 2 | Held continuously at 60 °C for the same total hot time as CYC |
| **Baseline** | 3 | The C40 / 60 °C cell of the retention matrix (2 h) |

CYC differs from the baseline in both cycle count and hot time. SOAK matches CYC on hot time,
so **CYC − SOAK isolates cycling** and **SOAK − baseline isolates time at temperature**.
Specimens sit open on paper in weighed dishes, as in §3.3, with one blank paper per arm;
evaporation over ~10 h is not negligible but is common to CYC and SOAK. Every hot leg is
timed. Cycling and soak are distinguished only if **|CYC − SOAK| > 1 percentage point**; a
smaller difference is "no resolvable difference". Onset and enthalpy drift are measured by DSC
and new bands by FTIR on the cycled specimen against an unheated reference (§3.7)
⚠️ [confirm whether the cycled specimen was submitted]. FTIR also guards against a degradation
product that thickens the melt and makes cycled leakage look better than it is.

### 3.5.2 Tilted long-cell settling assay (designed, not performed)

Solid RBW (0.96–0.99 g/cm³) is denser than molten lauric acid (~0.85 g/cm³ at 70 °C). Once the
network dissolves on a hot afternoon, the remaining crystals can settle toward the low edge of
a tilted container, leaving unsupported acid at the top of the panel, its hottest region. A
horizontal filter-paper test cannot detect this; El Kassar et al. (2025) likewise recommend
inspecting composite PCMs for "degradation or separation within the composite material". The
assay designed for it (a sealed cell ≥ 300 mm long at 20–35° tilt, cycled with CYC,
photographed hot, then sliced into thirds and the wax fraction measured) **was not run**, so
no extrapolation from §3.3 to a tilted module is made (§6, §8).

## 3.6 Field evaluation

H7 was tested on a roof in **Al Khobar, Saudi Arabia** (26.2° N) on **15, 16 and 17 October
2026**, behind **insulated-back (roof-integrated) modules** (Figure 3.2). The planned site was
Cadet College Hasanabdal. Al Khobar's October afternoons were hotter than the model's climate:
modelled air 33–41 °C and ≈ 800 W/m² at noon (Open-Meteo), against 15–29 °C (§3.9.6).

### 3.6.1 Stations and slabs

Four frameless mini mono-crystalline panels of one model, each **1 W, 3 × 5 in (7.6 × 12.7 cm,
97 cm²)**, not IV-matched, formed four stations:

- **(A) bare**;
- **(B) rice bran wax alone**, the thermal-mass control: RBW melts only near 70–73 °C (§4.1),
  so it adds mass and sensible heat without latent heat, and C − B isolates the latent effect;
- **(C) C40**;
- **(D) C40 + graphite**, 4 g natural graphite per 100 g composite (≈ 3.8 wt %), from a second
  casting.

**No container is used.** Each slab is **14 × 7 × 1 cm** (measured after the campaign; the
pre-registration assumed ≈ 2 cm). Masses before: RBW 98 g, C40 96 g, C40 + graphite 100 g. A
slab covers ≈ **92 %** of the module rear (12.7 × 7 cm), overhangs one end by ≈ 1.3 cm and is
notched around the two lead joints (Figure 3.2b). It is held between module and board by tape
on the module edges; nothing is stuck to the slab.

**Mounting.** Every module, the bare control included, is taped to its own 20 mm
expanded-polystyrene board, whose lower edge rests on a box and upper edge on a south-facing
wall (tilt ≈ 35°). Every sensor is therefore covered, by a slab or by the bare station's board,
so none is convectively cooled while another is insulated. Leads are open-circuit, ends taped
separately; catch paper lies under every module.

**Sensors.** One DS18B20 is taped to each module back at the same measured position on all
four and **sandwiched between the module and its slab** (on the bare station, between the
module and its board), on all three days. Each therefore reads the module's rear surface where
the slab presses against it. *Correction, 17 October 2026: earlier records, including the Day 1
note in the field pre-registration, place the sensor just below the slab's lower edge; the
authors confirm it sat between module and slab throughout.* Sensors are identified by ROM
address; the mapping
was confirmed by warming each probe on 16 October (S0 C40 + graphite, S1 C40, S2 RBW, S3 bare),
correcting Day 1's file header.

![Figure 3.2](../Data%20Analysis/outputs/fig_photo_field.jpg)

**Figure 3.2.** Field rig. (a) The four stations on the roof, each module taped to its own
polystyrene board, slab edges visible behind three of them. (b) The rear of a mini panel,
showing the two lead joints the slabs are notched around. (c) The logger: an Arduino Uno and
breadboard reading the four DS18B20 sensors over USB. Photographs taken by the authors.

### 3.6.2 Design and controls, as run

- **Rotation.** Each morning whole stations (board, slab and module) moved one position along
  the row, spreading position effects across days, but **panel and sensor bias stay tied to
  treatment**. The bare calibration run (all slabs off, stations moved every 15 min) was not
  available for analysis, so no panel correction is applied (§6).
- **Timing.** Day 1 logging began at ≈ 13:30, after solar noon (≈ 11:25); Day 2 at ≈ 11:47;
  Day 3 at 11:45, running to ≈ 18:50, past sunset (≈ 17:15). No pre-dawn logging. The stations
  stayed outdoors throughout the campaign, about 72 h in total. On Day 3 the row was checked
  every 30 min. The logger had no clock, so start times are recorded by hand.
- **Logging.** An Arduino Uno read the four sensors every 2 s; raw Serial Monitor transcripts
  are kept unchanged beside the clean files.
- **Weather.** No on-site pyranometer or ambient sensor was available. Irradiance, air
  temperature, wind and cloud come from the Open-Meteo API (Zippenfenig, 2023) at 15 min
  resolution, interpolated to each reading. These are **model values**, used to tell cloud
  from local shadow and to compare stations at matched sunlight.
- **Mass.** Slabs were weighed before the first day and after the last on a 1 g kitchen scale.
  The C40 + graphite slab partly collapsed on Day 2, was left in place for Day 3, and was weighed
  broken, without fragments stuck to its board.
- The field ΔT is compared against the **pre-registered model prediction** (§3.9.6, v2).
- **Not run.** A side-by-side oven hold of C40 and C40 + graphite specimens at 60 and 70 °C,
  under the §3.3 protocol, is needed to tell whether graphite itself weakens the network or the
  collapse was a field effect ⚠️ [PENDING — C40 vs C40 + graphite oven test].

## 3.7 Sample preparation for external instrumental analysis

DSC, FTIR (ATR) and SEM are performed by facility staff; the authors prepare, seal, label and
submit the samples and analyse the returned data. The requested sample sets and programmes are
in Appendix C. ⚠️ [Record from the facility report: instrument models, samples actually run
and programme actually used.] In brief: **DSC** on raw RBW, pure lauric acid and C30/C50/C70
(all seven if time allows), loaded molten, heat–cool–heat 20 → 90 → 20 → 90 °C at 1–2 °C/min
under N₂, with supercooling taken from the cooling segment at matched mass and rate; **FTIR**
on the same series plus cycled C40, examining the carbonyl (≈ 1700 and ≈ 1735 cm⁻¹) and O–H
regions; **SEM** on raw RBW, one low- and one high-acid composite, and uncycled and cycled C40,
with network density and needle length measured in ImageJ (n ≥ 30 features).

**Scope limit.** A DSC pan holds 5–20 mg, and a milligram sample supercools more than a bulk
one, so the H4 supercooling comparison is valid at DSC scale only. No bulk T-history apparatus
was built; the field evening cooling rates (§4.9.2) give partial evidence at real scale.

## 3.8 Sensor calibration

The four **DS18B20** sensors (12-bit, 0.0625 °C resolution, ±0.5 °C factory accuracy) were
given a **one-point offset** in a stirred crushed-ice slurry, tips bundled, each reference the
mean of 10 settled readings. Ice-bath means were **1.61, 1.39, 1.86 and 1.37 °C** (S0–S3; raw
spread 0.49 °C). The bath sat above 0 °C, so the offsets are used **only to compare sensors
with one another**. In an independent room-temperature water check, the raw spread of 0.41 °C
fell to **0.11 °C** after correction; that residual is the sensor-to-sensor uncertainty used
here. It was measured at ≈ 28 °C only: span (slope) differences at 40–70 °C are not corrected,
and the planned boiling-water point was not run. The melting-point trials used a 1 °C glass
thermometer and the retention holds the oven's display; the field data are the only results
that use these sensors.

## 3.9 Data analysis and statistics

### 3.9.1 Retention series

As set out in §3.3.8. Scripts in `Data Analysis/` regenerate every figure and number from the
workbook (`Data Analysis/leak_analysis_matrix.py` → `outputs/leak_matrix_results.txt`).

### 3.9.2 Heating curves

A single line fitted across a phase transition is meaningless, so each heating trial is split
at its first melting observation into a **sensible ramp** and a **melt region**, and the
melt-region slope is divided by that trial's own ramp (the cut-point is declared as a
researcher degree of freedom). Where the bath was logged, the boundary-free *k*<sub>eff</sub>
analysis of §3.4 is used instead. These are time series with serially correlated residuals,
so ordinary least-squares p-values are optimistic and are not presented as if observations
were independent.

### 3.9.3 Uncertainty budget

Type A (replicate and day-to-day scatter) and Type B (±0.5 °C sensor accuracy; 0.01 g
readability, *a*/√12 for a rectangular limit) are combined in quadrature. For a field
difference, u(ΔT) = √(u₁² + u₂²): 0.71 °C with uncalibrated sensors, falling to the 0.11 °C
inter-sensor spread after the offset correction. The sensors therefore do not limit the field
comparison; **panel and position bias** does, because with one module per treatment the
design does not remove it (§3.6.2, §6). Propagating V, I, irradiance and area into efficiency
gives an uncertainty larger than the expected effect, which is why efficiency is not
hypothesised. Reported precision matches uncertainty throughout.

### 3.9.4 Field data

Ice offsets are applied per sensor, and each slab station is differenced against the bare
station at the same moment.

**Pre-registered main number.** For each day, each slab station's peak is subtracted from the
bare station's peak (Day 2's last 5 min, packing up, excluded). The three daily values are
reported as mean ± SD with a t-based 95 % CI (n = 3). No other significance test is run;
effects are reported as sizes with their conditions.

**Post-hoc analyses, labelled as such.** (i) A **findings window** of the first 90 min of each
day, chosen after Day 2's data showed a shadow crossing the row from ≈ 95 min (modules dropped
one after another at 0 % modelled cloud); on Day 3 the row lost direct sun from ≈ 180 min.
**No reading is discarded**: full records are plotted and reported. (ii) **Matched sunlight**:
readings with modelled irradiance ≥ 600 W/m², shadow excluded, pooled across days. (iii)
**Evening cooling rate** (10 min running mean) compared at equal module temperature after the
row loses sun: a slab releasing latent heat on freezing should cool more slowly near 43–44 °C.
Modelled cloud cover was ≤ 7 % on all days, so the pre-registered cloud criterion excluded no
day. Analysis: `Data Analysis/field_analysis.py`; raw files in `Field Test Data/`.

### 3.9.5 Comparison against the pre-registered predictions

Measured DSC enthalpies are compared against the **191 J/g × *w*(LA)** line (zero intercept)
and the measured liquidus against the ideal Schröder–van Laar curve. Departures are reported as
findings with their direction; predictions are not adjusted after the fact.

### 3.9.6 Panel-scale thermal model and its pre-registered prediction

H7 concerns a panel, not a material. The two are bridged by a lumped two-node transient model
(`Data Analysis/pcm_panel_model.py`), run **before** the field campaign so that its output is
a falsifiable prediction. The module is one node; the composite is a second node handled by the
**enthalpy method over its measured melting band** (solidus 43 °C, liquidus 75 °C). Heat leaves
the front by wind convection and long-wave radiation to sky and ground; the rear either loses
heat to open air (open rack) or conducts through a 20 mm polystyrene board (insulated back),
and the same boundary is applied to the bare module and to the composite's outer face.
Integration is explicit Euler at 2 s over three days of a synthetic October climate for
northern Pakistan (Topi, near the planned Hasanabdal site: 15–29 °C, 800 W/m² clear-sky peak,
2 m/s wind). Equations are in Appendix A.

**Table 3.1.** Model parameters.

| Symbol | Quantity | Value | Status |
|---|---|---|---|
| *T*<sub>s</sub>, *T*<sub>l</sub> | solidus, liquidus | 43 °C, 75 °C | measured (§4.2, n = 1) |
| ΔH | latent heat of the composite | 76 J/g | prediction for C40 (191 J/g × 0.40); v1 used 95 J/g |
| ρ | density | 900 kg/m³ | placeholder |
| *c*<sub>p</sub> | specific heat | 2.0 J/g·K | literature (Durez et al., 2023) |
| *k* | conductivity | 0.2 W/m·K | literature (Durez et al., 2023) |
| *L*, *A* | layer thickness, module area | 0.02 m, 0.10 m² | design |
| *C*″ | module areal heat capacity | 9000 J/m²·K | order-of-magnitude estimate |
| (τα) | transmittance–absorptance | 0.90 | assumed |
| *h*<sub>b</sub> | back-face convection | 8 W/m²·K | assumed, identical in both cases |
| ε<sub>f</sub>, ε<sub>b</sub>, ε<sub>c</sub> | emissivity: glass, backsheet, composite | 0.85, 0.85, 0.90 | assumed |
| β | tilt | 35° | design (field rig) |
| *T*<sub>sky</sub> | clear-sky temperature | 0.0552 *T*<sub>a</sub><sup>1.5</sup> | Swinbank (1963) |
| *L*<sub>i</sub>, *k*<sub>i</sub> | insulation board | 20 mm, 0.035 W/m·K | design; typical expanded polystyrene |
| *V* → *h*<sub>w</sub> | wind → front convection | 2 m/s → 13.2 W/m²·K | Durez et al. (2023), Eq. 1 |
| η<sub>ref</sub>, β | efficiency at 25 °C, coefficient | 0.18, 0.0043 °C⁻¹ | rated (Yadav et al., 2025) |
| Δ*t* | timestep | 2 s, 3 days | numerical (convergence in §4.10) |

The model departs from Durez et al. (2023) deliberately: it runs **multi-day** and reports
whether the PCM re-solidifies each night, models a **melting band** rather than a sharp melting
point, and (from v2) includes **long-wave radiation** and a choice of **mounting**. ΔH, ρ,
c<sub>p</sub> and **k** are placeholders pending DSC and hot-wire measurement, with *k* the
dominant unknown, so the model verifies **behaviour**, not magnitudes.

**The prediction, stated in advance.** Two versions exist, both recorded before any field
data. Both are reported, and neither is revised after the campaign.

**Version 1** (git commit 63b03fa; open rack, convection only, 0.1 m² module, 2 cm layer,
ΔH = 95 J/g). At the placeholder conductivity the model predicts that the composite layer
**fails H7, and fails it in the wrong direction**:

| | Bare | With composite |
|---|---|---|
| Peak back-surface temperature | 61.5 °C | **66.7 °C** |
| Peak ΔT | — | **−5.3 °C** (hotter) |
| Daylight mean ΔT | — | −3.8 °C |
| Mean efficiency change | — | −0.16 pts (−0.9 % relative) |
| **H7 (≥ 2 °C drop)** | — | **not met** |

**Version 2** (15 October 2026, before the campaign). The *design* changed to insulated-back
modules, C40 and 2 cm slabs; the *model* gained long-wave radiation, which lowers the v1
open-rack bare peak from 61.5 °C to 47.8 °C, close to the ≈ 49 °C that Sandia's coefficients
give for the same conditions (King et al., 2004). For the field configuration v2 predicts:

| | Bare | C40, 2 cm | C40 + graphite, 2 cm (k 0.3–0.4) |
|---|---|---|---|
| Peak back-surface temperature | 59.2 °C | 57.3 °C | 57.0–57.1 °C |
| Peak ΔT | — | **+1.9 °C** (cooler) | +2.1 to +2.2 °C |
| Daylight mean ΔT | — | +0.8 °C | +0.8 to +0.9 °C |
| Peak liquid fraction | — | 0.25, solid again by every dawn | 0.31–0.35 |
| Peak composite temperature | — | 51.0 °C | 53–54 °C |
| **H7 (≥ 2 °C drop)** | — | **borderline: not met by 0.1 °C** | met by 0.1–0.2 °C |

Three features of v2 matter. **Mounting decides the sign:** the same slab on an open rack runs
6.0 °C hotter than bare and never melts, while against insulation (*U* ≈ 1.5 W/m²·K, against
*k*/*L* = 10 W/m²·K for the slab) its storage dominates. **Conductivity barely matters:** on the
insulated rear, *k* from 0.2 to 6 W/m·K moves peak ΔT only between +1.6 and +2.2 °C, so graphite
should make no detectable difference. **About half the cooling is mass:** a wax-only slab is
predicted at **+0.8 °C**, so C40 should run about 1.1 °C cooler than wax alone at peak.

The slabs were later measured at **1 cm**. The 2 cm prediction is the one tested; for
reference only, the same model at 1 cm gives C40 **+0.8 °C** at peak (liquid fraction 0.40,
composite peak 56 °C). The field ran in a hotter climate than the model (§3.6), so the
comparison is made on **differences between stations**, and the prediction is not re-run on Al
Khobar weather. Three outcomes were distinguished in advance: the field ΔT matches, exceeds or
falls short of the prediction. **The prediction is not revised after the campaign.**

## 3.10 Safety

Molten lauric acid at 70 °C burns skin: oven gloves for trays, forceps for specimens. The acid
is a mild eye and skin irritant and warm acid gives off a strong vapour, so gloves, eye
protection and ventilation were used, and all heated work was supervised by the chemistry
teacher. Paper and solvent were kept clear of the oven elements. **Graphite powder** was weighed
in ventilation with a dust mask, away from the balance and melt, and kept off the modules' bare
lead ends, since a graphite bridge would short the module; the collapsed graphite slab was
handled with gloves. Slabs were cut with a warm, dried knife, away from the hand. In the field,
the frameless panels were carried by their edges; module voltage is a few volts and leads were
open-circuit. The laptop, the only mains item, was kept shaded, raised off the roof and off wet
ground, and taken inside above about 35 °C shade temperature. The team worked in shade where
possible and carried water. Leaked composite was disposed of as solid waste with its catch
paper, never down a drain.

---
