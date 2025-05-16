# Filter list to include only strings longer than three characters
words = ["sun", "sky", "ocean", "fish", "on", "star"]
filtered = []
for word in words:
    if len(word) > 3:
        filtered.append(word)
print("Strings longer than 3 characters:", filtered)
