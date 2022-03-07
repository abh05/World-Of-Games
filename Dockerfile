FROM  python
WORKDIR /app
COPY . .
RUN /usr/local/bin/python -m ensurepip --upgrade
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install cryptography
RUN pip install flask
RUN pip install CurrencyConverter
CMD python Score/MainScores.py