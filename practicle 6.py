# Input main string
main_str = input("Enter the main string: ")

# Input substring
sub_str = input("Enter the substring to check: ")

# Check presence
if sub_str in main_str:
    print("Yes, substring is present.")
else:
    print("No, substring is not present.")
