FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install python3 python3-pip -y

RUN pip3 install django
COPY mlbcsite/. /mlbcsite