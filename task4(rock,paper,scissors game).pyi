#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

    import random  # Import random for computer's choice

def rock_paper_scissors_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    print("Type 'exit' to quit the game.\n")

    # Initialize scores
    user_score = 0
    computer_score = 0

    # Game loop
    while True:
        # Get user input
        user_choice = input("Enter your move (rock, paper, scissors): ").lower()
        if user_choice == 'exit':  # Exit condition
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please try again.")
            continue

        # Computer's random choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"The computer chose: {computer_choice}")

        # Determine the winner using a dictionary for win conditions
        win_conditions = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

        if user_choice == computer_choice:
            print("It's a tie!")
        elif win_conditions[user_choice] == computer_choice:
            print("You win this round!")
            user_score += 1
        else:
            print("The computer wins this round.")
            computer_score += 1

        # Display scores
        print(f"Scores: You - {user_score}, Computer - {computer_score}\n")

    # Game summary
    print("\nGame Over!")
    print(f"Final Scores: You - {user_score}, Computer - {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif user_score < computer_score:
        print("Better luck next time! The computer wins.")
    else:
        print("It's a draw!")

# Run the game
rock_paper_scissors_game()
