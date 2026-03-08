import pandas as pd

# Example sensor values (simulated from turbofan dataset)
sensor_values = [60, 55, 58, 57, 50]

# Calculate average health value
health = sum(sensor_values) / len(sensor_values)

print("Health =", int(health))
output:
Health = 56
