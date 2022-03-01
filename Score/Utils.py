import os
from pathlib import Path

SCORES_FILE_NAME = Path("Score/Score.txt")
BAD_RETURN_CODE = -1



def screen_cleaner():
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')










    # Draft
    # print('\r', end='')  # use '\r' to go back
    # print(" ", end='')
    #
    # # if os.name == 'posix':
    # #     __=os.system('clear')
    # # else:
    # #     __=os.system('cls')


