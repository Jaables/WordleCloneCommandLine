import wordle

if __name__ == '__main__':
    with open("cheat.txt", "w") as f:
        f.write(wordle.RANDOM_WORD)

    while True:
        guess = wordle.Guess_Word(
            w_str=input(f'[{wordle.Guess_Word.count}]')
        )
        if guess.is_valid():
            guess.increment_turn()
            guess.apply_guesses()
            guess.guessed_word()
            guess.game_loss()