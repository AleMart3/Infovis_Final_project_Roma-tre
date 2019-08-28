#!/bin/bash

echo Starting the application...

docker-compose build
docker-compose up -d zookeeper kafka
sleep 20


docker-compose up -d html_pages javascript_consumer
sleep 20
start chrome http://localhost:8081/apri_pagine.html
docker-compose up
