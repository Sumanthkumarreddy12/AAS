f = 600   # focal length
X = 1     # 3D X coordinate
Z = 2     # depth from camera

# Camera projection formula
u = (f * X) / Z

print("Projected pixel coordinate (u) =", u, "px")
output:
Projected pixel coordinate (u) = 300.0 px
