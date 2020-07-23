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

## Docker Run:

Elasticsearch:

docker run /\
    -p 9200:9200 /\
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

