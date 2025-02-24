# Guessing game

# Store the number to be guessed by the user. Ideally, it should be random
secret_number = 4
# Initialize the guess variable to be used in the 'while' loop
# Use '-1', so it is outside the guess range of (0 to 10)
guess = -1;

# Greet the user about the title and game mechanics
print("Guessing Game")
print("Hello, Mortal. I have a number in mind, can you guess it ranges from 0 to 10?")

# This while loop has an infinite condition 'guess!= secret_number'. It will continue running until a break condition is met or externally stopped.
# Ask the user to guess the 'secret_number' and prompt the user if its guess is high or low.
while guess!= secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Guess too low")
    elif guess > secret_number:
        print("Guess too high")
    else:
        print("Congrats, you have won")
        
        