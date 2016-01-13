#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2015 Juhua Huang.
# Author: Juhua Huang <hjh.1222@gmail.com>
# Version: : 
# FileName: 
# Date: <2015>
# Description: 


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(r'/signin/index.html')

if __name__ == "__main__":
    app.run()