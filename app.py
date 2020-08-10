#!/usr/bin/python

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    # Response,
    redirect,
    url_for,
    session,
)
import os

app = Flask(__name__)
app.secret_key = "eipohgoo4rai0uf5ie1oshahmaeF"


# Routes of my application
@app.route("/")
def index():
    application_version = os.getenv("APP_VERSION" , "1.0")
    return jsonify({"app_version" : application_version})


# Routes of my application
@app.route("/health")
def health():
    return jsonify({"healthchek" : "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)