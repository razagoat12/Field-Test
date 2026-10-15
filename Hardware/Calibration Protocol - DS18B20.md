# DS18B20 calibration — today

Two-point calibration of all sensors before any run. Takes about an hour.
Sketch: `ds18b20_calibrate.ino`. No RTC required.

---

## ⚠️ First: are your sensors waterproof?

| Type | Can it go in water? |
|---|---|
| **Stainless probe on a cable** | ✅ Yes, directly |
| **Bare TO-92 (black 3-pin chip)** | ❌ **No.** Water shorts the pins |

**If bare:** seal each in a small plastic bag with the leads exiting the top, squeeze the
air out so the chip contacts the bag wall, and tape the neck above the waterline. Adds a
few seconds of lag but no error at steady state.

---

## Reference points

| Point | Value | Reliability |
|---|---|---|
| **Ice bath** | **0.00 °C** | ⭐ Essentially pressure-independent — trust this for offset |
| **Boiling water** | **98.5 °C** at 450 m | ±0.3 °C with the day's weather — use for span |

Your glass thermometer read 98 °C at boiling, so it sits ~0.5 °C low. Consistent with the
"within 0.5 °C" note in Session 1.

---

## Procedure

### Setup

1. Wire all sensors in parallel on **D2**, with the **4.7 kΩ pull-up between D2 and 5 V**.
   No sensors found = missing pull-up, nine times out of ten.
2. Upload `ds18b20_calibrate.ino`, open Serial Monitor at **9600 baud**.
3. **Record the address map** it prints at startup. Physically label each probe with its
   index — you need to know which correction belongs to which sensor later.
4. **Bundle all sensor tips together** — tips touching, bound with a twist tie or tape.
   They must be at the same temperature; any difference you then see is sensor error.

### Point 1 — ice bath (0.00 °C)

1. Fill a beaker with **crushed ice**, then add just enough cold water to fill the gaps.
   It must be a **slurry, mostly ice** — water with a few floating cubes is not 0 °C.
2. Bury the bundle in the middle, not touching the glass.
3. **Stir gently and continuously.**
4. Wait for readings to stabilise (2–3 min), then record **10 readings** per sensor.

### Point 2 — room temperature water *(optional but useful)*

Beaker of water at ambient, bundle immersed, stir, 10 readings. Gives you a mid-range
check on linearity.

### Point 3 — boiling water (98.5 °C)

1. Bring water to a **rolling boil** and keep it boiling.
2. Bundle immersed, **not touching the bottom or sides** — the vessel base is hotter
   than the water.
3. Wait for stability, record **10 readings** per sensor.

⚠️ Steam and boiling water. Tongs, and keep the Arduino well away from splashes.

---

## Working out the corrections

For each sensor, average its 10 readings at each point:

```
offset  =  0.00 − mean_ice
scale   =  (98.51 − 0.00) / (mean_boil − mean_ice)

corrected  =  (raw − mean_ice) × scale
```

Simpler and adequate if the scale comes out within about 1% of 1.000:

```
corrected  =  raw + offset
```

## What to expect

| Observation | Meaning |
|---|---|
| Offsets within ±0.5 °C | Normal — that's the factory spec |
| **Spread** column < 0.3 °C | Sensors agree well. Good |
| Spread > 1 °C | One sensor is off, or the bundle wasn't isothermal — re-run |
| Any sensor reading −127 | Disconnected or bad wiring |
| Scale factor far from 1.000 | Suspect the boiling reading — was the probe touching the base? |

---

## Why the `spread` column matters most

For the chamber, **sensor agreement matters more than absolute accuracy.** Your uniformity
measurement is control-sensor minus corner-sensor. If those two disagree by 0.8 °C when
sitting in the same ice bath, every gradient you measure afterwards carries that error.

Calibration removes it. Record the residual spread after correction — that's your stated
measurement uncertainty for the gradient.

---

## Record in the notebook

- Date, time, ambient temperature
- Address map (which physical probe = which index)
- Raw means at each point, per sensor
- Computed offset and scale, per sensor
- Residual spread after correction
- Assumed boiling point **98.5 °C at 450 m**, and that ice was a stirred slurry

This is the same two-point method you already used on the glass thermometer, so it is
consistent with what Session 1 documented.
