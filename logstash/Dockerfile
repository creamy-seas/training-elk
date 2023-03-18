FROM docker.elastic.co/logstash/logstash:7.4.1
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
COPY ./settings/ /usr/share/logstash/config/
COPY ./pipeline/ /usr/share/logstash/pipeline/
