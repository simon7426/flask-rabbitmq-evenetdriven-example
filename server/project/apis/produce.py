from flask_restx import Namespace, Resource, fields
from flask import request, json
from project.producer.client import ProducerClient

producer_namespace = Namespace("Produce")

user_model = producer_namespace.model(
    "User Model",
    {
        "name": fields.String(required=True),
        "address": fields.String(required=True)
    }
)

@producer_namespace.route("")
class Producer(Resource):
    @producer_namespace.expect(user_model, validate=True)
    def post(self):
        data = request.get_json()
        ProducerClient(json.dumps(data))
        return {
            "message": "Sent to queue!"
        }, 200
