"""EX03 - Structured Wordle"""
__author__ = "730463838"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(search_char:str, char_single:str) -> bool:
    """Check for characters in string"""
    character: bool = False
    i = 0
    assert len(char_single) == 1
    while i < len(search_char):
        if search_char[i] == char_single:
            character = True
        i = i + 1
    return (character)
def emojified(guess:str, secret:str) -> str:
    """See if guess and secret match"""
    i = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    squares: str = ""
    assert len(guess) == len(secret)
    while i < len(secret):
            if guess[i] == secret[i]:
                squares = squares + GREEN_BOX
            else:  # printing yellow and white
                if contains_char(secret, guess[i]): 
                    squares = squares + YELLOW_BOX
                else: 
                    squares = squares + WHITE_BOX
            i = i + 1
    return squares 
def input_guess(expected_length: int) -> str:
    secret_guess: str = input(f"Enter a {expected_length} character word: ")
    if len(secret_guess) == expected_length:
        return secret_guess
    while len(secret_guess) != expected_length:
        secret_guess = input(f"That wasn't {expected_length} chars! Try again:  ")
    return secret_guess
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    i = 1 
    word: bool = True
    while i<=6 and word: 
        print(f"=== Turn {i}/6 === ")
        user_guess: str = input_guess(len(secret))
        print(emojified(user_guess, secret))
        if user_guess == secret:
            print(f"You won in {i}/6 turns!")
            word = False 
        else:
            i = i + 1
    if user_guess != secret:
        print("X/6 - Sorry, try again tomorrow!")
if __name__ == "__main__":
    main()