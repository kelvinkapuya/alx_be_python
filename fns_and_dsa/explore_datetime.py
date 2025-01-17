#!/bin/bash

from datetime import datetime, timedelta  # Import the datetime module

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current date and time: {formatted_date}")
    return formatted_date  # Return the formatted date and time

def calculate_future_date():
    """
    Calculates a future date by adding a user-specified number of days to the current date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=days_to_add)  # Calculate future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        print(f"Future date: {formatted_future_date}")
        return formatted_future_date  # Return the formatted future date
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
        return None

def main():
    """
    Main function to execute the script functionality.
    """
    print("Welcome to the Date and Time Explorer!")
    display_current_datetime()  # Display the current date and time
    calculate_future_date()  # Calculate and display the future date

if __name__ == "__main__":
    main()
