import numpy as np

# Robot position
robot = np.array([0, 0])

# Goal position
goal = np.array([7, 0])

# Attractive force constant
k_att = 1

# Attractive force
F_att = k_att * (goal - robot)

# Resultant force magnitude
force = np.linalg.norm(F_att)

print("Force =", int(force))
output:
Force = 7
