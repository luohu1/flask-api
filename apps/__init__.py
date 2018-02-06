from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config
from apps.views import api

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api.init_app(app)
    db.init_app(app)

    return app
