from flask import Flask  # import flask class
from config import Config # from config module import Config class

app = Flask(__name__) # instantiate flask object
app.config.from_object(Config) # read and apply config file

from app import routes # import routes file, always have this below

