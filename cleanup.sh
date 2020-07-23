#!/bin/bash

rm -fr elasticsearch/data/* &&
rm -fr elasticsearch/logs/* &&
rm -fr logstash/data/* &&
rm -fr kibana/data/* &&

touch elasticsearch/data/.lock &&
touch elasticsearch/logs/.lock &&
touch logstash/data/.lock &&
touch kibana/data/.lock &&

echo "Data and logs are purged.  Dont' forget to git push"
