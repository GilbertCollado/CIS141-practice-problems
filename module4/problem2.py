# Check sensor value for automatic headlights
sensor = int(input("Enter daylight sensor reading: "))

if sensor < 8:
    print("Headlights On")
else:
    print("Headlights Off")
