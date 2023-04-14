"""EX06 - Choose your own adeventure!"""
__author__ = "730463838"

from random import randint
player: str
points: int
plays: bool = True
WINTER_CONSTANT: str = "\U0001F5FB"
SUMMER_CONSTANT: str = "\U0001F30A"
SPRING_CONSTANT: str = "\U0001F4A7"
FALL_CONSTANT: str = "\U0001F341"


def greet() -> None:
    """Greet player!"""
    global player
    player = input("What is your name? ")
    print(f"Hello {player}!")


def second_quiz() -> None:
    """Second quiz for player!"""
    global points
    print(f"What city are you, {player}?")
    answer: str = input("What is your ideal weekend? \na. adventuring outside \nb. take your dog on a walk \nc. staying in bed and watching movies \nd. night in with friends \n")
    if answer == "a":
        points += 4
    if answer == "b":
        points += 3
    if answer == "c": 
        points += 1
    if answer == "d":
        points += 2
    input(f"Favorite drink, {player}? \na. Slushee \nb. Lemonade \nc. Hot cocoa \nd. Apple Cider \n")
    if answer == "a":
        points += 4
    if answer == "b":
        points += 3
    if answer == "c": 
        points += 1
    if answer == "d":
        points += 2
    input(f"People would describe you ({player}) as... \na. A free spirit \nb. Kind \nc. Independent \nd. Creative \n")
    if answer == "a":
        points += 4
    if answer == "b":
        points += 3
    if answer == "c": 
        points += 1
    if answer == "d":
        points += 2
    input(f"Ideal season, {player}? \na. Summer \nb. Spring \nc. Winter \nd. Fall \n")
    if answer == "a":
        points += 4
    if answer == "b":
        points += 3
    if answer == "c": 
        points += 1
    if answer == "d":
        points += 2
    input(f"Favorite animal, {player}? \na. Lion \nb. Giraffe \nc. Penguin \nd. Otter \n")
    if answer == "a":
        points += 4
    if answer == "b":
        points += 3
    if answer == "c": 
        points += 1
    if answer == "d":
        points += 2
    input(f"What color do you, {player} identify with? \na. Yellow \nb. Pink \nc. Purple \nd. Red \n")
    if answer == "a":
        points += 4
    if answer == "b":
        points += 3
    if answer == "c": 
        points += 1
    if answer == "d":
        points += 2
    if points >= 21:
        print(f"{player}, you are Honolulu {SUMMER_CONSTANT}!")
    elif points >= 16 and points <= 20:
        print(f"{player}, you are LA {SPRING_CONSTANT}!")
    elif points >= 11 and points <= 15:
        print(f"{player}, you are NYC {WINTER_CONSTANT}!")
    elif points >= 6 and points <= 10:
        print(f"{player}, you are D.C. {FALL_CONSTANT}!")


def original_quiz(point: int) -> int:
    """Original quiz for player!"""
    print("What city are you?")
    point = 0
    answer: str = input(f"What is your ideal weekend, {player}? \na. adventuring outside \nb. take your dog on a walk \nc. staying in bed and watching movies \nd. night in with friends \n")
    if answer == "a":
        point += 4
    if answer == "b":
        point += 3
    if answer == "c": 
        point += 1
    if answer == "d":
        point += 2
    input(f"Favorite drink, {player}? \na. Slushee \nb. Lemonade \nc. Hot cocoa \nd. Apple Cider \n")
    if answer == "a":
        point += 4
    if answer == "b":
        point += 3
    if answer == "c": 
        point += 1
    if answer == "d":
        point += 2
    input(f"People would describe you, {player} as... \na. A free spirit \nb. Kind \nc. Independent \nd. Creative \n")
    if answer == "a":
        point += 4
    if answer == "b":
        point += 3
    if answer == "c": 
        point += 1
    if answer == "d":
        point += 2
    input(f"Ideal city, {player}? \na. Honolulu \nb. LA \nc. NYC \nd. Atlanta \n")
    if answer == "a":
        point += 4
    if answer == "b":
        point += 3
    if answer == "c": 
        point += 1
    if answer == "d":
        point += 2
    input(f"Favorite animal, {player}? \na. Lion \nb. Giraffe \nc. Penguin \nd. Otter \n")
    if answer == "a":
        point += 4
    if answer == "b":
        point += 3
    if answer == "c": 
        point += 1
    if answer == "d":
        point += 2
    input(f"What color do you, {player} identify with? \na. Yellow \nb. Pink \nc. Purple \nd. Red \n")
    if answer == "a":
        point += 4
    if answer == "b":
        point += 3
    if answer == "c": 
        point += 1
    if answer == "d":
        point += 2
    if point >= 21:
        print(f"{player}, you are Summer {SUMMER_CONSTANT}!")
    elif point >= 16 and points <= 20:
        print(f"{player}, you are Spring {SPRING_CONSTANT}!")
    elif point >= 11 and points <= 15:
        print(f"{player}, you are Winter {WINTER_CONSTANT}!")
    elif point >= 6 and points <= 10:
        print(f"{player}, you are Fall {FALL_CONSTANT}!")   
    return point


def main() -> None:
    """To hold functions!"""
    global points
    points = 0
    global plays 
    global player
    greet()
    while plays is True:
        option: str = input(f"1. Take original quiz {player} (continue on), 2. Take a different quiz, 3. End the experience, 4. Random quiz! \n")
        if option == "3":
            print(f"Thank you for playing! You gained {points} points!")
            plays = False
        if option == "2":
            second_quiz()
        if option == "1":
            points += original_quiz(points) 
        if option == "4":
            if randint(1, 2) == 1:
                original_quiz(points)
            else: 
                second_quiz()


if __name__ == "__main__":
    main()