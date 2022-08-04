import wordle
import time

# Use this file to cheat and find out what the word you are trying to guess is
if __name__ == '__main__':
    with open("cheat.txt", "w") as f:
        f.write(wordle.RANDOM_WORD)

    print("Welcome to my Wordle Game! You have a maximum of 5 attemps to guess "
          "a 5 letter word, good luck! (Type 'help' for a list of used letters)" )
    time.sleep(2)

    while True:
        guess = wordle.Guess_Word(
            w_str=input(f'You have {wordle.Guess_Word.count} guesses remaining. Your word: ')
        )

        if guess.w_str == 'help':
            list = list(wordle.Guess_Word.alphabet.values())
            for i in list:
                 print(i, end=" " if list[-1] != i else "\n")
            continue

        if guess.is_valid():
            guess.increment_turn()
            guess.apply_guesses()
            guess.guessed_word()
            guess.game_loss()