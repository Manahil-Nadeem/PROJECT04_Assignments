def access_element(lst, index):
    """Access an element from the list by its index."""
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    """Modify an element in the list at the specified index."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    """Return a slice of the list from start index to end index."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    else:
        return "Invalid indices."

def game():
    # Initialize a list with 5 elements
    elements = ['apple', 'banana', 'orange', 100, 5.6]
    
    while True:
        print("\nCurrent List:", elements)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter the number of the operation: ")

        if choice == '1':
            # Access element
            index = int(input("Enter the index to access: "))
            print("Element at index", index, ":", access_element(elements, index))
        elif choice == '2':
            # Modify element
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            # Check if new value is a number
            if new_value.isdigit():
                new_value = int(new_value)
            else:
                try:
                    new_value = float(new_value)
                except ValueError:
                    pass
            print("Updated List:", modify_element(elements, index, new_value))
        elif choice == '3':
            # Slice list
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print("Sliced List:", slice_list(elements, start, end))
        elif choice == '4':
            # Exit the game
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    game()
