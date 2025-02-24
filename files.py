# Some basic comments for the file
# a - append r - read w - write

# Open "Hello.txt" in read ("r") mode.
file = open("Hello.txt", "r")

# Read all the items in the text file per line and then display it
numbers = file.readlines()

# Iterate to each line and remove leading and trailing characters from a string
for number in numbers:
    print(number.strip())

# Close the file
file.close()
