FROM  FROM python:3.7-alpine
WORKDIR /app
COPY . .
RUN pip install urllib3==1.22
RUN pip3 install -U pip setuptools
RUN pip3 install --upgrade pip
RUN /usr/local/bin/python -m ensurepip --upgrade
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install cryptography
RUN pip install flask
RUN pip install CurrencyConverter
CMD python Score/MainScores.py