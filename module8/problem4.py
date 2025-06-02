# Write a program that reads the poll.txt file Count how many votes "yea" or "nay" received and print the results.
with open("poll.txt", "w") as file:
    file.write("yea,nay,yea,nay,yea,nay,yea")

# Read and count votes
with open("poll.txt", "r") as file:
    content = file.read().strip().lower()
    votes = content.split(",")

yea_count = votes.count("yea")
nay_count = votes.count("nay")

print("Yea votes:", yea_count)
print("Nay votes:", nay_count)
