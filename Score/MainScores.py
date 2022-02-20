from flask import Flask, render_template
from jinja2 import TemplateNotFound
from Utils import BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/score')
def score_server():
    error = BAD_RETURN_CODE
    try:
        SCORES_FILE = open('Score.txt', "r")
        score = SCORES_FILE.readlines()
        score = int(score[0])
        return render_template("ScoreH.html", score=score)
    except (TemplateNotFound, FileNotFoundError):
        return render_template("ErrorF.html", ERROR=error)


app.run(port=40000, debug=True)
