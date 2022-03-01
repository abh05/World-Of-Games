FROM python:alpine
Run pip install flask
COPY .  .
CMD python /app/Score/MainScores.py