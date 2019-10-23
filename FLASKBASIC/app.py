from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from .database import init_db
from .config import Config
from . import models



def create_app():
    app = Flask(__name__)
    Bootstrap(app) 
    init_db(app)

    app.config.from_object(Config)
    

    return app

app = create_app()

