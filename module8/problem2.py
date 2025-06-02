# Write a Python program that allows users to log their hiking trips. The program should:
# - Use a while loop to repeatedly ask for a hike name and distance in miles
# - Save each entry to hiking_log.txt (each hike on a new line)
# - When the user presses 0, exit the loop & print the contents of hiking_log.txt

file = open("hiking_log.txt", "a")

while True:
    name = input("Enter hike name (0 to stop): ")
    if name == "0":
        break
    distance = input("Enter hike distance in miles: ")
    if distance == "0":
        break
    file.write(name + "\t" + distance + "\n")
file.close()

# Print log contents
file = open("hiking_log.txt", "r")
print("\nHiking Log:")
for line in file:
    print(line.strip())
file.close()
