import random

def main():
    # Generate the secret number at random
    secret_number = random.randint(1, 99) 
    
    print("I am thinking of a number between 1 and 99...")

    # Ask for the first guess
    guess = int(input("Enter a guess: "))

    # Keep asking until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Ask for a new guess
        print()  # This prints an empty line to make the output clear
        
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
    
    # If the guess is correct, congratulate the user
    print(f"Congrats 😊! The number was: {secret_number}")

if __name__ == '__main__':
    main()
