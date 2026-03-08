# Simulated line position from camera
line_position = "left"

# Decision logic
if line_position == "left":
    action = "Turn Left"
elif line_position == "right":
    action = "Turn Right"
else:
    action = "Move Forward"

print("Action:", action)
output:
 Turn Left
