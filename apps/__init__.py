from flask import Flask

from config import load_config


def create_app():
    app = Flask(__name__)
    config = load_config()
    app.config.from_object(config)

    from apps.controller.api_v1 import api_v1
    api_v1.init_app(app)

    return app
