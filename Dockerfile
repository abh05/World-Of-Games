FROM python:alpine
RUN pip install flask
WORKDIR /app
COPY . .
CMD python Score/MainScores.py