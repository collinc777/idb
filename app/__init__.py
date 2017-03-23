# __init__.py essentially makes the folder "app" a module we can import
# you can see a usage of this in application.py: "from app import application"
# which we define down below

from flask import Flask
import SQLAlchemy  # this is was the only way i could get it to work. :/

application = Flask(__name__)
# Update this to the URI of our database in IDB2
# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
database = SQLAlchemy(application)

from app import views
