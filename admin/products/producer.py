import pika


params=pika.URLParameters('amqps://gxlccvid:aotLrPEaarM1Gk3YCra7CERnZwfTN9na@cow.rmq2.cloudamqp.com/gxlccvid')

connection=pika.BlockingConnection(params)

channel=connection.channel()

def publish():
    channel.basic_publish(exchange='',routing_key='admin',body='hello')
