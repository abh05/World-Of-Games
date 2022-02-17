import time
import random


def generate_sequence(difficulty):
    randomlist = []
    for i in range(difficulty):
        randomlist.append(random.randint(1, 101))

    return randomlist


def get_list_from_user(difficulty):
    user_guess = input(f"Please Enter {difficulty} numbers that you remember:\n")
    user_list = []
    while len(user_list) < difficulty:
        if user_guess.isnumeric() is False or user_guess.isdigit() is False:
            print("invalid input")
            user_guess = input()
        else:
            user_list.append(int(user_guess))
            if len(user_list) < difficulty:
                user_guess = input()
    return user_list


def is_list_equal(randomlist, user_list):
    print(user_list, randomlist)
    if user_list == randomlist:
        return True
    else:
        return False


def backline():
    print('\r', end='')  # use '\r' to go back


def play(difficulty):
    random_list = [generate_sequence(difficulty)]
    print("Stay Foucsed")
    for x in random_list:
        time.sleep(0.70)
        print("\r {}".format(x), end="")
    time.sleep(2)
    backline()
    print(" ", end='')

    user_guess = [get_list_from_user(difficulty)]
    result = is_list_equal(random_list, user_guess)
    if result:
        print("True - you won")
        return True
    else:
        print("False - you lost")
        return False



