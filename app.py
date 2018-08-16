from flask import Flask
from flask import render_template
from memgenerator import make_meme
import random

app = Flask(__name__)


@app.route("/")
def hello():
    adj = open("adj.txt").readlines()
    make_meme("ƯỚC GÌ " + adj[random.randint(0, len(adj) - 1)], "NHƯ ĐỨC LINH", "templates/template.jpg")
    return render_template('meme.html', )
