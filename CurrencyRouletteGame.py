import random
import currency_converter


def get_money_interval(difficulty): #get the current currency rate from USD to ILS
    c = currency_converter
    randnum = random.randint(1, 100)
    print(f"This is the {randnum} USD that you need to guess the conversion")
    t = c.CurrencyConverter(decimal=True).convert(randnum,'USD','ILS')
    d = difficulty
    interval = (t - (5 - d), t + (5 - d))
    return interval

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_guess_from_user(): #prompt a guess from the user to enter a guess of value to a given amount of USD#
    guess_user = input("please enter your 'ILS' guess\n")
    while guess_user.isnumeric() is False and isfloat(guess_user) is False:
        print("invalid option: choose again")
        guess_user = input()
    else:
        guess_user = float(guess_user)

    return guess_user


def play(difficulty):
    generated = get_money_interval(difficulty)
    guess_user = get_guess_from_user()
    print(generated)
    if guess_user < generated[0] or guess_user > generated[1]:
        print("lost")
        return False
    else:
        print("correct win")
        return True









