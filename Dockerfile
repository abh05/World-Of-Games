FROM python:alpine
Run pip install flask
WORKDIR '/app/'
COPY .  .
CMD python /Score/MainScores.py