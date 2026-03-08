# Node execution status
publisher_node = True
subscriber_node = True
communication = True

# Real-time check
if publisher_node and subscriber_node and communication:
    result = "Real-Time Achieved"
else:
    result = "Communication Delay"

print("Result:", result)
output:
 Real-Time Achieved
