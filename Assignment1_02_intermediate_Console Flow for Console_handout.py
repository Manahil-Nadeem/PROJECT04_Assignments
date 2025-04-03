import random

NUM_ROUNDS = 5  # Number of rounds to play

def main():
    score = 0  # To track the player's score
    
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    # Loop through each round
    for round_num in range(1, NUM_ROUNDS + 1):
        # Generate random numbers for the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Round {round_num}")
        print(f"Your number is {player_number}")
        
        # Get user's guess: whether they think their number is higher or lower
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        # Check if the guess is valid
        while guess not in ['higher', 'lower']:
            guess = input("Please enter either 'higher' or 'lower': ").lower()
        
        # Determine if the user's guess was correct
        if (guess == 'higher' and player_number > computer_number) or (guess == 'lower' and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increment the score if the guess was correct
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Print the current score
        print(f"Your score is now {score}\n")
    
    # Conditional ending messages based on score
    print("Thanks for playing!")
    print(f"Your final score is {score}")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()
