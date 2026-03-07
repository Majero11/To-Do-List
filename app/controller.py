# import methods and objects from flask
from flask import render_template, redirect, url_for, request, session, flash

from config.database import get_db

from app import app


# create the routes
@app.route('/', methods = ["GET"])
def index():
    return render_template("index.html")