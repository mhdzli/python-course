# import modules
from random import choice
from enum import IntEnum

# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

# a function to get user's choice and pruduce a random choice for computer (retry `retries` times if user don't give the proper option)
def get_Choices(retries=4, options = ["Rock", "Paper", "Scissors"], reminder = "Come on, just pick a valid option."):
    # random choice for computer
    computer_choice = choice(options)
    
    # get the user choice
    for i in range(retries):
        # get user input
        user_choice = input(f"Enter your choice \n 1 - {options[0]} \n 2 - {options[1]} \n 3 - {options[2]} \n")
        
        # check if the input is an integer
        try:
            user_choice = int(user_choice)
        except ValueError as e:
            print(e)
            print("You should choose the integer value of your chosen action.")
        # check if the input is in the options range
        else:
            if user_choice in range(1,4):
                # put user and computer choices in a dictionary
                choices = {"user": options[user_choice-1], "computer": computer_choice}
                break
            else:
                print("Choose an integer between 1, 2 and 3")
            if i == retries - 1:
                print(f"{reminder} \n {options}")
                raise ValueError('Invalid user choices')
    # return user and computer choices
    return(choices)

# a function to determine the winner
def check_winner(user, computer):
    # nested if statement
    if user == computer:
        return "It's a tie!"
    elif user == "Rock":
        if computer == "Scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif user == "Paper":
        if computer == "Rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif user == "Scissors":
        if computer == "Paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

# a function for asking if user wants to play again
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

while True:
    choices = get_Choices()
    resulte = check_winner(choices["user"],choices["computer"])
    print(resulte)
    play_again = ask_ok("Play again? (y/n): ",2)
    if not play_again:
        break