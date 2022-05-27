# ELKSTACK for Proof of Concept
> Maintainer: Andrew Eng 
> Last Updated: 2022-May-27

# Summary
This ELKSTACK docker setup is for ELKSTACK testing.  This is a basic deployment where docker-compose will bring up elasticsearch and kibana version 8.2.2.  Environment variables included in the docker-compose file are:

Elasticsearch:
- Cluster Name: SIEM
- Bind Address: opened to the world
- Port Number: Default port is 9200
- XPACK Security is disabled

Kibana:
- Bind Address: open to the world
- Elasticsearch Host: since both elastic and kibana is on the bridged network, I used 172.17.0.1.

Both containers will use docker volumes:
- esdata : /usr/share/elasticsearch
- kibana-data : /usr/share/kibana

# Design Considerations
I use this setup for doing quick tests to perform analytics and shut it down when no longer needed.  Security was not designed initially.  However, it is in my queue to configure elkstack security later down the road.  

Use this ELK Docker POC for development and testing.  All other uses are strongly unadvised.
