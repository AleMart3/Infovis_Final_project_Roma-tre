#!/bin/bash

echo Starting the application...

docker-compose build
docker-compose up -d zookeeper kafka
sleep 20

echo Cancellazione topics se esistono
docker exec kafka kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic review
docker exec kafka kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic media_stelle
docker-compose up -d html_pages javascript_consumer
start chrome http://localhost:8081/apri_pagine.html
sleep 20
docker-compose up
