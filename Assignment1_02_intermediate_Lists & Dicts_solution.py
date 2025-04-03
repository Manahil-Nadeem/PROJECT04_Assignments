def access_element(lst, index):
    """Access an element from the list by its index."""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    """Modify an element in the list at the specified index."""
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    """Return a slice of the list from start index to end index."""
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():
    """Simple index game that lets the user interact with a list."""
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)

    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

# Run the index game
index_game()
