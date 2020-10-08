#!/bin/bash
# Shutdown elkstack
docker-compose down && 

# Remove databases
rm -fr elasticsearch/data/* &&
rm -fr elasticsearch/logs/* &&
rm -fr logstash/data/* &&
rm -fr kibana/data/* &&

touch elasticsearch/data/.lock &&
touch elasticsearch/logs/.lock &&
touch logstash/data/.lock &&
touch kibana/data/.lock &&

# Synch up github
git add -A &&
git commit -m "synched via script" &&
git push &&

echo "Synched from local machine to github."
