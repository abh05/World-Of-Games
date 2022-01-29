from pathlib import Path

def add_score(difficulty):
    global Total
    POINTS_OF_WINNING = (difficulty * 3) + 5
    path_file = Path("C:/Users/avi/PycharmProjects/WorldOfGames/Scores.txt")
    if path_file.is_file():
        SCORES_FILE = open(path_file, "r+")
        prevuisscore = SCORES_FILE.readlines()
        print(f"Old Score {int(prevuisscore[0])}")
        for line in prevuisscore:
            splitted_line = line.split(' ')
            for values in splitted_line:
                value_as_int = int(values)
                value_as_int += POINTS_OF_WINNING
                print(f"New Score {value_as_int}")
                Total = value_as_int
                SCORES_FILE.close()
        SCORES_FILE = open(path_file, "w")
        SCORES_FILE.write(str(Total))
        SCORES_FILE.close()
    else:
        SCORES_FILE = open(path_file, "a+")
        SCORES_FILE.write(str(POINTS_OF_WINNING))
        print(POINTS_OF_WINNING)
        SCORES_FILE.close()




