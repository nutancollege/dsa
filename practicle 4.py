# Input list of words
words = input("Enter words separated by space: ").split()

# Input the word to remove and its occurrence
target = input("Enter the word to remove: ")
occurrence = int(input("Enter the occurrence to remove (1 for first, 2 for second, etc.): "))

# Initialize counter
count = 0

# Loop to find and remove the ith occurrence
for i in range(len(words)):
    if words[i] == target:
        count += 1
        if count == occurrence:
            words.pop(i)
            break

# Output the list after removal
print("List after removing", occurrence, "occurrence of", target, ":", words)
