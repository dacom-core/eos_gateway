FROM python:3.6.2

COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install binutils libproj-dev gdal-bin -y
RUN pip install pipenv
RUN pip install -r requirements.txt

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

RUN chmod +x /tmp