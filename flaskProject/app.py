#!/usr/lib/python3
import string
import time

import numpy as np
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index1.html")


@app.route("/whoami", methods=['POST', 'GET'])
def whoami():
    ip_address = request.remote_addr
    time_on_server = time.strftime('%H:%M:%S %d %B %Y ')
    user_browser = request.user_agent.browser
    return render_template('index.html', ip_address=ip_address, time_on_server=time_on_server,
                           user_browser=user_browser)


@app.route("/random", methods=['POST', 'GET'])
def length():
    global gen_string
    length = request.args.get('length', type=int)
    specials = request.args.get('specials', type=int)
    digits = request.args.get('digits', type=int)
    if length in range(1, 100):
        gen_string = string.ascii_uppercase
    if specials == 1:
        gen_string += '!"№;%:?*()_+'
    if digits == 1:
        gen_string += '0123456789'
    random_symbols = np.random.randint(1, len(gen_string), length)
    symbols = ''.join([gen_string[i] for i in random_symbols])
    return render_template('index3.html', symbols=symbols)


@app.route("/source_code", methods=['POST', 'GET'])
def source_code():
    WORDS = []
    file = open('app.py')
    for line in file.readlines():
        WORDS.append(line.rstrip())
    words = [word for word in WORDS]
    return render_template('index2.html', jsonfile=json.dumps(words))


app.run(debug=True)
