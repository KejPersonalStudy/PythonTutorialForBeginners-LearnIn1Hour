# Some basic comments for the file
# a - append r - read w - write

# Open "Hello.txt" in read ("r") mode.
file = open("Hello.txt", "r")

# Read all the items in the text file per line and then display it
numbers = file.readlines()

sum = 0

# Iterate to each line and remove leading and trailing characters from a string
# Convert the string into integer and summate all the numbers in a single variable
for number in numbers:
    sum = sum + int(number.strip())

# Display the total 
print (sum)

# Close the file
file.close()
