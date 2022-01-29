# from Live import load_game
import random


def get_guess_from_user(difficulty):
    user_guess = input(f"Please Enter Your Guess Number between 1 - {difficulty}\n")
    while user_guess.isnumeric() is False or int(user_guess) < 1 or int(user_guess) > (int(difficulty)):
        print("invalid option: choose again")
        user_guess = input()
    else:
        user_guess = int(user_guess)
        return user_guess

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    print("genetrated is", secret_number)
    return secret_number

def compare_results(secret_number,user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False


def play(difficulty):
    user_guess = get_guess_from_user(difficulty)
    result = compare_results(generate_number(difficulty), user_guess)
    if result:
        print("True - you won")
        return True
    else:
        print("False - you lost")
        return False







