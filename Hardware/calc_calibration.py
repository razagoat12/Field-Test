"""
DS18B20 calibration calculator.
Paste your measured means below, then run: python calc_calibration.py
"""

BOILING_POINT = 98.51   # deg C at 450 m
ICE_POINT     = 0.00

# ---- EDIT THIS: your measured means, one entry per sensor ----
# "label": (mean_ice, mean_boil)
data = {
    "S0": (0.31, 98.62),
    "S1": (-0.19, 98.05),
    "S2": (0.06, 98.44),
}
# --------------------------------------------------------------

print(f"{'sensor':>8} {'mean_ice':>9} {'mean_boil':>10} {'offset':>8} {'scale':>8}")
print("-" * 48)
offsets, scales, ices = {}, {}, []
for k, (mi, mb) in data.items():
    off = ICE_POINT - mi
    sc = (BOILING_POINT - ICE_POINT) / (mb - mi)
    offsets[k], scales[k] = off, sc
    ices.append(mi)
    print(f"{k:>8} {mi:>9.4f} {mb:>10.4f} {off:>+8.4f} {sc:>8.5f}")

raw_spread = max(ices) - min(ices)
corr = [(mi - mi) for mi in ices]          # after offset correction all -> 0
print()
print(f"Raw spread at ice point       : {raw_spread:.4f} C")
print(f"Residual spread after offset  : {max(corr)-min(corr):.4f} C")
print()

bad = [k for k, s in scales.items() if abs(s - 1.0) > 0.01]
if bad:
    print(f"NOTE: scale >1% from unity for {bad} - use the two-point form:")
    print("      corrected = (raw - mean_ice) * scale")
else:
    print("All scales within 1% of unity - simple offset correction is sufficient:")
    print("      corrected = raw + offset")
print()
print("Arduino code to paste into thermal_chamber.ino:")
print()
print("const float CAL_OFFSET[] = {" +
      ", ".join(f"{offsets[k]:+.4f}f" for k in data) + "};")
print("// then:  float t = sensors.getTempCByIndex(i) + CAL_OFFSET[i];")
