import Utils
from flask import Flask, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__, template_folder='C:/Users/avi/PycharmProjects/WorldOfGames/')

@app.route('/score')
def score_server():
    error = Utils.BAD_RETURN_CODE
    try:
        SCORES_FILE  = open("C:/Users/avi/PycharmProjects/WorldOfGames/Scores.txt", "r")
        score = SCORES_FILE.readlines()
        score = int(score[0])
        return render_template("ScoreH.html", score=score)
    except (TemplateNotFound, FileNotFoundError):
        return render_template("ErrorF.html", ERROR=error)


app.run(port=40000, debug=True)

