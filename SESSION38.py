# Package status
package_picked = True
destination_reached = True

# Delivery check
if package_picked and destination_reached:
    status = "Delivered"
else:
    status = "Pending"

print("Package Status:", status)
output:
Package Status: Delivered
