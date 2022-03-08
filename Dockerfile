FROM  python
WORKDIR /app
COPY . .
RUN pip install flask
RUN pip install CurrencyConverter
CMD python Score/MainScores.py