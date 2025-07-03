# Create a simple Python program to manage a shopping list. The program should:

# Start with a few items in a list.

# Allow the user to:

# View items

# Add new items

# Remove items

# Exit the program
import os

FILENAME = "shopping_list.txt"

# Load from file
def load_shopping_list():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save to file
def save_shopping_list(shopping_list):
    with open(FILENAME, "w") as file:
        for item in shopping_list:
            file.write(item + "\n")

shopping_list = load_shopping_list()

while True:
    print("\n---------- Shopping List -----------")
    for i, item in enumerate(sorted(shopping_list), start=1):
        print(f"{i}. {item}")

    print("\nOptions:")
    print("1. Add new item")
    print("2. Remove item")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        new_item = input("Enter item to add: ").strip().lower()
        if new_item in [item.lower() for item in shopping_list]:
            print(f"'{new_item}' is already in the list!")
        else:
            shopping_list.append(new_item)
            save_shopping_list(shopping_list)
            print(f"{new_item} added to list.")

    elif choice == "2":
        remove_item = input("Enter item to remove: ").strip().lower()
        found = False
        for item in shopping_list:
            if item.lower() == remove_item:
                shopping_list.remove(item)
                save_shopping_list(shopping_list)
                print(f"{item} removed from the list.")
                found = True
                break
        if not found:
            print("Item not found in list.")

    elif choice == "3":
        print("Goodbye!!")
        break

    else:
        print("Invalid option... Try again")
