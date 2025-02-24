# These three are lists in python and they support indexing, slicing, and other list operations
name = ["Abel", "Abenezer"] # List containing two strings
numbers = [1, 2, 3] # List containing three integers
combo = ["Abel", 2, 3] # Combination of strings and integers

# Display the lists in the terminal
print(name)
print(numbers)
print(combo)
print(name + combo)

# Using For Loop. Print and iterate to each item in the combo list
for item in combo:
    print(item)

# Accessing a specific item on the 'numbers' list using index.
print (numbers[1])