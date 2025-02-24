# These three are lists in python and they support indexing, slicing, and other list operations
name = ["Abel", "Abenezer"] # List containing two strings
numbers = [1, 2, 3] # List containing three integers
combo = ["Abel", 2, 3] # Combination of strings and integers

# This is an example of a dictionary, which is a collection of key-value pairs. 'One', 'Two'... are keys and '1', '2'... are values
# Each key are unique and each key maps to a single value
alphaNum = {
    "One": 1,
    "Two": 2,
    "Three": 3
}

# This will replace '1' with 'A' (the first part of the list)
# The 'numbers' list will now became a combination of strings and integers
numbers[0] = "A"
print(numbers)

# By defauly, using a 'for' loop on a dictionary will iterate or loop through the keys.
for items in alphaNum:
    print(items)
