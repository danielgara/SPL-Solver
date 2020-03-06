from flask import Flask

from solvers.main.config import config_map


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    return app
