import pika
from flask import current_app as app


class ProducerClient:
    def __init__(self, body):
        self.credentials = pika.PlainCredentials(
            username=app.config["RABBITMQ_USER"], 
            password=app.config["RABBITMQ_PASSWORD"])
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=app.config["RABBITMQ_HOST"], credentials=self.credentials)
        )

        self.channel = self.connection.channel()

        self.channel.queue_declare('poridhi', durable=True)

        self.channel.basic_publish(
            exchange="",
            routing_key="poridhi",
            body=body
        )
        self.connection.close()
