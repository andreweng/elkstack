#!/bin/bash

docker run \
    -p 5601:5601 \
    -v ${PWD}/kibana/config:/usr/share/kibana/config \
    -v ${PWD}/kibana/data:/usr/share/kibana/data \
docker.elastic.co/kibana/kibana:7.8.0
