from flask import Flask
from flask import Response
from flask import json
from flask import jsonify
app = Flask(__name__)


@app.route("/data/", methods=['GET'])
def data():
    resp_data = jsonify(message="Hello, World!")
    resp = app.make_response(resp_data)
    resp.mimetype = "application/json"
    return resp
