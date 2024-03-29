import random, string
from hangman_dictionary import words

def select_word():
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word

def hangman():
    word = select_word()
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word) # letters in the word to be guessed
    used_letters = set() # set of letters that has been guessed
    lives = 7

    while len(word) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie H - N G - A -)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess an alphabet: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print ('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('Your letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that letter. Guess another letter!!!')

        else:
            print ('This is not a valid letter!!!')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

hangman()
