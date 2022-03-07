FROM  python
WORKDIR /app
COPY . .
RUN apk add --no-cache gcc musl-dev linux-headers
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install cryptography
RUN pip install flask
RUN pip install CurrencyConverter
CMD python Score/MainScores.py