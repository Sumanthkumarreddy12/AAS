# Localization Example

# Expected position (from map)
expected_position = (5, 5)

# Detected position (from sensors)
detected_position = (5, 5)

# Check localization accuracy
if expected_position == detected_position:
    result = "Accurate Localization"
else:
    result = "Localization Error"

print("Result:", result)
output:
Accurate Localization
