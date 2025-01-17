#!/bin/bash

def display_menu():
    """
    Displays the menu for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function for the shopping list manager.
    """
    shopping_list = []  # Initializes an empty shopping list

    while True:
        display_menu()  # Display menu options
        try:
            # Accept user input as a number
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                # Adding an item
                item = input("Enter the item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"'{item}' has been added to the shopping list.")
                else:
                    print("Error: Item name cannot be empty.")

            elif choice == 2:
                # Removing an item
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the shopping list.")
                else:
                    print(f"'{item}' not found in the shopping list.")

            elif choice == 3:
                # Viewing the list
                if shopping_list:
                    print("\nCurrent Shopping List:")
                    for i, item in enumerate(shopping_list, 1):
                        print(f"{i}. {item}")
                else:
                    print("\nThe shopping list is empty.")

            elif choice == 4:
                # Exiting the program
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number between 1 and 4.")

        except ValueError:
            print("Error: Please enter a valid number for your choice.")

if __name__ == "__main__":
    main()

