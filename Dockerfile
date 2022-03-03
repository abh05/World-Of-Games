FROM python:alpine
RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
CMD python Score/MainScores.py