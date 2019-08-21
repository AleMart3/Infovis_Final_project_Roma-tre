from kafka import KafkaProducer
import time
import os


producer = KafkaProducer(bootstrap_servers='kafka:9092')
cont=0


f = open("/data/business_review2.json", "r")
for line in f:
    print(line)
    cont+=1
    print(cont)
    producer.send('review', str.encode(line))
    producer.flush()
    time.sleep(0.3)
    #time.sleep(1)

