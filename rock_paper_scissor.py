import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor: ")
    opponent = random.choice(['r', 'p', 's'])

    if user == opponent:
        return f"It is a tie!!! You chose: {user} and your opponent chose: {opponent}"

    elif is_win(user, opponent):
        return f"Yay, you won!!! You chose: {user} and your opponent chose: {opponent}"

    else:
        return f"Oh oh!!! You lost!!! You chose: {user} and your opponent chose: {opponent}"

def is_win(choice_1, choice_2):
    if (choice_1 == 'r' and choice_2 == 's') or (choice_1 == 's' and choice_2 == 'p') or (choice_1 == 'p' and choice_2 == 'r'):
        return True

print (play())