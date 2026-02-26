sensors = {
    "Camera": 80,
    "Radar": 150,
    "LiDAR": 200
}

selected_sensor = max(sensors, key=sensors.get)

print("Sensor Ranges:", sensors)
print("Selected Sensor:", selected_sensor)
OUTPUT:
Sensor Ranges: {'Camera': 80, 'Radar': 150, 'LiDAR': 200}
Selected Sensor: LiDAR
