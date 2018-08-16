from flask import Flask
from flask import render_template
from flask import request
from memgenerator import make_meme
import random

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            adj = request.form['text'].upper()
            choice = request.form['template']
        except KeyError:
            adj = ''
            choice = 'random'
        print(adj)
        print(choice)
        if choice == 'random' and adj == '':
            adj = open("adj.txt").read().split('\n')
            make_meme("ƯỚC GÌ " + adj[random.randint(0, len(adj) - 1)], "NHƯ ĐỨC LINH",
                      "templates/template" + str(random.randint(0, 1)) + ".jpg")
        elif adj == '':
            adj = open("adj.txt").read().split('\n')
            make_meme("ƯỚC GÌ " + adj[random.randint(0, len(adj) - 1)], "NHƯ ĐỨC LINH",
                      "templates/" + choice)
        elif choice == 'random':
            make_meme("ƯỚC GÌ " + adj, "NHƯ ĐỨC LINH",
                      "templates/template" + str(random.randint(0, 1)) + ".jpg")
        else:
            make_meme("ƯỚC GÌ " + adj, "NHƯ ĐỨC LINH", "templates/" + choice)
    else:
        adj = open("adj.txt").read().split('\n')
        make_meme("ƯỚC GÌ " + adj[random.randint(0, len(adj) - 1)], "NHƯ ĐỨC LINH",
                  "templates/template" + str(random.randint(0, 1)) + ".jpg")
    return render_template('meme.html', list=open("adj.txt").read().split('\n'))
