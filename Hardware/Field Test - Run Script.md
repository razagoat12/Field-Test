# Field test — run script (H7 four-panel crossover)

Status: **draft, 2026-10-15**. Not ready to run.
Sources: Paper `Chapters 1-3 - Draft.md` §3.6 (field evaluation), §3.8 (calibration), §3.9.4 and §3.9.6 (analysis and pre-registered prediction).

Items marked **DECIDE** are not settled in the paper. Settle them and write the answer into this file before Day 1.

---

## 0. Blockers — do not start Day 1 until all are ticked

- [ ] **Logging path works.** The ESP32 → laptop Wi-Fi receiver and sketch are **not written or tested** (the write was declined). Build and test a full day indoors first. USB fallback: `serial_logger.py` on a laptop next to the stations, with a cable no longer than 5 m.
- [ ] **Ambient and clear-sky record.** §3.9.6 uses ambient temperature and irradiance. §3.6.2 requires a clear-sky criterion declared in advance. All four DS18B20s are used on the stations, so there is no ambient sensor. **DECIDE:** add a fifth DS18B20 in shade for ambient, and choose how clear days are judged (pyranometer reading, or a written visual rule).
- [ ] **Site.** §3.6 names Cadet College Hasanabdal. The rig is planned at home (roof or yard). **DECIDE** and correct the paper if the site changes.
- [ ] **Pre-registration.** Run `Data Analysis\pcm_panel_model.py` and save its output with today's date **before Day 1**. The prediction is: composite layer is **hotter** than bare by 5.3 °C at peak, so H7 is not met.
- [ ] **Timeline checked.** §3.6 needs 2 bare days, at least 5 clear crossover days, and 2 night logs. If Day 1 is 15 Oct and every day is clear, the earliest finish is about 22 Oct, after the paper deadline of 20 Oct 2026 (project notes). If that's the case, keep H7 as "untested" in `changes\limitations.md`.
- [ ] **Sensor calibration file.** Ice offsets and the 0.11 °C room check are in `changes\calibration.md`. Re-run the bench check (section 2, step 6) before going out.

---

## 1. Equipment (from §3.6.1)

- Four panels: the four closest of six IV-tested mono-crystalline panels (10–20 Wp each). Record panel ID, Wp, and mounting position.
- Four stations:
  - **A:** bare (no PCM)
  - **B:** sand thermal-mass control
  - **C:** composite
  - **D:** composite + graphite at the same thickness
- Four containers: 316 stainless, nominal 76 × 102 × 7.6 mm internal (≈ 59 cm³), filled to about **90 % (≈ 50 g)**.
- Graphite foil interface between container face and panel backsheet. **Confirm whether station B also gets foil.**
- **Identical insulating patch on every station, including A.**
- Four DS18B20 sensors, bonded at the **measured geometric centre** of the PCM-backed region. Use the ROM addresses from the calibration:
  - S0 `28BAC2B4000000E8`
  - S1 `2809627500000033`
  - S2 `28B5357300000084`
  - S3 `28DDDA76000000D2`
- Fifth DS18B20 for ambient (**DECIDE**, see section 0).
- Catch trays under stations C and D (§3.6.7).
- Balance readable to 0.01 g, and a dummy specimen with a sensor to check it reads ambient before each weighing (§3.3, §3.6).
- ESP32 with its power supply, and weatherproof enclosure (**DECIDE** type).

---

## 2. Setup (before the first bare day)

1. Mount all four panels at the **same orientation and tilt**. Record both.
2. Bond each sensor at its station's measured centre. Use the same bonding on A.
3. Fit the identical insulating patch to all four stations.
4. Write the **station table**: station, panel ID, ROM address, date. Keep one copy in the notebook.
5. Weigh each container **three times**, average, and record. Weigh the sealed control the same way.
6. **Bench check:** put all four sensors in one bath, wait until they settle, and confirm the corrected spread is about 0.1 °C. If it's over 0.5 °C, stop and fix before going out.
7. **Logging check:** run the receiver for at least 30 minutes with the ESP32 at the mount position. Confirm one row per sensor every 2 s and no −127 or 85.0 values.

---

## 3. Bare calibration days (2 days, required by §3.6.2)

1. All four panels bare (A configuration on every panel). Same insulation and sensor positions as the crossover.
2. Log continuously from sunrise to sunset.
3. Record the clear/cloudy decision for the day (section 5).
4. After both days, compute the per-panel correction ratios (analysis, not part of this script).

---

## 4. Crossover days (at least 5 clear days, §3.6.2)

Each day:
1. **Morning:**
   - Check power and Wi-Fi; the receiver should show rows arriving.
   - Check the catch trays. Photograph any leakage and date the photo.
   - Confirm the day's configuration table: which configuration is on which panel. **Swap configurations between panels daily** (§3.6.2).
   - Record the ROM address on each panel for the day. **DECIDE** how sensors rotate, so that sensor identity is not confounded with treatment.
2. **Logging:** log continuously. On at least **two nights**, keep logging past sunset through the night. Look for a freezing arrest near 43.8 °C on the way down. That is direct evidence of re-solidification.
3. **Evening:** copy the day's CSV to a second location. Note the weather and any events (shadow, rain, wind, disturbance).

---

## 5. Clear-sky rule (declared before the campaign)

- Write the rule here before Day 1: **DECIDE**.
- Each day gets one entry: `clear` or `excluded — reason`.
- **Never average cloudy days in.** Excluded days are reported with the reason (§3.9.4).

---

## 6. Weighing and leakage

- Weigh each container **before the first exposure** (done in section 2, step 5) and **after the last exposure**.
- Use the same method each time: three weighings, averaged, with the dummy check. Don't weigh anything warm.
- Photograph catch trays daily and date each photo.

---

## 7. End of campaign

1. Remove the panels and weigh each container again (three times, averaged). Weigh the sealed control again.
2. Photograph the trays.
3. **Drift check (recommended, not in the paper):** put the four sensors in the calibration bath again and compare with the offsets in `changes\calibration.md`. Record the result.
4. Back up every CSV to two locations, and list them in the notebook.

---

## 8. Failure rules

| What you see | What to do | Recorded how |
|---|---|---|
| −127 on one sensor | Reseat that sensor; note the time | Rows during the fault are excluded, not filled in (**DECIDE** if this is acceptable) |
| 85.0 on one sensor | Power-on value: check the red (VDD) wire | As above |
| Wi-Fi drop | Planned ESP32 buffer holds about 10 min of readings in RAM | Note the gap time |
| Laptop restarted | Restart the receiver | Note the gap time |
| Leakage on a tray | Photograph and date it | Note in notebook |

---

## 9. Analysis (for reference; not part of the field run)

- Paired differences within each day, after the per-panel correction ratios (§3.9.4).
- ΔT tracked daily, not averaged across the campaign.
- Compare the measured ΔT against the pre-registered prediction from section 0. Report agreement or departure as a finding, without adjusting the prediction (§3.9.5).

---

## 10. Log

Use this for each day: date, weather, clear/excluded, configuration table, sensor table, any faults, file names.
