import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def print_result(user_choice, computer_choice, result):
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    print(f"Result: {result}")

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ("yes", "no"):
            return choice == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors game!")

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice not in ("rock", "paper", "scissors"):
            print("Invalid input. Please enter either 'rock', 'paper', or 'scissors'.")
            continue

        result = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"User score: {user_score}")
        print(f"Computer score: {computer_score}")

        if not play_again():
            print("Thanks for playing!")
            break

if _name_ == "_main_":
    main()
