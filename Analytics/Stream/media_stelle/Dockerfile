FROM rappdw/docker-java-python

RUN pip install pyspark==2.3.3 kafka-python==1.4.6

ADD ./media_stelle.py media_stelle.py

CMD ["python", "media_stelle.py"]