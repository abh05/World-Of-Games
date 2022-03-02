FROM python:alpine
Run pip install flask
WORKDIR '/'
CMD python /Score/MainScores.py