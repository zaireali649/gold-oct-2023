import random

var = {}  # Create an empty dictionary and assign it to the variable 'var'
print(var)  # Print the contents of 'var'
print(type(var))  # Print the type of 'var'

var2 = {"juice": "cranberry", "movie": "The Lion King (1991)", "fruit": "mango"}  # Create a dictionary 'var2' with key-value pairs
print(var2)

print(var2["juice"])  # Print the value associated with the key "juice" in 'var2'

var2["drank"] = "Patron"  # Add a new key-value pair "drank": "Patron" to 'var2'
print(var2)

var2["movie"] = "Scarface"  # Update the value associated with the key "movie" in 'var2'
print(var2)

del var2["drank"]  # Delete the key-value pair with the key "drank" from 'var2'
print(var2)

print(dir(var2))  # Print the list of attributes and methods available for 'var2'

print(list(var2.keys()))  # Print a list of all keys in 'var2'
print(list(var2.values()))  # Print a list of all values in 'var2'
print(list(var2.items()))  # Print a list of all key-value pairs in 'var2'

for k, v in var2.items():
    print(k, v)  # Print each key-value pair in 'var2' as separate items
    
dict_of_lists = {
    "000": [random.randint(0, 10) for i in range(0, 3)], 
    "001": [random.randint(0, 10) for i in range(0, 3)], 
    "002": [random.randint(0, 10) for i in range(0, 3)]
}  # Create a dictionary of lists with random integers
print(dict_of_lists)

for k, v in dict_of_lists.items():
    print(k, v)  # Print each key and its corresponding list in 'dict_of_lists'
    for element in v:
        print(element)  # Print each element in the sub-list associated with the key

dict_of_dict = {
    "000": {"1000": "String"},  # Create a dictionary of dictionaries with a nested dictionary for key "000"
    "001": {"1001": "String"},  # Create another nested dictionary for key "001"
    "002": {"1002": "String"}   # Create another nested dictionary for key "002"
}

print(dict_of_dict["000"]["1000"])  # Print the value associated with key "1000" in the nested dictionary under key "000"
