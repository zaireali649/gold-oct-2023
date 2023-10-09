import random

number = random.randint(0, 10)  # Generate a random number between 0 and 10

count = 0  # Initialize a count variable to 0

while number != 7:
    if count >= 15:  # Check if the count exceeds 15
        break
    number = random.randint(0, 10)  # Generate a new random number
    count = count + 1  # Increment the count by 1 (count += 1)

print(count, number)  # Print the final count and number

numbers = [0, 1, 2, 3, 4]

for number in numbers:
    print(number*2)  # Print each number multiplied by 2

for i in range(10):
    print("Hello World From For Loop:", i)  # Print a message with the current value of i in the range
