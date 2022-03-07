FROM python:alpine
WORKDIR /app
COPY . .

RUN apt-get update && apt-get upgrade -y && apt-get install gcc
RUN pip install pynacl
RUN pip install flask
RUN pip install selenium
RUN pip install CurrencyConverter
CMD python Score/MainScores.py