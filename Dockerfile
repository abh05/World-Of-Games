FROM python:alpine
COPY . .
RUN pip install -r requirements.txt
CMD python Score/MainScores.py