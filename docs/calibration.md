# Calibration write-up (§3.8, DS18B20 sensors)

Date: 2026-10-14. Status: calibration done for the 4 sensors; replacement §3.8 text below; the draft is not edited yet.

---

## Replacement text for §3.8

**3.8 Sensor calibration**

Temperature was logged with four DS18B20 digital sensors (12-bit, 0.0625 °C resolution, ±0.5 °C factory accuracy), read by an Arduino Uno and logged to a laptop over USB (Serial Monitor transcript). Each sensor was identified by its unique 64-bit ROM address and labelled S0–S3.

Calibration used a one-point offset against a stirred crushed-ice slurry, with the four sensor tips bundled together so that they shared one thermal environment. Each reference point was the mean of 10 consecutive readings taken after the readings had settled (range ≤0.125 °C over 10 readings). The offset for each sensor was the difference between the reference value and its mean reading.

The ice-bath sensor means were 1.61, 1.39, 1.86 and 1.37 °C, giving offsets of −1.61, −1.39, −1.86 and −1.37 °C, and a raw spread of 0.49 °C. The bath was above 0 °C, so the absolute offsets are biased. The calibration is therefore used only to compare the sensors with one another, not to report absolute temperatures.

As an independent check, the four sensors were held in room-temperature water (not used to set the offsets). Raw means were 29.98, 29.71, 30.13 and 29.74 °C (raw spread 0.41 °C). After applying the ice offsets, the corrected values were 28.38, 28.33, 28.26 and 28.38 °C, a corrected spread of 0.11 °C. This residual spread is the sensor-to-sensor uncertainty used in this study for comparisons between sensors. It was measured at one temperature only (about 28 °C after correction); agreement at the field temperatures (40–70 °C) was not checked.

---

## Numbers (source: Serial Monitor transcript, 2026-10-14)

Station on each sensor (finger test, 16 Oct 2026): **S0 composite + graphite, S1 C40 composite, S2 RBW alone, S3 bare.** The calibration is per sensor, so it is unaffected by which station a sensor is on.

| Sensor | ROM address | Ice mean (°C) | Ice offset (°C) | Room raw mean (°C) | Room corrected (°C) |
|---|---|---|---|---|---|
| S0 | 28BAC2B4000000E8 | 1.6062 | −1.6062 | 29.9813 | 28.3751 |
| S1 | 2809627500000033 | 1.3875 | −1.3875 | 29.7125 | 28.3250 |
| S2 | 28B5357300000084 | 1.8625 | −1.8625 | 30.1250 | 28.2625 |
| S3 | 28DDDA76000000D2 | 1.3687 | −1.3687 | 29.7437 | 28.3750 |

- Ice raw spread: 0.4937 °C.
- Room raw spread: 0.4125 °C. Room corrected spread: 0.1126 °C (reported as 0.11 °C).
- The earlier attempt at about 3 °C (sensors disagreed by 2.6 °C, and one bus dropout at −127) was not saved. Re-seating the wires removed the dropout and the large disagreement.

---

## What changed from the old draft, and why

| Old draft | Now | Why |
|---|---|---|
| Two-point ice + boiling (98.5 °C) | One-point ice offset, plus a room-temperature check | Only 4 sensors, and no boiling point was run |
| "Calibration not yet performed" warning | Calibration performed (Oct 2026) | It was done |
| 7 sensors | 4 sensors | Confirmed by the student |

---

## To-dos

- [x] **Save the raw data.** The stored ice and room captures are printed at the top of every logger transcript (`Hardware/logs/*_raw_serial.txt`, lines 9–12). A dedicated calibration CSV was not saved. Copy the full transcript into `Hardware\logs\` (or rerun with `serial_logger.py`) so that the paper's numbers can be traced to a file.
- [ ] **Replace §3.8 in `Paper\Chapters 1-3 - Draft.md`** with the text above. Not done yet.
- [ ] **Add a limitation:** agreement at 40–70 °C is untested. Either run the optional warm check (`w` in the sketch) or keep this limitation.
- [ ] **Add a limitation:** absolute temperatures are biased by the ice-bath offset (bath above 0 °C); only sensor-to-sensor comparisons are valid.
- [ ] **Check the ice bath temperature.** If you can get a true 0.00 °C reference later, repeat the ice point; the offsets would then be absolute.
- [ ] **Update `changes\methods.md`** line about the DS18B20 calibration: mark done and point here.
- [ ] **Keep the field spread check.** The corrected residual (0.11 °C) is the number to use for gradient uncertainty in §3.6.

---

## Sources and limits

- Sketch: `Hardware\ds18b20_calibration_test\ds18b20_calibration_test.ino` (one-point ice offset, held-out checks, EEPROM storage).
- Offsets and room check values are from the transcript above; they are not stored on disk yet (see first to-do).
- The room-temperature medium (water vs air) is not recorded in the transcript. Note it in the lab notebook.
