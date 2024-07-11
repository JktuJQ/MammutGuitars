# Imports
from backend.application import application

from flask import render_template


@application.route('/', methods=["GET"])
def index():
    """Website index page"""
    return render_template("index.html")
