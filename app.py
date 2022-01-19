from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/feature-a")
def hello_feature_a():
    return render_template('feature-a.html')

@app.route("/feature-b")
def hello_feature_b():
    return render_template('feature-b.html')