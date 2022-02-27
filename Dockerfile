FROM python:alpine
Run pip install flask
WORKDIR '/app/'
ADD templates /app/templates/
COPY ./Score/ .
CMD python /app/MainScores.py