import random

def user_guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess the number: '))
        if guess > random_number:
            print ("Sorry your guess is too high!!!")
        elif guess < random_number:
            print ("Sorry your guess is too low!!!")
    
    print (f"Yay, congrats!!! You have guessed the number {random_number} correctly :)")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"My guess is: {guess} Is guess is too high(H), too low(L), or correct(C)? ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print (f"Yay, the computer guessed the number, {guess}, correctly")


# user_guess(10)
computer_guess (350)