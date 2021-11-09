FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /raspid
WORKDIR /raspid
COPY requirements.txt /raspid/
RUN pip install -r requirements.txt
COPY . /raspid/
