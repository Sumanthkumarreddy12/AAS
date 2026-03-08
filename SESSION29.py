# Hybrid Energy Battery Mode Detection

# Example battery values
battery_level = 35   # percentage
temperature = 30     # degree Celsius

# Decision logic
if battery_level < 40:
    mode = "Charging Mode"
else:
    mode = "Discharging Mode"

print("Battery Status:", mode)
output:
Battery Status: Charging Mode
