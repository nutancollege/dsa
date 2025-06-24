text = input("Enter a sentence: ")

print("You entered:", text)  # Debug print

words = text.split()
print("Words after split:", words)  # Debug print

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word frequencies:")
for word in freq:
    print(word, ":", freq[word])
