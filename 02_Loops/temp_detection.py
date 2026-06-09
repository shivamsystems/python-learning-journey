temperatures = [36.5, 37.0, 36.8, 39.5, 37.2, 38.0]
# Loop through them.
for t in temperatures:
# If any temperature is above 39.0, print "FEVER DETECTED: [temp]°C" and STOP checking.
    if t > 39:
        print(f"FEVER DETECTED: {t}°C")
        break
# If none are above 39.0, print "All normal".
else:
    print("All normal")

