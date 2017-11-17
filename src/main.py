from flask import Flask
app = Flask(__name__)

@app.route("/data/")
def retrieve_data():
    return "Hello World!"