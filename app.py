# -*- coding: utf-8 -*-
from zeep import Client
from flask import Flask, request, render_template

#import keyring
import requests
from datetime import datetime, date, time
    
app = Flask(__name__)


@app.route('/')
def index():
    return "ok"

