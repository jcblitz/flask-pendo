from flask import Flask
from flask import render_template
from datetime import datetime
import gunicorn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', id=datetime.now())

@app.route("/feature-a")
def hello_feature_a():
    return render_template('feature-a.html', id=datetime.now())

@app.route("/feature-b")
def hello_feature_b():
    return render_template('feature-b.html', id=datetime.now())