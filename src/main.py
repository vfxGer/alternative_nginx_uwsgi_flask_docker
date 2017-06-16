#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask

app = flask.Flask(__name__)


@app.route('/')
def hello():
    return "hello world" 


if __name__ == "__main__":
    app.run('0.0.0.0', 80, debug=True)

