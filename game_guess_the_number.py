"""
Guess the number game

Moved to a separate module
"""
import random


def game_guess_the_number():
    """
    This function implements the Guess the Number game.

    The user needs to guess a randomly generated secret number between 1 and 20.
    The user has 7 attempts to guess the number correctly.
    """
    while True:
        number = random.randint(1, 20)
        tries = 0
        guess = 0
        print("Гра вгадай число")
        print("Число знаходиться між 1 і 20, ВВи маєте 7 спроб")
        while guess != number and tries < 7:
            guess = input("Яке число?: ")
            if guess.isdigit():
                guess = int(guess)
                if guess > number:
                    print("Надто велике!")
                elif guess < number:
                    print("Надто мале!")
            else:
                print("Це не число")
            tries += 1
        if guess == number:
            print("Ви вгадали число! Загадане число:", number)
        else:
            print("Ви не вгадали число! Загадане число:", number)
        print("Для виходу введіть: вийти")
        answer = input("Зіграти знову? ").lower().strip()
        if answer == "вийти":
            print("Допобачення")
            break
