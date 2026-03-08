# Distance readings from sensors (in meters)
left = 5
front = 2
right = 8

# Decision logic
if front < 3:
    if right > left:
        action = "Turn Right"
    else:
        action = "Turn Left"
else:
    action = "Move Forward"

print("Action:", action)
output:
Action: Turn Right
