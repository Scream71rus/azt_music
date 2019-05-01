#!/bin/sh

PING=0

while [ $PING != 1 ] ; do
    PING=$(psql -d azt -U azt -h db -c "select 'ping';" | grep -c 'ping')
    echo 'Await DB...'
    sleep 1s
done

psql -h db -d azt -U azt -f /home/application/azt.sql

python ./server.py \
    --db_host=$DB_HOST \
    --cache_host=$CACHE_HOST \
