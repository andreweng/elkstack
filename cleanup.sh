#!/bin/bash

rm -fr elasticsearch/data/* &&
rm -fr elasticsearch/logs/* &&
rm -fr logstash/data/* &&
rm -fr kibana/data/* &&

echo "Data and logs are purged.  Dont' forget to git push"
