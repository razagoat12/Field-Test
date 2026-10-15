# Thermal chamber — build guide

Arduino-controlled temperature chamber for the leakage series (50/60/70 °C) and,
more importantly, **automated cycling** (Protocol F: 20–25 cycles, 60 °C ↔ 25 °C).

> ⚠️ **Build this only if you don't get oven access, or if you keep the cycling test.**
> A laboratory drying oven is better for the leakage series — it reaches 70 °C without
> extrapolation, has engineered uniformity, and needs no build time. The chamber's unique
> value is unattended cycling, which no standard oven can do.

**Evidence base:** [OpenTCC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9041232/) (*HardwareX*,
peer-reviewed) validated an Arduino chamber at **50 °C ± 0.2 °C for 60 hours**. An
[Arduino neonatal incubator](https://pmc.ncbi.nlm.nih.gov/articles/PMC10393824/) held
36 ± 0.1 °C. Those are careful builds — treat their figures as achievable, not automatic,
and validate your own (see §7).

---

## 1. Parts list

| Part | Spec | Notes |
|---|---|---|
| **PTC heater + fan module** | 12 V, 50–100 W | ⭐ Best choice. **Self-limiting** — cannot thermally run away. Usually ships with fan attached |
| **MOSFET module** | IRF520 or similar | Switches the 12 V heater from an Arduino pin. PWM-capable |
| **Power supply** | 12 V, 5 A minimum | 60 W. Size up if using a 100 W heater |
| **Circulation fan** | 80 mm, 12 V | Computer case fan. **Runs continuously**, not switched with the heater |
| **DS18B20 × 3** | ✅ have | Control, far-corner, heater-side |
| **4.7 kΩ resistor** | ¼ W | ⚠️ **1-Wire pull-up. Sensors will not work without it.** Most-forgotten part |
| **Arduino + RTC** | ✅ have | |
| **Thermal fuse** | 100 °C, in series with heater | Hardware backstop independent of software |
| **Enclosure** | see §2 | |
| Jumper wires, terminal blocks | | |

Rough cost if you have the Arduino/sensors: **PKR 3,000–5,000**.

### Why PTC over a light bulb

A bulb is a **point source** — it radiates directly onto whatever faces it, so samples
read hotter than air temperature. It also runs on mains. A 12 V PTC element is
low-voltage, distributes heat through its fan, and is **self-limiting**: its resistance
rises with temperature, so it physically cannot run away even if the control fails.

If you must use a bulb: 25–60 W, mains through an **optoisolated** relay module, and get
a teacher to check the wiring.

---

## 2. Enclosure

**Options, best first:**

1. **Thermopore/styrofoam cooler box** — good insulation, cheap. ⚠️ Polystyrene softens
   near 90 °C, so the heater must never touch or face a wall directly.
2. **Wooden or cardboard box lined with thermopore sheet** — more work, safer at 70 °C.
3. **Metal biscuit tin lined with insulation** — safest, hardest to work with.

**Size:** big enough for your sample rack plus ~10 cm clearance around the heater.
For 21 leakage discs you need a shelf roughly 30 × 30 cm. For cycling only, much smaller.

**Critical:** cut a small vent hole (~10 mm) high on one wall. A completely sealed box
traps moisture driven off the samples, and for a gravimetric test that moisture must leave.

---

## 3. Internal layout

```
   ┌──────────────────────────────────┐
   │  [PTC + fan] →→→  ║  ← baffle    │
   │                   ║              │
   │      ┌────────────╨──────┐       │
   │      │   SAMPLE  RACK    │       │
   │      │  ● control sensor │       │
   │      └───────────────────┘       │
   │                                  │
   │  ● far-corner sensor        vent○│
   └──────────────────────────────────┘
        ↑ circulation fan (continuous)
```

**Four rules:**

1. **Baffle between heater and samples.** Without it, samples receive radiant heat and sit
   hotter than the air. A piece of aluminium or a metal sheet is enough.
2. **Control sensor sits at the samples**, not near the heater. You are controlling the
   temperature the samples experience.
3. **Far-corner sensor** is your uniformity check. Log it; never control on it.
4. **Fan runs continuously**, independent of the heater. Air circulation is what buys
   uniformity — OpenTCC used *eight* distributed heating pads for this reason.

---

## 4. Wiring

```
Arduino 5V  ──┬── DS18B20 VDD (all three, parallel)
              └── 4.7 kΩ ──┐
Arduino D2  ───────────────┴── DS18B20 DATA (all three)
Arduino GND ─────────────────── DS18B20 GND

Arduino D3  ─── MOSFET module SIG
Arduino GND ─── MOSFET module GND

12V PSU (+) ─── thermal fuse ─── PTC heater (+)
PTC heater (−) ─── MOSFET V+ / V− ─── 12V PSU (−)

12V PSU ─── circulation fan (direct, always on)

RTC: SDA → A4, SCL → A5, VCC → 5V, GND → GND
```

All three DS18B20s share one data pin — 1-Wire is a multi-drop bus. The **4.7 kΩ pull-up
between DATA and 5 V is mandatory.**

---

## 5. Control strategy

**Bang-bang with hysteresis.** Simpler than PID, adequate for your tolerance, no tuning.

```
if  T < setpoint − 0.5 °C   → heater ON
if  T > setpoint + 0.5 °C   → heater OFF
otherwise                    → unchanged
```

Expect **±0.5–1 °C** in practice. Your leakage test does not need better. PID would get
you nearer the published ±0.2 °C but costs a tuning session you probably can't spare.

---

## 6. Safety — both layers, non-negotiable

| Layer | Implementation |
|---|---|
| **Software** | If any sensor reads > setpoint + 15 °C, or reads −127 (disconnected), cut the heater and halt |
| **Hardware** | 100 °C thermal fuse in series with the heater — works even if the Arduino crashes |
| **Inherent** | PTC element is self-limiting |

Never run unattended overnight until you have watched a full cycle complete correctly.

---

## 7. ⭐ Validate before you trust it

**Do not assume the published figures apply to your build.** Two-hour empty test:

1. Set to 60 °C, no samples, both sensors logging every 30 s
2. Let it stabilise, then run 2 hours
3. From the log, compute:

| Metric | Target |
|---|---|
| **Stability** — max − min of the control sensor after stabilisation | ≤ ±1 °C |
| **Uniformity** — mean difference between control and far-corner sensor | ≤ 2 °C |
| **Time to setpoint** | note it; affects cycle timing |

This converts *"published designs achieve ±0.2 °C"* into *"**my** chamber holds
±X °C with ≤Y °C gradient"* — which is what belongs in your methods section, and what a
judge will ask for.

**Also calibrate the sensors first** — two-point, exactly as you did the glass thermometer:
ice water (0 °C) and boiling water (~98 °C at 450 m). DS18B20 is ±0.5 °C from the factory;
calibration tightens the absolute reading.

---

## 8. Known limitation

OpenTCC's validated range is **20–55 °C**. Your 70 °C setpoint is **beyond any published
validation** for this class of build. Heating higher is the easy direction — more power,
better insulation — but note it honestly in your methods, and lean on the oven for 70 °C
if you can get one.
