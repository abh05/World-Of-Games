FROM python:alpine
Run pip install flask
WORKDIR '/app/'
CMD python /ScoreBLA/MainScores.py