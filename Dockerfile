FROM python:3.7-alpine
WORKDIR /app
COPY . .
RUN apk add --no-cache gcc musl-dev linux-headers
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install flask
RUN pip install CurrencyConverter
RUN pip install python3-setuptools
CMD python Score/MainScores.py