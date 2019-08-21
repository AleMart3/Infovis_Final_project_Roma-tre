FROM python:3

ADD ./producer.py producer.py

RUN pip install kafka-python==1.4.6

CMD [ "python", "producer.py" ] 