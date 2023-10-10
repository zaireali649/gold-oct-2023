#!/bin/python3

import math
import os
import random
import re
import sys

# Check if the script is being run as the main program
if __name__ == '__main__':
    n = int(input().strip())  # Read an integer input
    
    if (n % 2) != 0:
        print("Weird")  # If n is odd, print "Weird"
    elif n >= 2 and n <= 5:  # If n is even and in the range [2, 5], print "Not Weird"
        print("Not Weird")
    elif n >= 6 and n <= 20:  # If n is even and in the range [6, 20], print "Weird"
        print("Weird")
    elif n >= 21:  # If n is even and greater than or equal to 21, print "Not Weird"
        print("Not Weird")
