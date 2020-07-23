# elkstack
## BLUF
This is a basic elkstack deployment using Docker.  This will create 3 seperate containers: elasticsearch, logstash, and kibana based off of the current release 7.8.0 from docker.elastic.co.  

## Development
### Elasticsearch:
Host Directory mount for persistence:
- config (Configuration files, add clustering capabilities if needed)
- logs (logs for sifting through issues)
- data (es data)

### Kibana
- config (Configuration files)
- data (data)

### Logstash
- config (Not really used right now as it points to pipeline)
- pipeline (This is where the magic happens)
-- NOTE: if you open additional ports, don't forget to append those ports in docker run
- data (Not sure if this is needed, but we'll see)

### Deployment Notes
The containers will have permission issues with the logstash and kibana data directory in the elkstack folder.  This is because the services are run in non privileged users.  In a production environment, I will use volumes to correct this, but during this test phase, just do the following:

- cd elkstack
- chmod -R 777 *

Also, don't forget the firewall ports and security contexts if you have them open:
- ufw allow 9200/tcp
- ufw allow 5601/tcp
- ufw allow 5141/tcp

## Docker Compose:
#### docker-compose up

This will run all three instances: elasticsearch, kibana, logstash

http://localhost:5601

Default logstash port is <b>5141/\TCP</b>

## Manual Run:

Elasticsearch:

docker run \
    -p 9200:9200 \
    -p 9300:9300 \
    -v ${PWD}/elasticsearch/config:/usr/share/elasticsearch/config \
    -v ${PWD}/elasticsearch/logs:/usr/share/elasticsearch/logs \
    -v ${PWD}/elasticsearch/data:/usr/share/elasticsearch/data \
    -e "discovery.type=single-node" \
docker.elastic.co/elasticsearch/elasticsearch:7.8.0

Kibana:

docker run \
    -p 5601:5601 \
    -v ${PWD}/kibana/config:/usr/share/kibana/config \
    -v ${PWD}/kibana/data:/usr/share/kibana/data \
docker.elastic.co/kibana/kibana:7.8.0

Logstash:

docker run \
    -p 5141:5141 \
    -v ${PWD}/logstash/config:/usr/share/logstash/config \
    -v ${PWD}/logstash/pipeline:/usr/share/logstash/pipeline \
    -v ${PWD}/logstash/data:/usr/share/logstash/data \
docker.elastic.co/logstash/logstash:7.8.0

