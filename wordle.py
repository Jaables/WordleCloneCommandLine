from valid_words import valid_words
import random
import sys

RANDOM_WORD = random.choice(valid_words)
GUESSES_MAX = 5


class Colour:
    BASE = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"


class Guess_Word:
    count = 0
    def __init__(self, w_str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.guess_str = ""

    def increment_turn(self):
        Guess_Word.count += 1

    def is_valid(self):
        return self.w_str in valid_words

    def green(self):
        for i, _ in enumerate(self.w_chars):
            actual_char = RANDOM_WORD[i]
            guessed_char = self.w_chars[i]
            if actual_char == guessed_char:
                coloured_char = f"{Colour.GREEN}{actual_char}{Colour.BASE}"
                self.w_chars[i] = coloured_char

    def yellow(self):
        for i, _ in enumerate(self.w_chars):
            guessed_char = self.w_chars[i]
            if guessed_char in RANDOM_WORD:
                coloured_char = f"{Colour.YELLOW}{guessed_char}{Colour.BASE}"
                self.w_chars[i] = coloured_char


    def apply_guesses(self):
        self.green()
        self.yellow()
        self.guess_str = ''.join(self.w_chars)
        print(self.guess_str)

    def guessed_word(self):
        if self.w_str == RANDOM_WORD:
            print(f"Congrats you have beat Wordle in {Guess_Word.count} tries!")
            sys.exit(1)

    def game_loss(self):
        if Guess_Word.count == GUESSES_MAX:
            print(f'You lost :( The word you were looking for was {RANDOM_WORD}. Better luck next time!')
            sys.exit(1)



