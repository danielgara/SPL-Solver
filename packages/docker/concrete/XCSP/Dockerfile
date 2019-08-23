FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y wget xz-utils openjdk-8-jdk

COPY ./concrete-3.11 /concrete
COPY ./run.sh /run.sh

ENTRYPOINT ["/run.sh"]
