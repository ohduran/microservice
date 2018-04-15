#!environment/bin/python3
from flask import Flask
from config import Config

from flask_restful import Api


app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)

from app import endpoints
