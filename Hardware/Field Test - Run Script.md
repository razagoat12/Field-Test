# Field test — run script, as actually run

Rewritten **17 Oct 2026** to match what was done. The earlier draft planned 316-stainless
containers, a sand control, 10–20 Wp panels, two bare days, five crossover days, two
nights and a Hasanabdal site. None of that was used. The differences are listed in
section 7.

---

## 1. Site and setup

- **Site:** a roof in **Al Khobar, Saudi Arabia**, panels against a wall facing south.
- **Panels:** four frameless **mini mono-crystalline panels** of one model, **1 W, 3 × 5 in** (7.6 × 12.7 cm), not IV-matched.

- **Mounting (roof-integrated case):** each panel is taped to its own **2 cm thermocol
  board**. The board's bottom edge rests on a box and its top edge leans on the wall, so the
  board sets the tilt (≈ 35°). The back of every panel is insulated, which copies a
  roof-integrated (BIPV) module with no rear airflow.
- **Leads:** left **open-circuit**, each bare end taped separately so they cannot touch.
- **Catch paper** on the box under every panel.

## 2. Stations

| Sensor | ROM address | Station | Behind the panel |
|---|---|---|---|
| S3 | `28DDDA76000000D2` | **Bare** | nothing; panel on the board |
| S2 | `28B5357300000084` | **RBW alone** | 1 cm rice bran wax slab (thermal-mass control) |
| S1 | `2809627500000033` | **C40** | 1 cm slab, 40 wt % lauric acid / 60 wt % RBW |
| S0 | `28BAC2B4000000E8` | **C40 + graphite** | 1 cm C40 slab with 4 g graphite per 100 g (≈ 3.8 wt %) |

- Slabs are cast **14 × 7 × 1 cm** (measured after the test; earlier notes said ≈ 2 cm), notched round the lead joints and held
  between panel and board. **No container.**
- Each **sensor is taped to the panel's back, sandwiched between panel and slab** (bare panel:
  between panel and board), at the same measured spot on all four panels, on all three days.
  (Corrected 17 Oct; an earlier note said "just below the slab's lower edge".)
- Mapping confirmed by **finger test on 16 Oct**. Day 1's original file header had it wrong.

## 3. Each day

1. Start logging. Write the start time in the notebook (the calibration sketch has no clock).
   Day 1 started ≈ 13:30, Day 2 ≈ 11:47, Day 3 11:45 (ran to ≈ 18:50, past sunset).
2. Note the sky and wind every 30 min; photograph the sky hourly.
3. Note anything unusual with its time: a shadow, someone near a panel, a slab moving.
4. At the end: photograph every catch paper and slab. Copy the Serial Monitor transcript to
   `logs/` unchanged, and make a clean CSV beside it.

**Rotation:** whole stations (board, slab and panel together) move one spot along the row
each morning. Slabs stay on their own panel, so **panel and sensor bias are not balanced by
the rotation** and must come from a bare calibration run (section 4).

## 4. Bare calibration run

All slabs off, every panel bare on its board, same rig. Log for at least an hour in full
sun, moving every station one spot every 15 min and marking each move. Use
`field_station_logger/field_station_logger.ino` (type `m` + Enter after each move) or
`field_logger_pc.py --move-every 15`. **Status:** its log was not available for analysis; bias is bounded instead from the post-sunset convergence of the stations (`analysis/field_results.txt`).

## 5. Weighing

Weigh every slab before its first day and after its last (three weighings, averaged; never
weigh warm). On 16 Oct the **C40 + graphite slab partly collapsed and flowed**; it was left in
place for Day 3 and weighed broken afterwards. Results (kitchen scale, 1 g):
RBW 98 → 98 g (0 %), C40 96 → 94 g (2.1 %), C40 + graphite 100 → 89 g + fragments (11 %).

## 6. Data used for findings

- **Findings window: the first 90 min of each day.** On Day 2 a shadow crosses the row from
  ≈ 13:22, and on Day 3 the row loses sun from ≈ 14:45; everything after is kept, plotted and
  reported as a limitation.
- Weather comes from Open-Meteo (model data) for Al Khobar, interpolated to each reading.
- Analysis: `analysis/field_analysis.py`.

## 7. Planned versus done

| Planned (draft of 15 Oct) | Done |
|---|---|
| Site: Cadet College Hasanabdal | Roof in Al Khobar, Saudi Arabia |
| 4 matched 10–20 Wp panels | 4 mini panels, not IV-matched |
| 316 stainless containers + graphite foil | Free-standing 1 cm slabs, no container, no foil |
| Sand thermal-mass control | Rice bran wax slab |
| Sensor at the centre of the PCM-backed area | Sensor between panel and slab, same spot on all four |
| Treatments swapped between panels daily | Whole stations rotated; slabs stay on their panel |
| 2 all-bare days first | One bare calibration run (late afternoon) |
| ≥ 5 clear days + 2 nights | 3 slab days, from midday or afternoon; Day 3 past sunset; no pre-dawn |
| ESP32 over Wi-Fi | Arduino Uno over USB, Serial Monitor transcript |
| Ambient DS18B20 + clear-sky rule | Open-Meteo weather (model) + sky notes |
