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


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    old_score = 0
    if SCORES_FILE_NAME.is_file():
        # getting old Value
        old_score = get_score_from_file()
    print(f"Old Score {old_score}")
    new_score = old_score + POINTS_OF_WINNING
    print(f"New Score {new_score}")
    # updating The New Score To File
    write_score_to_file(new_score)
