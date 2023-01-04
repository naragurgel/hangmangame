import random
from words import word_list

def choose_word():
    """
    Gets a random word from the list 'words' and converts the user input to uppercase to make easer the comparison logic
    """
    word = random.choice(word_list)
    return word.upper()

def start_game(word):
    """
    represent unguesses letters as underscores and show letter as correct guesses
    """
    word_completion = "_" * len(word)
    certain = False
    certain_letters = []
    certain_words = []
    attempts = 6
    print("Are you ready to play Hangman? Let's get started!")
    print(display_hangman(attempts))
    print(word_completion)
    print("\n")
    """
    the loops runs till the word is guessed or the users runs out of tries
    """
    while not certain and attempts > 0:
        try = input("Please guess a letter or word: ").upper()
        if len(try) == 1 and try.isalpha():

    elif len(try) == len(word) and try.isalpha():

    else:
        print("Not a valid guess.")
    print(display_hangman(attempts))
    print(word_completion)
    print("\n")




