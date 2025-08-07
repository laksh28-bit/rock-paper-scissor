import random

def game():
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Please enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice, please try again.")
            continue

        comp_choice = random.choice(choices)
        print("Computer choice:", comp_choice)

        if user_choice == comp_choice:
            print("Tie!")
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'scissors' and comp_choice == 'paper') or \
             (user_choice == 'paper' and comp_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Play again? yes/no: ").lower()
        if play_again == "yes":
            continue
        elif play_again == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Exiting game.")
            break

game()
