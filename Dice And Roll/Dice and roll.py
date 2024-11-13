import numpy as np
import time

print("Welcome to the Dice Game!")
print("Press Enter to roll the dice, or type 'end' to end the game.\n")

user_score = 0
computer_score = 0

while True:
    user_input = input("\nPress Enter to roll the dice or type 'end' to end the game: ").strip().lower()

    # Roll the dice for the user
    user_roll = np.random.randint(1, 7)
    print(f"\nYour roll: {user_roll}")
    time.sleep(1)

    # Roll the dice for the computer
    computer_roll = np.random.randint(1, 7)
    print(f"Computer's roll: {computer_roll}")

    # Update scores based on rolls
    user_score += user_roll
    computer_score += computer_roll

    # Special condition if either rolls a 6
    if user_roll == 6:
        print("You rolled a 6! You get an extra bonus!")
        computer_score = (computer_score - 6)  # Deduct points from computer

    if computer_roll == 6:
        print("Computer rolled a 6! It gets an extra bonus!")
        user_score = (user_score - 6)  # Deduct 6 points from user

    # Display current scores
    print(f"Current Score -> You: {user_score}, Computer: {computer_score}\n")
    
    # Check if any player has reached the winning score
    if user_score >= 100 or computer_score >= 100:
        print("\nThe game has reached the winning score limit!")
        if user_score >= 100 and user_score > computer_score:
            print("Congratulations, you won the game! 😍💕")
        elif computer_score >= 20 and computer_score > user_score:
            print("The computer wins! Better luck next time!")
        else:
            print("It's a tie!")
        break

print("\nThanks for playing!")
