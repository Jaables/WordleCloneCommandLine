from valid_words import valid_words
import random
import sys

RANDOM_WORD = random.choice(valid_words)
GUESSES_MAX = 0


class Colour:
    BASE = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"


class Guess_Word:
    count = 5
    store_words = []
    alphabet = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
    }
    def __init__(self, w_str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.guess_str = ""

    def increment_turn(self):
        Guess_Word.count -= 1

    def is_valid(self):
        if self.w_str in valid_words:
            return self.w_str
        else:
            print("Sorry that word doesn't exist. Try again: ")

    def green(self):
        for i, _ in enumerate(self.w_chars):
            actual_char = RANDOM_WORD[i]
            guessed_char = self.w_chars[i]
            if actual_char == guessed_char:
                coloured_char = f"{Colour.GREEN}{actual_char}{Colour.BASE}"
                self.w_chars[i] = coloured_char
                self.edit_alphabet(actual_char, coloured_char)


    def yellow(self):
        for i, _ in enumerate(self.w_chars):
            guessed_char = self.w_chars[i]
            not_green = Colour.GREEN not in Guess_Word.alphabet.get(guessed_char, '')
            if guessed_char in RANDOM_WORD and not_green:
                coloured_char = f"{Colour.YELLOW}{guessed_char}{Colour.BASE}"
                self.w_chars[i] = coloured_char
                self.edit_alphabet(guessed_char, coloured_char)
            else:
                coloured_char = f"{Colour.RED}{guessed_char}{Colour.BASE}"
                self.edit_alphabet(guessed_char, coloured_char)

    def edit_alphabet(self, k, v):
        # Stops additional keys being added
        if k not in Guess_Word.alphabet.keys():
            return
        Guess_Word.alphabet[k] = v

    def apply_guesses(self):
        self.green()
        self.yellow()
        self.guess_str = ''.join(self.w_chars)
        Guess_Word.store_words.append(self.guess_str)
        print(self.guess_str)




    def guessed_word(self):
        if self.w_str == RANDOM_WORD:
            print(f"Congrats you have beat Wordle with {Guess_Word.count} attempts remaining! Your guessed words were:")
            for i in Guess_Word.store_words:
                print(i)
            sys.exit(1)

    def game_loss(self):
        if Guess_Word.count == GUESSES_MAX:
            print(f'You lost :( The word you were looking for was {RANDOM_WORD}. Better luck next time!')
            sys.exit(1)



