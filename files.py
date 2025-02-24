# Some basic comments for the file
# a - append r - read w - write

# Open "Hello.txt" in write ("w") mode. If the file doesn't exist, Python will create one. If it exist, it will be overwritten.
# For now, the file will be at the root.
file = open("Hello.txt", "w")

# Write Hello World on the text file
file.write("Hello World")

# Close the file
file.close()
