# Distance from wall (in meters)
wall_distance = 1

# Safe distance threshold
safe_distance = 2

# Decision logic
if wall_distance < safe_distance:
    action = "Move Away"
else:
    action = "Follow Wall"

print("Action:", action)
output:
Action: Move Away
