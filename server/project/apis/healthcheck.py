from flask_restx import Namespace, Resource

health_namespace = Namespace("health")


@health_namespace.route("")
class Healthz(Resource):
    def get(self):
        return {"message": "ok"}, 200
