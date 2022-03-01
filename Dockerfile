FROM python:alpine
Run pip install flask
COPY .  .
CMD python MainScores.py