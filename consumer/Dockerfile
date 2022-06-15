# pull official base image
FROM python:3.10.4-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat \
  && apt-get clean


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .
RUN chown -R root:root /usr/src/app
RUN chmod +x /usr/src/app/entrypoint.sh
