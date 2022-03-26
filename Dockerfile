FROM  python
WORKDIR /app
COPY ./Score/ .
RUN pip install flask
RUN pip install CurrencyConverter
CMD python3 MainScores.py