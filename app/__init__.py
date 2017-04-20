# __init__.py essentially makes the folder "app" a module we can import
# you can see a usage of this in application.py: "from app import application"
# which we define down below
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

application = Flask(__name__)
CORS(application)
application.config.from_object('config')
database = SQLAlchemy(application)

from app import views
