from flask_restx import Api

from project.apis.healthcheck import health_namespace
from project.apis.produce import producer_namespace

api = Api(version="1.0", title="Flask Rabbitmq demo api", doc="/docs")

api.add_namespace(health_namespace, "/healthz")
api.add_namespace(producer_namespace, "/produce")