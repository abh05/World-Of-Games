FROM python:alpine
Run pip install flask
WORKDIR '/app/'
COPY .  .
CMD python MainScores.py