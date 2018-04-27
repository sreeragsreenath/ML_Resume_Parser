FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install python3 python3-pip -y

RUN pip3 install django
RUN pip3 install PyPDF2
RUN pip3 install luigi
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install sklearn
RUN pip3 install scipy
RUN pip3 install nltk
RUN pip3 install textblob
RUN pip3 install boto3
COPY mlbcsite/. /mlbcsite