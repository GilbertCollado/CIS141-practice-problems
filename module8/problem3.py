# Write a Python program that:
#- Reads the file
#- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
#- Counts how many times each word appears
#- Creates a dictionary of the words and their counts
#- Print the dictionary to the console
words_to_count = []
for i in range(5):
    word = input(f"Enter word {i+1} to count: ").lower()
    words_to_count.append(word)

# Read file and count words
file = open("song_lyrics.txt", "r")
text = file.read().lower()
file.close()

word_freq = {}
for word in words_to_count:
    count = text.count(word)
    word_freq[word] = count

print("Word Frequencies:", word_freq)
