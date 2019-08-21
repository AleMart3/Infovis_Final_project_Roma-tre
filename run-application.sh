#!/bin/bash

echo Starting the application...

docker-compose build
docker-compose up -d zookeeper kafka
sleep 20

echo Cancellazione topics se esistono
docker exec kafka kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic review
docker exec kafka kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic media_stelle
docker exec  kafka  kafka-topics.sh  --list --zookeeper zookeeper:2181
docker-compose up -d googlemaps google_consumer barchart
start chrome http://localhost:8081/googlecluster.html
start chrome http://localhost:8082/barchart.html
sleep 20
docker-compose up
