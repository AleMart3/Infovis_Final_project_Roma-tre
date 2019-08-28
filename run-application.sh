#!/bin/bash

echo Starting the application...

echo Avvio zookeeper e kafka
docker-compose build
docker-compose up -d zookeeper kafka
echo wait 20 seconds
sleep 20

echo avvio pagine html e javascript_server_side
docker-compose up -d html_pages javascript_consumer
echo wait 20 seconds
sleep 20

echo apertura pagine html
start chrome http://localhost:8081/apri_pagine.html

echo Avvio analisi streaming
docker-compose up
