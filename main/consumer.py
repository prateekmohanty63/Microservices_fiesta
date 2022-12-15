import pika,json
from main import Product,db

params=pika.URLParameters('amqps://gxlccvid:aotLrPEaarM1Gk3YCra7CERnZwfTN9na@cow.rmq2.cloudamqp.com/gxlccvid')

connection=pika.BlockingConnection(params)

channel=connection.channel()

channel.queue_declare(queue='main')


def callback(ch,method,properties,body):
    print('Received in main')
    print(body)
    data=json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product=Product(id=data['id'],title=data['title'],image=data['image'])
        db.session.add(product)
        db.session.commit()
    elif properties.content_type == 'product_created':
        product=Product.query.get(data['id'])
        product.title=data['title']
        product.image=data['image']
        db.session.commit()
    
    elif properties.content_type=="product_deleted":
        product=Product.query.get(data)
        db.session.delete(product)
        db.session.commit()




channel.basic_consume(queue='main',on_message_callback=callback,auto_ack=True)
print('Started Consuming')

channel.start_consuming()

channel.close()
