from flask import Flask  # import flask class
from config import Config # from config module import Config class
from flask_sqlalchemy import SQAlchemy # from sqlalchemy module import SQAlchemy object
from flask_migrate import Migrate #import Migrate class from migrate package

app = Flask(__name__) # instantiate flask object
app.config.from_object(Config) # read and apply config file

from app import routes # import routes, models file, always have this below

