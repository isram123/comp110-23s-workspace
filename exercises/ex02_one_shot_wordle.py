"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730463838"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)} guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_game: bool = True
# look at each letter in the string
while guess_game: 
    if len(guess) == len(secret_word):
        i = 0
        squares = ""
        while i < len(secret_word):
            if guess[i] == secret_word[i]:
                squares = f"{squares}{GREEN_BOX}"
            else: # printing yellow and white
                match_idx = 0
                found = False
                while match_idx < len(secret_word):
                    if guess[i] == secret_word[match_index]:
                        found = True
                    match_index = match_idx + 1 
                if found: squares = f"{squares}{YELLOW_BOX}"
                else: squares = f"{squares}{WHITE_BOX}"
            i = i + 1  
        print(squares)
        if guess == secret_word:
            print("Woo! You got it!")
        else:
                print("Not quite. Play again soon!")
        guess_game = False
    else: # guess not the length of secret word
        guess = input(f"That was not {len(secret_word)} letters! Try again: ")

