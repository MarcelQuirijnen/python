#!/usr/bin/python3
import abc
import pika


class AbstractQueue(metaclass=abc.ABCMeta):
    USER = 'user'
    PASSWORD = 'password'
    HOST = 'host'
    PORT = 'port'
    VHOST = 'vhost'

    EXCHANGE = 'http-poller'
    EXCHANGE_TYPE = 'direct'
    QUEUE = 'poller'

    parameters = {}
    connection = None
    channel = None
    queue = None

    def __init__(self, parameters):
        self.parameters = parameters

    def connect(self):
        print("Connect...")
        credentials = pika.PlainCredentials(self.parameters[self.USER], self.parameters[self.PASSWORD])
        connection_params = pika.ConnectionParameters(self.parameters[self.HOST],
                                                      self.parameters[self.PORT],
                                                      self.parameters[self.VHOST],
                                                      credentials)

        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()

    def declare_exchange(self):
        self.channel.exchange_declare(exchange=self.EXCHANGE, exchange_type=self.EXCHANGE_TYPE, durable=True)
        self.channel.queue_declare(queue=self.QUEUE, durable=True)
        self.channel.queue_bind(exchange=self.EXCHANGE, queue=self.QUEUE)

    def disconnect(self):
        print("Connect...")
        self.connection.close()
