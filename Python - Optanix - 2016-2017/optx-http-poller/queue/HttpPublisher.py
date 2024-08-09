#!/usr/bin/python3
import pika
import uuid
from queue.AbstractQueue import AbstractQueue


class HttpPublisher(AbstractQueue):
    TTL = 30000

    is_wait_callback = False
    callback_queue = None
    corr_id = None
    response = None

    def create_response_queue(self):
        result = self.channel.queue_declare(exclusive=True, auto_delete=True)
        self.callback_queue = result.method.queue
        self.channel.queue_bind(exchange=self.EXCHANGE, queue=self.callback_queue)
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)
        self.is_wait_callback = True

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def send(self, message):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange=self.EXCHANGE,
                                   routing_key=self.QUEUE,
                                   properties=pika.BasicProperties(
                                       content_type="application/json",
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),

                                   body=message)
        if self.is_wait_callback:
            while self.response is None:
                self.connection.process_data_events()

        return str(self.response)
