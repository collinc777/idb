# We'll define all of our views in this file. 

from flask import render_template, flash, redirect
from app import application


@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('hello.html')
