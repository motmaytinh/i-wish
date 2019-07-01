from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from memgenerator import make_meme
import random
import base64

app = Flask(__name__)

ADJ = open("adj.txt").read().split('\n')
WISH = "ƯỚC GÌ "
LIKE_SOMEONE = "NHƯ ĐỨC LINH"

@app.route('/', methods=['GET'])
def index():
    # adj = open("adj.txt").read().split('\n')
    # make_meme("ƯỚC GÌ " + adj[random.randint(0, len(adj) - 1)], "NHƯ ĐỨC LINH",
    #             "templates/template" + str(random.randint(0, 2)) + ".jpg")
    return render_template('meme.html', list=ADJ)


@app.route('/gen_meme', methods=['POST'])
def gen_meme():
    data = request.get_json()
    try:
        adj = data['text']
        template = data['template']
    except KeyError:
        adj = ''
        template = 'random'

    ret = ''

    if template == 'random' and adj == '':
        ret = make_meme(WISH + ADJ[random.randint(0, len(ADJ) - 1)], LIKE_SOMEONE,
                    "templates/template" + str(random.randint(0, 2)) + ".jpg")
    elif adj == '':
        ret = make_meme(WISH + ADJ[random.randint(0, len(ADJ) - 1)], LIKE_SOMEONE,
                    "templates/" + template)
    elif template == 'random':
        ret = make_meme(WISH + adj, LIKE_SOMEONE,
                    "templates/template" + str(random.randint(0, 2)) + ".jpg")
    else:
        ret = make_meme(WISH + adj, LIKE_SOMEONE, "templates/" + template)

    return jsonify({'meme': str(ret)})