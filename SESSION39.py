# IMU Drift Correction Example


drift = 1.8 

imu_readings = [10.5, 15.2, 20.8, 25.3, 30.1]

corrected_readings = []

for angle in imu_readings:
    corrected_angle = angle - drift
    corrected_readings.append(corrected_angle)

print("Original IMU Readings:", imu_readings)
print("Corrected Readings:", corrected_readings)

print("\nOutput: Orientation Stabilized")
output:
Original IMU Readings: [10.5, 15.2, 20.8, 25.3, 30.1]
Corrected Readings: [8.7, 13.399999999999999, 19.0, 23.5, 28.3]

Output: Orientation Stabilized
