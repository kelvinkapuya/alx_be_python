#!/bin/bash

while True:
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose the operation (+, -, *, /): ")

    # Use match case to handle operations
    match operator:
        case "+":
            result = num1 + num2
            print("The result is", result)
        case "-":
            result = num1 - num2
            print("The result is", result)
        case "*":
            result = num1 * num2
            print("The result is", result)
        case "/":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                result = num1 / num2
                print("The result is", result)
        case _:
            print("Invalid operator. Please use +, -, *, or /.")

    # Ask the user if they want to execute the program again
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break

