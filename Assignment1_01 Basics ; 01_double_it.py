def main():
    # Prompt the user to enter a number
    curr_value = int(input("Enter a number: "))  # Convert the user input to an integer

    # While the current value is less than 100, double it and print the result
    while curr_value < 100:
        curr_value = curr_value * 2 # Double the value
        print(curr_value, end=" ")  
# Run the program 
if __name__ == '__main__':
    main()