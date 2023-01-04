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
            elif try not in word:
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
            if try in certain_words:
                print("You alredy guessed the word", guess)
            elif try != word:
                print(try, "is not the word.")
                attempts -= 1
                certain_words.append(try)
            else:
                certain = True
                word_completion = word


        else:
            print("Not a valid guess.")
        print(display_hangman(attempts))
        print(word_completion)
        print("\n")

    if certain:
        print("God job, you guessed the word! You win!")

    else:
        print("Unfortunately, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = choose_word()
    start_game(word)
    while input("Play Again? (Y/N)A "). upper() == "Y":
        word = choose_word()
        start_game(word)

if __name__ == "__main__":
    main()