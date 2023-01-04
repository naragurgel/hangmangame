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
            if try in certain_letters:
                print("You alredy guessed the letter", try)
            elif guess not in word:
                print(try, "is not in the word.")
                attempts -= 1
                certain_letters.append(try)
            else:
                print("Well done,", try, "is in the word!")
                certain_letters.append(try)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == try]
                for index in indices:
                    word_as_list[index] = try
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    certain = True

    elif len(try) == len(word) and try.isalpha():

    else:
        print("Not a valid guess.")
    print(display_hangman(attempts))
    print(word_completion)
    print("\n")




