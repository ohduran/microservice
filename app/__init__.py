#!environment/bin/python3
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.ext.httpauth import HTTPBasicAuth

from flask_restful import Api


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)
auth = HTTPBasicAuth()

from app import endpoints, models
