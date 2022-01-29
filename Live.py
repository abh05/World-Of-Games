import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score


def welcome(name):
    welcome_message = f"Hello {name} and welcome to the World of Games (WoG).\n" \
                      "Here you can find many cool games to play."
    return welcome_message

def load_game():


    load_welcome_message = "Please choose a game to play:\n"\
                           " 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n" \
                           " 2. Guess Game - guess a number and see if you chose like the computer.\n" \
                           " 3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n"
    game_difficulty_message = "Please choose game difficulty from 1 to 5:\n"

    chosen_game = input(load_welcome_message)
    while chosen_game.isnumeric() is False or int(chosen_game) <= 0 or int(chosen_game) >= 4:
        chosen_game = input("invalid option: choose again\n")
    else:
        chosen_game = int(chosen_game)

    chosen_difficulty = input(game_difficulty_message)
    while chosen_difficulty.isnumeric() is False or int(chosen_difficulty) <= 0 or int(chosen_difficulty) >= 6:
        chosen_difficulty = input("invalid option: choose again\n")
    else:
        chosen_difficulty = int(chosen_difficulty)

    # mymenu = {1: MemoryGame.play(chosen_difficulty),
    #           2: GuessGame.play(chosen_difficulty),
    #           3: CurrencyRouletteGame.play(chosen_difficulty)
    #           }
    # mymenu[chosen_game]
    if chosen_game == 1:
        if MemoryGame.play(chosen_difficulty) is True:
            Score.add_score(chosen_difficulty)
    elif chosen_game == 2:
        if GuessGame.play(chosen_difficulty) is True:
            Score.add_score(chosen_difficulty)
    elif chosen_game == 3:
        if CurrencyRouletteGame.play(chosen_difficulty) is True:
            Score.add_score(chosen_difficulty)






















