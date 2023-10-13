import random

var = []  # Create an empty list and assign it to the variable 'var'
print(var)  # Print the contents of 'var'
print(type(var))  # Print the type of 'var'

var2 = [151, 251, 386, 493, 649, "009"]  # Create a list 'var2' with various elements
print(var2)

var2.append(721)  # Append the value 721 to 'var2' (in-place modification)
print(var2)

var2 = var2 + [1008]  # Concatenate 'var2' with another list containing 1008 and reassign to 'var2'
print(var2)

print(dir(var2))  # Print the list of attributes and methods available for 'var2'

var2.reverse()  # Reverse the order of elements in 'var2'
print(var2)

print(dir("This is a string"))  # Print the list of attributes and methods available for a string

numbers = [0, 1, 2, 3, 4]  # Create a list of numbers
print(numbers)

numbers = range(0, 10)  # Create a range object and assign it to 'numbers'
print(type(numbers))

numbers = list(numbers)  # Convert the range object to a list
numbers = list(range(0, 10))  # Alternatively, create a list directly from a range
print(type(numbers))
print(numbers)

for number in numbers:
    print(number*2)  # Print each number multiplied by 2

print(dir(random))  # Print the list of attributes and methods available for the 'random' module

letters = [random.choice(["A", "B", "C"]) for i in range(0, 5)]  # Generate a list of random letters
print(letters)

for letter in letters:
    print(letter.lower())  # Print each letter converted to lowercase

sq_numbers = [0, 1, 4, 9, 16]  # Create a list of square numbers
print(sq_numbers)

print(sq_numbers[2])  # Print the element at index 2 (zero-based index) Also dangerous

print(sq_numbers.index(9))  # Print the index of the value 9 in 'sq_numbers'

try:
    print(sq_numbers.index(10))  # Try to find the index of 10 in 'sq_numbers' (will raise an exception)
except:
    print("not in list")  # Print a message since 10 is not in 'sq_numbers'

print(len(sq_numbers))  # Print the length of 'sq_numbers'

list_of_lists = [[random.randint(0,10) for j in range(0, 3)] for i in range(0, 5)]  # Create a list of lists with random integers
print(list_of_lists)

for list_of_list in list_of_lists:
    print(list_of_list)  # Print each sub-list
    for element in list_of_list:
        print(element)  # Print each element in the sub-list
