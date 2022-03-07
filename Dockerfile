FROM python:3.7-alpine
WORKDIR /app
COPY . .
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
     && pip install cython \
     && apk del .build-deps gcc musl-dev
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install flask
RUN pip install CurrencyConverter
CMD python Score/MainScores.py