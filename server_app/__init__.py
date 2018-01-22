"""
CREAt: 2018/1/19
AUTHOR: Hehahutu
"""
from flask import Flask
from server_app.server_views import fibp
from setting import DEBUG, SECRET_KEY


def create_app():
    app = Flask(__name__)
    app.debug = DEBUG
    app.secret_key = SECRET_KEY
    register_blueprint(app)

    return app


def register_blueprint(app):
    app.register_blueprint(fibp)
