from config.rabbitmq_config import rabbitmq_config
from queue.HttpConsumer import HttpConsumer

if __name__ == "__main__":
    consumer = HttpConsumer(rabbitmq_config)
    consumer.run()
