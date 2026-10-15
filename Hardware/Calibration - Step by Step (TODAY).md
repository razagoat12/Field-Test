# DS18B20 calibration — complete step-by-step

Everything from bare parts to a table of correction numbers. ~1 hour.
No RTC needed — tomorrow's delivery does not block this.

---

## §0 On the bench before you start

- [ ] Arduino + USB cable
- [ ] DS18B20 sensors (all of them)
- [ ] **4.7 kΩ resistor** ← without this, nothing works
- [ ] Breadboard + jumper wires (or terminal blocks)
- [ ] Computer with Arduino IDE
- [ ] 2 beakers, crushed ice, kettle/burner, stirring rod, tongs
- [ ] Twist tie or tape (to bundle sensor tips)
- [ ] Notebook

---

## §1 Software setup

1. Open **Arduino IDE**
2. **Tools → Manage Libraries** (or Sketch → Include Library → Manage Libraries)
3. Search **`OneWire`** → install *OneWire by Paul Stoffregen*
4. Search **`DallasTemperature`** → install *DallasTemperature by Miles Burton*
5. Open `ds18b20_calibrate.ino`
6. **Tools → Board** → select your board (Uno/Nano/etc.)
7. **Tools → Port** → select the COM port that appears when the Arduino is plugged in

---

## §2 Wiring

### Identify the pins

**Bare TO-92 chip** — flat face toward you, pins pointing down:

```
   ___________
  |  DS18B20  |     left   = GND
  |___________|     middle = DATA (DQ)
     |  |  |        right  = VDD
    GND DQ VDD
```

**Waterproof probe** — usually **red = VDD, black = GND, yellow = DATA**.
⚠️ Colours vary by supplier. If unsure, check with the seller or a multimeter.

### Connect

All sensors go in **parallel** — same three rails:

```
Arduino 5V   ──┬──────────────── all VDD  (red)
               │
              4.7kΩ
               │
Arduino D2   ──┴──────────────── all DATA (yellow)

Arduino GND  ───────────────── all GND  (black)
```

The **4.7 kΩ sits between D2 and 5 V** — not in series with anything. This is the
single most common failure point.

---

## §3 First run — verify before you get anything wet

1. Upload the sketch
2. **Tools → Serial Monitor**, set baud to **9600** (bottom-right dropdown)
3. You should see:

```
# DS18B20 calibration
# sensors found: 3
# index 0 = 28FF4A2B04150312
# index 1 = 28AA1C3D05160421
# index 2 = 28BB7E4F06170533
elapsed_s,S0,S1,S2,mean,spread
2,26.8125,26.7500,26.8750,26.8125,0.1250
```

4. **Copy the address map into your notebook.** Physically label each probe
   `S0`, `S1`, `S2` with tape. You need to know which correction goes with which probe.

**If `sensors found: 0`** → see troubleshooting at the end.

---

## §4 Bundle the sensors

Bind all sensor **tips together**, touching, with a twist tie or tape.

This is the point of the whole exercise: if they're all at the same temperature, then
any difference in their readings is **sensor error**, which is exactly what you're
measuring.

⚠️ **Bare TO-92 chips cannot go in water** — the pins short. Seal each in a small plastic
bag, leads exiting the top, air squeezed out so the chip touches the bag wall, taped above
the waterline.

---

## §5 Ice bath — reference 0.00 °C

1. Fill a beaker with **crushed ice**, then add just enough cold water to fill the gaps.
   **Mostly ice, slurry consistency.** Water with cubes floating in it is *not* 0 °C.
2. Bury the sensor bundle in the middle — **not touching the glass**
3. **Stir gently and continuously**
4. Watch the Serial Monitor. Wait until readings stop drifting (2–3 min)
5. **Select 10 consecutive lines, copy, paste into a text file** named `ice.csv`

---

## §6 Room temperature *(optional, 2 min)*

Beaker of tap water at ambient, bundle immersed, stir, copy 10 lines → `room.csv`.
Gives a mid-range linearity check.

---

## §7 Boiling — reference 98.51 °C

1. Bring water to a **rolling boil**, keep it boiling
2. Immerse the bundle — **not touching the bottom or sides** (the base runs hotter
   than the water)
3. Wait for stability, copy 10 lines → `boil.csv`

⚠️ Tongs. Keep the Arduino away from splashes and steam.

---

## §8 Compute the corrections

Average each sensor's 10 readings at each point, then:

```
offset = 0.00 − mean_ice
scale  = 98.51 / (mean_boil − mean_ice)

corrected = (raw − mean_ice) × scale
```

If every scale lands within ~1% of 1.000, the simple version is fine:

```
corrected = raw + offset
```

Use `calc_calibration.py` in this folder — paste your means in and it does it.

### Worked example

| Sensor | mean_ice | mean_boil | offset | scale |
|---|---|---|---|---|
| S0 | +0.31 | 98.62 | −0.31 | 1.0026 |
| S1 | −0.19 | 98.05 | +0.19 | 1.0026 |
| S2 | +0.06 | 98.44 | −0.06 | 1.0021 |

Raw spread at ice: 0.50 °C. After correction: ~0.00 °C. **That 0.50 °C is the error you
just removed from every gradient measurement you'll make.**

---

## §9 Record in the notebook

- [ ] Date, time, ambient temperature
- [ ] Address map — which physical probe is which index
- [ ] Raw means at each point, per sensor
- [ ] Computed offset and scale, per sensor
- [ ] **Residual spread after correction** ← your stated measurement uncertainty
- [ ] Assumed boiling point **98.51 °C at 450 m**; ice was a stirred slurry

---

## Troubleshooting

| Symptom | Cause |
|---|---|
| `sensors found: 0` | **Missing 4.7 kΩ pull-up** (90% of cases). Or DATA on the wrong pin, or VDD/GND swapped |
| Some sensors found, not all | Bad joint on the parallel bus; check each VDD/GND/DATA |
| Reads **−127** | That sensor is disconnected mid-run |
| Reads **85.0** exactly | Power-on default — sensor powered but never completed a conversion. Check wiring |
| Readings jump around | Loose breadboard connection, or cable too long for the pull-up (try 2.2 kΩ) |
| Ice bath reads 2–4 °C | Not enough ice. Needs to be a slurry, and stirred |
| Boiling reads >100 °C | Probe touching the vessel base |
| Garbage characters in Serial Monitor | Baud rate not 9600 |
