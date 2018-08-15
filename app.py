from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello():
    adj = open("adj.txt").readlines()
    return "Ước gì " + adj[random.randint(0, len(adj) - 1)] + " như Đức Linh"
