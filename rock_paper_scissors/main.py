# import modules
from random import choice


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


options = ["(Rock 🪨 )", "(Paper 🗞 )", "(Scissors ✂ )"]

# print multiline instruction
# performstring concatenation of string
print(bcolors.HEADER
      + f"Rules of the game {options[0]} {options[1]} {options[2]} are :\n"
      + bcolors.END
      + f"{options[0]} vs {options[2]} -> {options[0]} wins \n"
      + f"{options[1]} vs {options[0]} -> {options[1]} wins \n"
      + f"{options[2]} vs {options[1]} -> {options[2]} wins \n"
      )


# a function to get user's choice and pruduce a random choice for computer
# (retry `retries` times if user don't give the proper option)
def get_Choices(retries=4, reminder="Come on, just pick a valid option."):
    # random choice for computer
    computer_choice = choice(options)
    choices = None

    # get the user choice
    for i in range(retries):
        # get user input
        user_choice = input(bcolors.HEADER
                            + "Enter your choice: \n"
                            + bcolors.END
                            + f"1 - {options[0]}\n"
                            + f"2 - {options[1]}\n"
                            + f"3 - {options[2]}\n")

        # check if the input is an integer
        try:
            user_choice = int(user_choice)
        except ValueError as e:
            print(e)
            print(bcolors.YELLOW
                  + "You should choose the integer value"
                  + "of your chosen action."
                  + bcolors.END)
        # check if the input is in the options range
        else:
            if user_choice in range(1, 4):
                # put user and computer choices in a dictionary
                choices = {"user": options[user_choice-1],
                           "computer": computer_choice}
                break
            else:
                print(bcolors.YELLOW
                      + "Choose an integer between 1, 2 and 3"
                      + bcolors.END)
            if i == retries - 1:
                print(bcolors.RED + f"{reminder}\n" + bcolors.END
                      + "{options}")
                raise ValueError('Invalid user choices')
    # return user and computer choices
    return choices


# a function to determine the winner
def check_winner(user, computer):
    # nested if statement
    if user == computer:
        return bcolors.CYAN + "You both choose " + user + ". It's a tie! \
😐" + bcolors.END
    elif user == options[0]:
        if computer == options[2]:
            return bcolors.GREEN + f"{options[0]} smashes {options[2]}! \
You win! 😀" + bcolors.END
        else:
            return bcolors.RED + f"{options[1]} covers {options[0]}! \
You lose. 😞" + bcolors.END
    elif user == options[1]:
        if computer == options[0]:
            return bcolors.GREEN + f"{options[1]} covers {options[0]}! \
You win! 😀" + bcolors.END
        else:
            return bcolors.RED + f"{options[2]} cuts {options[1]}! \
You lose. 😞" + bcolors.END
    elif user == options[2]:
        if computer == options[1]:
            return bcolors.GREEN + f"{options[2]} cuts {options[1]}! \
You win! 😀" + bcolors.END
        else:
            return bcolors.RED + f"{options[0]} smashes {options[2]}! \
You lose. 😞" + bcolors.END


# a function for asking if user wants to play again
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(bcolors.HEADER + prompt + bcolors.END)
        if ok in ('y', 'ye', 'yes', ''):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(bcolors.YELLOW + reminder + bcolors.END)


while True:
    choices = get_Choices()
    if choices is not None:
        resulte = check_winner(choices["user"], choices["computer"])
        print(resulte)

    play_again = ask_ok("Play again? 🤔 (Y/n): ", 2)
    if not play_again:
        break
