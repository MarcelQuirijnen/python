#!/usr/bin/python3
import pika
import time
from queue.AbstractQueue import AbstractQueue


class HttpConsumer(AbstractQueue):

    def on_request(self, ch, method, props, body):
        print(" [x] Received message %r" % body)
        response = body
        time.sleep(1)
        if props.reply_to:
            ch.basic_publish(exchange=self.EXCHANGE,
                             routing_key=props.reply_to,
                             properties=pika.BasicProperties(
                                 correlation_id=props.correlation_id,
                                 content_type="application/json",

                             ),
                             body=response)
            print(" [x] Send answer %r" % body)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(" [x] Done")

    def run(self):
        self.connect()
        self.declare_exchange()
        self.channel.basic_consume(self.on_request, queue=self.QUEUE)
        self.channel.start_consuming()
