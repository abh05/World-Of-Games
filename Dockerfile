FROM python:alpine
Run pip install flask
WORKDIR '/app/'
CMD pythonn ./Score/MainScores.py