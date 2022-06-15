#!/bin/bash
while ! nc -z rabbitmq 5672; do sleep 3; done

echo "Rabbitmq up"
python consumer.py