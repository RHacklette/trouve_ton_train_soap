import os
from zeep import Client
from flask import Flask, request, render_template

#import keyring
import requests
from datetime import datetime, date, time

app = Flask(__name__)


@app.route('/')
def index():
    return "ok"

cmd="/home/$USER/.local/bin/ladon-3.7-ctl testserve SOAPServer.py -p 80"
os.system(cmd)