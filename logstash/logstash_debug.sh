docker run -it -p 5141:5141 -v ${PWD}/pipeline:/usr/share/logstash/pipeline docker.elastic.co/logstash/logstash:8.2.2 /usr/share/logstash/bin/logstash -f /usr/share/logstash/pipeline/logstash.conf
