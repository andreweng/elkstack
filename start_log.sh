#!/bin/bash

docker run -p 5141:5141 -v ~/dock-es/logstash/config:/usr/share/logstash/config -v ~/dock-es/logstash/pipeline:/usr/share/logstash/pipeline -v ~/dock-es/logstash/data:/usr/share/logstash/data docker.elastic.co/logstash/logstash:7.8.0
