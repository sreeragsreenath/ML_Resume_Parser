FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install python3 python3-pip -y

RUN pip3 install django
RUN pip3 install PyPDF2
RUN pip3 install luigi
COPY mlbcsite/. /mlbcsite