#!/usr/lib/python3
from flask import Flask, request, jsonify
import time
import subprocess, string
import numpy as np

app = Flask(__name__)


@app.route("/whoami")
def whoami():
    ip_address = request.remote_addr
    time_on_server = time.strftime('%H:%M:%S %d %B %Y ')
    user_browser = request.user_agent.browser
    return f"""Clients browser: {user_browser},
                Requester IP: {ip_address}, 
                Time: {time_on_server}"""


@app.route("/random")
def length():
    a = request.args.get('length', type=int)
    special = request.args.get('specials', default=False, type=bool)
    digits = request.args.get('digits', default=False, type=bool)
    if a in range(1, 100):
        gen_string = string.ascii_uppercase
    if special is True:
        gen_string += '!"№;%:?*()_+'
    if digits is True:
        gen_string += '0123456789'
    random_symbols = np.random.randint(1, len(gen_string), a)

    return ''.join([gen_string[i] for i in random_symbols])


@app.route("/source_code")
def source_code():
    WORDS = []
    file = open('dz4.py')
    for line in file.readlines():
        WORDS.append(line.rstrip())
    words = [word for word in WORDS]
    return jsonify(words)


app.run(debug=True)
