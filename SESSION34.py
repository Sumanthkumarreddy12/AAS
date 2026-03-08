# Simulated keyboard input
key = 'a'   # 'a' represents left turn

# Decision logic
if key == 'w':
    action = "Move Forward"
elif key == 's':
    action = "Move Backward"
elif key == 'a':
    action = "Left Turn"
elif key == 'd':
    action = "Right Turn"
else:
    action = "Stop"

print("Action:", action)
output:
Action: Left Turn
