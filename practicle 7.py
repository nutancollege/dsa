# Input keys
keys = input("Enter keys separated by space: ").split()

# Input values
values = input("Enter values separated by space: ").split()

# Convert both to lists
# (Optionally: cast to int if needed)
if len(keys) != len(values):
    print("Error: Number of keys and values must be the same.")
else:
    # Create dictionary using zip()
    result_dict = dict(zip(keys, values))
    print("Mapped dictionary:", result_dict)
