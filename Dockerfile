FROM python:alpine
Run pip install flask
WORKDIR '/app/'
CMD python MainScores.py