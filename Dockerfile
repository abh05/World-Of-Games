FROM python:alpine
Run pip install flask
WORKDIR '/app/'
COPY ./Score/ .
CMD python /app/MainScores.py