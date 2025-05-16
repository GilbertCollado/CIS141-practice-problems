# Count how many numbers are positive and how many are negative
nums = [5, -2, 0, 13, -8, -1, 7]
positive_count = 0
negative_count = 0
for n in nums:
    if n > 0:
        positive_count += 1
    elif n < 0:
        negative_count += 1
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
