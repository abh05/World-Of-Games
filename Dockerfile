FROM python:alpine
Run pip install flask
WORKDIR '/app/'
COPY .  .
CMD python /app/Score/MainScores.py