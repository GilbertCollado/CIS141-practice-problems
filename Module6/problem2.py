# Count how many times "Olympic" appears in a list
words = ["Olympic", "Games", "College", "Olympic", "Track", "Olympic"]
count = 0
for word in words:
    if word == "Olympic":
        count += 1
print("Olympic appears", count, "times")
