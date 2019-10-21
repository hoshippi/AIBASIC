from flask import Flask, render_template, request
from .database import init_db
from .config import Config


def create_app():
    app = Flask(__name__)
    init_db(app)
    app.config.from_object(Config)

    return app

app = create_app()

