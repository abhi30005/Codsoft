import random

# Computer choose
def computer_turn():
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)

# Choose winner
def choose_winner(user_move, computer_move):
    if user_move == computer_move:
        return 'tie'
    # Rock beats scissors, scissors beat paper, and paper beats rock
    elif (user_move == 'rock' and computer_move == 'scissors') or \
            (user_move == 'scissors' and computer_move == 'paper') or \
            (user_move == 'paper' and computer_move == 'rock'):
        return 'computer'
    else:
        return 'user'


user = 0
comp= 0

def score(winner):
    global user, comp
    if winner == 'user':
        user += 1
    elif winner == 'computer':
        comp += 1

def play_game():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = input("Enter your choose: ")

    if user_choice not in ['1', '2', '3']:
        print("Invalid input...!!")
        return play_game()

    user_move = ['rock', 'paper', 'scissors'][int(user_choice) - 1]
    computer_move = computer_turn()

    print(f"\nYou choose: {user_move}")
    print(f"Computer choose: {computer_move}\n")

    winner = choose_winner(user_move, computer_move)
    if winner == 'tie':
        print("It's  tie...!!")
    elif winner == 'user':
        print("You win...!!")
    else:
        print("Computer wins...!!")

    score(winner)
    print(f"Score - You: {user}, Computer: {comp}")

    play_again = input("\nDo you want to play again..? (Y/N): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thank You..!!")

play_game()