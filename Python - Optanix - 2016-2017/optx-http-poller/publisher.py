from config.rabbitmq_config import rabbitmq_config
from queue.HttpPublisher import HttpPublisher

if __name__ == "__main__":
    publisher = HttpPublisher(rabbitmq_config)
    publisher.connect()
    publisher.declare_exchange()
    publisher.create_response_queue()

    res = publisher.send('test message')
    print('Result: '+res)

    publisher.disconnect()
