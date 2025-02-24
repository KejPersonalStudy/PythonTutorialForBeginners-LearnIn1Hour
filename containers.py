# These three are lists in python and they support indexing, slicing, and other list operations
from token import NUMBER


name = ["Abel", "Abenezer"] # List containing two strings
numbers = [1, 2, 3] # List containing three integers
combo = ["Abel", 2, 3] # Combination of strings and integers

# Add an integer '4' to the 'numbers' list
numbers.append(4)
print(numbers)

# Insert the integer '100' on the index '1' (second in this case)
numbers.insert(1,100)
print(numbers)

# Add multiple elements instead of one to the end of the list.
numbers.extend([300,400,25])
print(numbers)

# Reaarange the elements in the list in ascending order. 
numbers.sort()
print(numbers)

# Reaarange the elements in the list in descending order. 
numbers.reverse()
print(numbers)

# Delete the specific item on the list
numbers.remove(400)
print(numbers)
