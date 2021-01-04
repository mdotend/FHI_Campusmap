FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update -y
RUN apt-get -y install libgdal-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
