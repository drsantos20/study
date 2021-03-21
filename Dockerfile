FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /study-api
WORKDIR /study-api
COPY requirements.txt /study-api/
RUN pip install -r requirements.txt
COPY . /study-api/
