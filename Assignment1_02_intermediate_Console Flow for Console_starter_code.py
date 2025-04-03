import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    # Initialize the score
    your_score = 0
    
    # Play multiple rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers for the player and the computer
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is {your_num}")
        
        # Ask the player if they think their number is higher or lower than the computer's
        choice = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        # Validate input (ensure it's either 'higher' or 'lower')
        while choice not in ['higher', 'lower']:
            choice = input("Please enter either 'higher' or 'lower': ").strip().lower()
        
        # Evaluate if the player's guess is correct
        if (choice == 'higher' and your_num > computer_num) or (choice == 'lower' and your_num < computer_num):
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        # Display the player's score after each round
        print(f"Your score is now {your_score}")
        print()
    
    # After all rounds, display the final score and feedback
    print("Thanks for playing!")
    print(f"Your final score is {your_score}")
    
    # Provide feedback based on the score
    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
