from app import app
import requests as r
from flask import render_template

@app.route('/')
def land():
    return render_template('land.html')