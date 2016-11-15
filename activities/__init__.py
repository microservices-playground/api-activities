import yaml
from flask import Flask
from mongoalchemy.session import Session
from documents import Activity
from flask_cors import CORS

with open('config.yml', 'r') as f:
    config_file = f.read()

config = yaml.load(config_file)

app = Flask(__name__)
cors = CORS(app)

app.debug = config.get('app', {}).get('debug', False)
app.config['CORS_HEADERS'] = 'Content-Type'

session = Session.connect(config.get('mongo', {}).get('database'), host=config.get('mongo', {}).get('host'))

import activities
import status
