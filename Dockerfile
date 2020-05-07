FROM ubuntu:16.04

MAINTAINER Juan Lucas Ibarra

RUN apt-get update \

&& apt-get install -y python3-pip python3-dev libpq-dev \

&& pip3 install --upgrade pip \

&& apt-get install nano \

&& pip install django \

&& pip install psycopg2 \

&& pip install psycopg2-binary

COPY ProyectoChiper /home/

EXPOSE 8000
