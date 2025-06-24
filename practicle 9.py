# Input sentence from user
sentence = input("Enter a sentence: ")

# Convert sentence to lowercase (optional)
sentence = sentence.lower()

# Split the sentence into words
words = sentence.split()

# Create empty dictionary
char_dict = {}

# Loop through each word
for word in words:
    # Get the first character
    first_char = word[0]

    # If the character is already a key, append the word to its list
    if first_char in char_dict:
        char_dict[first_char].append(word)
    else:
        # If not, create a new list with the word
        char_dict[first_char] = [word]

# Print the dictionary
print("\nDictionary:")
for char, word_list in char_dict.items():
    print(f"{char}: {word_list}")