FROM python:latest

MAINTAINER sar.yoon89@gmail.com

RUN apt-get update && apt-get -y install vim

RUN mkdir /automation

COPY ./apidemotest/ automation/apidemotest/
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install


ENV MACHINE=docker
ENV WP_HOST=mamp

ENV WC_KEY=ck_e5df94f4a380812b14f6fb4f5943581117a45bd4
ENV WC_SECRET=cs_57b648248cdb80766f37e3c584dfc43211951886
ENV DB_USER=root
ENV DB_PASSWORD=root