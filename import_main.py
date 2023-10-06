# Import the 'random' module for generating random numbers
import random

# Import the 'os' module for interacting with the operating system
import os

# Import the 'hello_world' module (assuming it exists in the same directory)
import hello_world

# Import the 'whats_your_name' module (assuming it exists in the same directory)
import whats_your_name

# Define a variable 'var' with the string "Hello World From Main"
var = "Hello World From Main"

# Generate a random integer between 0 and 10 (inclusive) and store it in 'number'
number = random.randint(0, 10)

# Print the value of the 'var' variable
print(var)

# Print the special '__name__' variable, which is automatically set by Python
print(__name__)

# Print the random number stored in 'number'
print(number)

# Call the 'print_full_name' function from the 'whats_your_name' module
# with the arguments "Zaire" and "Ali"
whats_your_name.print_full_name("Zaire", "Ali")
