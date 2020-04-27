from flask import Flask  #import flask class

app = Flask(__name__) #instantiate flask object

from app import routes #import routes file

