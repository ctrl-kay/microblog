from flask import Flask  # import flask class
from config import Config # from config module import Config class
from flask_sqlalchemy import SQLAlchemy # from sqlalchemy module import SQAlchemy object
from flask_migrate import Migrate #import Migrate class from migrate package

app = Flask(__name__) # instantiate flask object
app.config.from_object(Config) # read and apply config file
db = SQLAlchemy(app) # db object to represent the database
migrate = Migrate(app, db) # migrate object to represent Migrate engine

from app import routes, models # import routes, models file, always have this below

