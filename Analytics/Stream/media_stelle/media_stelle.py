import os
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from kafka import KafkaProducer

os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.3 pyspark-shell"

sc = SparkContext(appName="maxStars")
ssc = StreamingContext(sc, 5)
ssc.checkpoint("checkpoint")


# RDD with initial state (key, value) pairs
initialStateRDD = sc.parallelize([])


kstream = KafkaUtils.createDirectStream(ssc, ['review'], {"metadata.broker.list": 'kafka:9092'})

#producer.send('review', str.encode(line))
    #producer.flush()


#Nella funzione di update devono essere fatte le stesse operazioni che vengono fatte nella reduce + l'operazione della media, la media
#viene messa nell'ultimo campo

#last_values | new_value  -> [('nome', latitude, longitude, somma_stelle, somma_recensioni)]

def updateFunc(new_values, last_values):

    # print("last_values -> " + str(last_values))
    # print("new_values -> " + str(new_values))
    if last_values == None:

        #0:nome, 1:latitudine, 2:longitudine, 3:stars, 4:recensioni, 5:media

        return [(new_values[0][0], new_values[0][1], new_values[0][2], new_values[0][3], new_values[0][4], new_values[0][3]/new_values[0][4])]

    elif new_values == []:

        return [(last_values[0][0], last_values[0][1], last_values[0][2], last_values[0][3], last_values[0][4], last_values[0][3]/last_values[0][4])]

    else:
        return [(new_values[0][0], new_values[0][1] , new_values[0][2], new_values[0][3]+last_values[0][3], new_values[0][4] + last_values[0][4],
                 (new_values[0][3]+last_values[0][3])/(new_values[0][4] + last_values[0][4]))]

#OUTPUT STREAM:

# business_id -> [('nome', latitude, longitude, somma_stelle, somma_recensioni, media_stelle)]

#business: (business_id -> (name, address, city, state, postal_code, latitude, longitude, categories))
#review: (business_id -> (review_id, user_id, stars, text, date))

#(business_id -> (name, latitude, longitude, stars ,1)
business_review = kstream.map(lambda line: (json.loads(line[1])["business_id"], (json.loads(line[1])["name"],
                                                                                json.loads(line[1])["latitude"],
                                                                                json.loads(line[1])["longitude"],
                                                                                float(json.loads(line[1])["stars"]), 1,

                                                                                ))) \
                    .reduceByKey(lambda x, y:(x[0], x[1], x[2], x[3]+y[3],x[4]+y[4])) \
                    .updateStateByKey(updateFunc, initialRDD=initialStateRDD)\
                    .transform(lambda rdd: rdd.sortBy(lambda x: x[1][0][4], ascending=False))


def send_message(list_rdd):
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    #print(list_rdd)
    for rdd in list_rdd:
        if rdd != []:

            # rdd[1][0][0])    #nome
            # rdd[1][0][1])   #lat
            # rdd[1][0][2])    #lng
            # rdd[1][0][3])   #somma_stelle
            # rdd[1][0][4])   #somma_recensioni
            # rdd[1][0][5])    #media_stelle

            message= rdd[1][0][1] + "," + rdd[1][0][2] + "," + rdd[1][0][0] +"," + str(rdd[1][0][4]) +"," + str(rdd[1][0][5])
            producer.send("media_stelle", str.encode(message))
            producer.flush()


business_review.foreachRDD(lambda rdd : send_message(rdd.take(15)))


business_review.pprint()
ssc.start()
ssc.awaitTermination()

