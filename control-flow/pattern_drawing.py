#!/bin/bash

size = int(input("Enter the size of the pattern: ")) # Prompt the user for the pattern size

while size <= 0: # Validate the input to ensure it's a positive integer
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks for each column in the row
    for _ in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Increment the row counter
    row += 1
