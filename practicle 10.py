# Function to find length using recursion
def find_length(lst):
    # Base case: if list is empty, return 0
    if lst == []:
        return 0
    else:
        # Recursive case: count 1 and call the function with rest of list
        return 1 + find_length(lst[1:])

# Input list from user
items = input("Enter elements separated by space: ").split()

# Call function and print result
length = find_length(items)
print("Length of the list is:", length)
