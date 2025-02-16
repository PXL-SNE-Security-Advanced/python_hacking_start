# Simulate the state of a port
port_open = False
port_filtered = True

# Check the state of the port and print the corresponding message
if port_open:
    print("Port is open")
elif port_filtered:
    print("Port is filtered")
else:
    print("Port is closed")
    
    