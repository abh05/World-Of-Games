from pathlib import Path
from Utils import SCORES_FILE_NAME

def get_score_from_file():
    SCORES_FILE = open(SCORES_FILE_NAME, "r+")
    prevuisScore = SCORES_FILE.readlines()[0]
    score_as_int = int(prevuisScore)
    SCORES_FILE.close()
    return score_as_int

def write_score_to_file(score):
    SCORES_FILE = open(SCORES_FILE_NAME, "w")
    SCORES_FILE.write(str(score))
    SCORES_FILE.close()


#
# def add_score3(difficulty):
#     global Total
#     POINTS_OF_WINNING = (difficulty * 3) + 5
#     if path_file.is_file():
#         SCORES_FILE = open(path_file, "r+")
#         prevuisScore = SCORES_FILE.readlines()
#         print(f"Old Score {int(prevuisScore[0])}")
#         for line in prevuisScore:
#             splitted_line = line.split(' ')
#             for values in splitted_line:
#                 value_as_int = int(values)
#                 value_as_int += POINTS_OF_WINNING
#                 print(f"New Score {value_as_int}")
#                 Total = value_as_int
#                 SCORES_FILE.close()
#         SCORES_FILE = open(path_file, "w")
#         SCORES_FILE.write(str(Total))
#         SCORES_FILE.close()
#     else:
#         SCORES_FILE = open(path_file, "a+")
#         SCORES_FILE.write(str(POINTS_OF_WINNING))
#         print(POINTS_OF_WINNING)
#         SCORES_FILE.close()


# def add_score2(difficulty):
#     POINTS_OF_WINNING = (difficulty * 3) + 5
#     if not (path_file.is_file()):
#         write_score_to_file(POINTS_OF_WINNING)
#         print(f"Your Score is: {POINTS_OF_WINNING} Points")
#     else:
#         old_score = get_score_from_file()
# #       Finished getting old Value
#         print(f"Old Score {old_score}")
#         new_score = old_score + POINTS_OF_WINNING
#         print(f"New Score {new_score}")
# #       updating The New Score To File
#         write_score_to_file(new_score)
# #
def add_score3(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    old_score = 0
    if SCORES_FILE_NAME.is_file():
    #getting old Value
        old_score = get_score_from_file()
    print(f"Old Score {old_score}")
    new_score = old_score + POINTS_OF_WINNING
    print(f"New Score {new_score}")
    # updating The New Score To File
    write_score_to_file(new_score)



        #homeWork Change the method so score is 0 once the file does not exsist - no Code Duplication



