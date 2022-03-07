FROM python:alpine
WORKDIR /app
COPY . .
RUN apk add linux-headers
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
     && pip install cython \
     && apk del .build-deps gcc musl-dev
RUN pip install flask
RUN pip install CurrencyConverter
CMD python Score/MainScores.py