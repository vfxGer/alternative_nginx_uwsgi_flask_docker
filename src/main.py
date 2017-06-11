#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


import flask
from werkzeug.utils import secure_filename
from PIL import Image

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = '/client_uploads'

app = flask.Flask(__name__)
@app.route('/')
def hello():
    return "hello world" 


if __name__ == "__main__":
    app.run('0.0.0.0', 80, debug=True)
