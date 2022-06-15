import json
import sys
import pika
import os
from mysql.connector import connect, Error

class MessageReceiver:
    def __init__(self):
        self.credentials = pika.PlainCredentials(
            username=os.getenv("RABBITMQ_USER","poridhi"),
            password=os.getenv("RABBITMQ_PASSWORD","poridhi")
        )
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv("RABBITMQ_HOST", "localhost"), credentials=self.credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="poridhi", durable=True)
        self.channel.basic_consume(
            queue="poridhi",
            auto_ack=True,
            on_message_callback=self.callback
        )

    def callback(self, ch, method, properties, body):
        print(f"[x] Received {body}")
        body = json.loads(body)
        query = f"INSERT INTO users (name, address) VALUES ('{body['name']}', '{body['address']}');"
        try:
            with connect(
                host="mysql",
                user="poridhi",
                password="poridhi",
                database="poridhi"
            ) as connection:
                with connection.cursor() as cursor:
                    print(f"Executing query = {query}")
                    cursor.execute(query)
                    connection.commit()
        except Error as e:
            print(e)


if __name__ == "__main__":
    try:
        worker = MessageReceiver()
        worker.channel.start_consuming()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


# CREATE TABLE users (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, address VARCHAR(30) NOT NULL);