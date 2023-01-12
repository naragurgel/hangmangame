import random
import string
from words import word_list
from stages import STAGES
import pyfiglet
import os
from time import sleep


def retrieve_yes_no_response(input_value):
    """
    Outputs a boolean value based on the user response (Y/N)
    """
    response = get_user_input(input_value)
    if response == "Y":
        return True
    elif response == 'N':
        return False
    else:
        print('Invalid input. Please try again.')
        retrieve_yes_no_response(input_value)


def get_user_input(input_value):
    """
    Retrieve user input in uppercase and stripped

    """
    response = input(input_value)
    return response.upper().strip()


def username():
    """
    Retrieve username and print greeting in the screen
    """
    name = input('Enter your name: \n')
    print(f"Hey, {name}! Let's Play.")


def display_goodbye():
    """
    Print goodbye in the screen
    """
    print(pyfiglet.figlet_format('Thank you, good bye!'))


class HangmanGame:
    """
    Data Model for Hangman Game

    *
    Attributes
    ----------
    word: str
        random word user is trying to guess in 6 attempts
    word_completion: str
        display of word with blanks for user's guesses
    certain: Boolean
        tracks if user has guessed current word or not
    guessed_letters: array of str
        tracks letters user has guessed
    guessed_words: array of strings
        tracks words user has guessed
    attempts: int
        count down of attempts untl user looses game
    """

    def __init__(self, word):
        """
        Initialize method, it starts the class off with default parameters.
        as if a user just started to play a game.
        """
        self.word = word.upper()
        self.word_displayed = [x for x in "*" * len(word)]
        self.game_completed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.attempts = 6
        self.available_letters = set(string.ascii_uppercase)

    def run_game(self):
        """
        Run the game until the user ran out of tries or won the game
        """
        print("\33[34mLet's get started!\33[m")
        self.display_hangman()
        # the loops runs till the word is guessed
        # or the users runs out of guessed_letter
        while not self.game_completed and self.attempts > 0:
            guess = get_user_input("Please guess a letter or word: \n")
            if len(guess) == 1 and guess.isalpha():
                self.resolve_guessed_letter(guess)

            elif len(guess) == len(self.word) and guess.isalpha():
                self.resolve_guessed_word(guess)
            else:
                print("\33[41mNot a valid guess.\33[m")
            self.display_hangman()

        if self.game_completed:
            print("\33[32mGod job, you guessed the word! You won!\33[m")
        else:
            print(
                "\33[31mUnfortunately, you ran out of guesses. The word was "
                + self.word + ". Maybe next time!\33[m"
                )

    def display_hangman(self):
        """
        Display all the visual cues for the user to play the game
        """
        sleep(2)
        os.system('clear')
        print(f"Available Letters: {' '.join(sorted(self.available_letters))}")
        print(STAGES[self.attempts])
        print('Can you solve this word:')
        print(' '.join(self.word_displayed))
        print(f"Tries left: {self.attempts}")
        print(f'Letters guessed: {" ".join(sorted(self.guessed_letters))}')
        print(f'Words guessed: {" ".join(self.guessed_words)}')
        print("\n")

    def resolve_guessed_letter(self, guessed_letter):
        """
        Decides if the guessed letter existe in the word and update the game
        """
        if guessed_letter in self.guessed_letters:
            print(f"You already guessed the letter {guessed_letter}")
        elif guessed_letter not in self.word:
            print(f"{guessed_letter} is not in the word.")
            self.attempts -= 1
        else:
            print(f"Well done, {guessed_letter} is in the word!")
            self.reveal_letters(guessed_letter)
        self.guessed_letters.append(guessed_letter)
        self.available_letters -= {guessed_letter}

    def resolve_guessed_word(self, guessed_word):
        """
        Decides if the word is the one chosen by the computer
        """
        if guessed_word in self.guessed_words:
            print("You already guessed the word", guessed_word)
        elif guessed_word != self.word:
            print(guessed_word, "is not the word.")
            self.attempts -= 1
            self.guessed_words.append(guessed_word)
        else:
            self.game_completed = True
            self.word_displayed = self.word

    def reveal_letters(self, guessed_letter):
        """
        Update the display word to show the position of the guessed letter
        """
        indices = [
            i for i, letter in enumerate(self.word)
            if letter == guessed_letter
            ]
        for index in indices:
            self.word_displayed[index] = guessed_letter
        if "*" not in self.word_displayed:
            self.game_completed = True


def main():
    """
    Greets the user and ask the user if they wants to play the game or not
    """
    print(pyfiglet.figlet_format("HANGMAN"))
    username()
    want_to_play = retrieve_yes_no_response(
        '\33[36mAre you ready to play Hangman? (Y/N)\n\33[m'
        )
    while want_to_play:
        word = random.choice(word_list)
        game = HangmanGame(word)
        game.run_game()
        want_to_play = retrieve_yes_no_response('Play Again? (Y/N) \n')
    display_goodbye()


if __name__ == "__main__":
    main()