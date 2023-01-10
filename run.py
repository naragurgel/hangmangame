import random
import string
from words import word_list
from stages import STAGES

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

    def __init__(self):
        self.word = ""
        self.word_displayed = ""
        self.game_completed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.attempts = 6
        self.available_letters = set(string.ascii_uppercase)

    def choose_word(self):
        """
        Gets a random word from the list 'words' and converts the user input to uppercase to make easer the comparison logic
        """
        self.word = random.choice(word_list).upper()
        self.word_displayed = "_" * len(self.word)

    def start_game(self):
        """
        represent unguesses letters as underscores and show letter as correct guesses #noqa
        """
        print("Are you ready to play Hangman? Let's get started!")
        self.display_hangman()
        """
        the loops runs till the word is guessed or the users runs out of guessed_letter
        """
        while not self.game_completed and self.attempts > 0:
            guess = input("Please guess a letter or word: \n").upper()
            if len(guess) == 1 and guess.isalpha():
                self.resolve_guessed_letter(guess)

            elif len(guess) == len(self.word) and guess.isalpha():
                self.resolve_guessed_word(guess)
            else:
                print("Not a valid guess.")
            self.display_hangman()

        if self.game_completed:
            print("God job, you guessed the word! You won!")
        else:
            print("Unfortunately, you ran out of guesses. The word was " + self.word + ". Maybe next time!")  # noqa

    def display_hangman(self):
        """
        to print the game instructions and the hangman tries
        """
        print(f"Available Letters: {' '.join(sorted(self.available_letters))}")
        print(STAGES[self.attempts])
        print(self.word_displayed)
        print(f"Tries left: {self.attempts}")
        print(f'Letters guessed: {" ".join(self.guessed_letters)}')
        print(f'Words guessed: {" ".join(self.guessed_words)}')
        print("\n")

    def resolve_guessed_letter(self, guessed_letter):
        """
        commands for game results as inputs from the user
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
        result for guessed word 
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
        result gor guessed letters
        """
        word_as_list = list(self.word_displayed)
        indices = [i for i, letter in enumerate(self.word) if letter == guessed_letter]
        for index in indices:
            word_as_list[index] = guessed_letter
        self.word_displayed = "".join(word_as_list)
        if "_" not in self.word_displayed:
            self.game_completed = True

def main():
    game = HangmanGame()
    game.choose_word()
    game.start_game()

    while input("Play Again? (Y/N) \n").upper() == "Y":
        game = HangmanGame()
        game.choose_word()
        game.start_game()


if __name__ == "__main__":
    main()