FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install flask
RUN pip install selenium
RUN pip install CurrencyConverter
CMD python Score/MainScores.py