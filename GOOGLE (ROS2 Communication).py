class Twist:
    def __init__(self, linear_x=0.0, angular_z=0.0):
        self.linear_x = linear_x
        self.angular_z = angular_z


# Publisher Node
def publish_twist():
    # Create movement command
    msg = Twist(linear_x=1.0, angular_z=0.5)
    print("Publishing Twist Message...")
    print("Linear Velocity:", msg.linear_x)
    print("Angular Velocity:", msg.angular_z)
    
    return msg


# Subscriber Node
def subscribe_twist(msg):
    print("\nSubscriber Received Message")
    
    if msg.linear_x > 0:
        print("Robot Moving Forward")
        
    if msg.angular_z > 0:
        print("Robot Rotating")


# Main execution
twist_message = publish_twist()
subscribe_twist(twist_message)
