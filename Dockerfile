FROM python:alpine
Run pip install flask
WORKDIR '/app/'
ADD Utils.py /app/Score/
COPY . .
CMD python /app/Score/MainScores.py