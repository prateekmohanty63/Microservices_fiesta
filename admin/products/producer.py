import pika,json


params=pika.URLParameters('amqps://gxlccvid:aotLrPEaarM1Gk3YCra7CERnZwfTN9na@cow.rmq2.cloudamqp.com/gxlccvid')

connection=pika.BlockingConnection(params)

channel=connection.channel()

def publish(method,body):
    properties=pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='main',body=json.dumps(body),properties=properties)
