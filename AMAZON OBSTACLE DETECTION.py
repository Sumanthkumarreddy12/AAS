depth_values = [0.8, 0.6, 0.4, 0.9, 0.3]

threshold = 0.5

for distance in depth_values:
    if distance < threshold:
        velocity = 0
        print("Obstacle Detected at", distance, "m")
        print("Robot Halted")
    else:
        velocity = 1
        print("Safe Distance:", distance, "m")
        print("Robot Moving")
      OUTPUT:
  Safe Distance: 0.8 m
Robot Moving
Safe Distance: 0.6 m
Robot Moving
Obstacle Detected at 0.4 m
Robot Halted
Safe Distance: 0.9 m
Robot Moving
Obstacle Detected at 0.3 m
Robot Halted
