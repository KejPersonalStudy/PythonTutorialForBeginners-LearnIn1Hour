# Ask user for age and tell them their in five years

# Store the input of the user in 'age'. The input is datatype of String.
age = input("Enter your age: ")

# Cast the age(DataType: String) to an Integer then add 5 to it.
# The variable name is also a multi-word and Python uses 'snake_case'
age_in_five_years = int(age) + 5

# Convert the integer 'age_infive_years') back to string, combine it with the rest of the string, then display the result.
print("You will be " + str(age_in_five_years) + " years old in five years.")
