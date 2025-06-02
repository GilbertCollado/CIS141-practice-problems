# Write a Python script that reads a file gardening_tips.txt and prints out each tip one by one.
with open("gardening_tips.txt", "r") as file:
    for tip in file:
        print(tip.strip())

