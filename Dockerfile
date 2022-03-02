FROM python:alpine
Run pip install flask
WORKDIR '/app/Score/'
CMD python MainScores.py