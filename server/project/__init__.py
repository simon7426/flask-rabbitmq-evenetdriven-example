import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")

    app.config.from_object(app_settings)

    from project.apis import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {
            "app": app,
        }

    return app
