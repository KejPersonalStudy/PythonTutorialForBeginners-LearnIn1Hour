# Create a class named 'Animal'
class Animal:
    # Implemented a constructor and assign the name to the instance
    def __init__(self, name):
        self.name = name
    # Self represents the instance calling this method

    # Instance methods for the Animal Class...
    def eat(self):
        print("Eating...")
    def breathe(self):
        print("Breathing...")

# Define a 'Dog' Class that inherits from the Animal Class
class Dog(Animal):
    def sound(self):
        print("Barking...")

# Define a 'Cat' Class that inherits from the Animal Class
class Cat(Animal):
    def sound(self):
        print("Meow...")

# Create an instance of a dogm, store it in labradodle, and call the method from the Animal Class and the Dog Class
labradodle = Dog("Labradodle")
labradodle.eat()
labradodle.sound()

# Similar to the Above code.
persian_cat = Cat("Persian Cat")
persian_cat.sound()
persian_cat.breathe()