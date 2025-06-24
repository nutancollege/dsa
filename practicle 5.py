# Program to count the occurrences of each word in a string

# Input string from user
sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase to count words without case sensitivity
sentence = sentence.lower()

# Split the sentence into words using space as separator
words = sentence.split()

# Create an empty dictionary to store word counts
word_freq = {}

# Loop through each word in the list
for word in words:
    # If word already in dictionary, increment its count
    if word in word_freq:
        word_freq[word] += 1
    else:
        # Otherwise, add the word to dictionary with count 1
        word_freq[word] = 1

# Display the word count
print("\nWord Frequencies:")
for word, count in word_freq.items():
    print(f"{word}: {count}")