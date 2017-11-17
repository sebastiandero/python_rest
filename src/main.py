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


@app.errorhandler(400)
def badrequest():
    resp_data = jsonify(
        code="400", error="Bad request. Check your request and try again.")
    resp = app.make_response(resp_data)
    resp.mimetype = "application/json"
    return resp


@app.errorhandler(401)
def notfound():
    resp_data = jsonify(
        code="401", error="You are not authorized to access this endpoint. Try authenticating yourself.")
    resp = app.make_response(resp_data)
    resp.mimetype = "application/json"
    return resp


@app.errorhandler(403)
def notfound():
    resp_data = jsonify(
        code="403", error="You are not allowed to access this endpoint.")
    resp = app.make_response(resp_data)
    resp.mimetype = "application/json"
    return resp


@app.errorhandler(404)
def notfound():
    resp_data = jsonify(
        code="404", error="The endpoint you are trying to access does not exist.")
    resp = app.make_response(resp_data)
    resp.mimetype = "application/json"
    return resp


@app.errorhandler(405)
def notfound():
    resp_data = jsonify(
        code="405", error="This HTTP method is not allowed on this endpoint.")
    resp = app.make_response(resp_data)
    resp.mimetype = "application/json"
    return resp
