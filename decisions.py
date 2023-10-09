import random

number = random.randint(0,10)  # Generate a random number between 0 and 10
print(number)

if number > 6:
    print("Big number")

number = number + 1  # Increment the number by 1 (number += 1)
print(number)

thresh = 8  # Set the threshold value to 8

if number > thresh:
    print("Big number")
elif number < thresh:
    print("Small number")
else:  # The number is equal to the threshold (elif number == thresh)
    print("Number is", thresh)
