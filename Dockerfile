FROM python:alpine
Run pip install flask
WORKDIR '.'
COPY .  .
CMD python MainScores.py