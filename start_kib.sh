#!/bin/bash

docker run -p 5601:5601 -v ~/dock-es/kibana/config:/usr/share/kibana/config -v ~/dock-es/kibana/data:/usr/share/kibana/data docker.elastic.co/kibana/kibana:7.8.0
