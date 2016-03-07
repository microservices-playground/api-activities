import yaml
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mongorest import MongoRest

with open('config.yml', 'r') as f:
    config_file = f.read()

config = yaml.load(config_file)

app = Flask(__name__)
app.debug = config.get('app', {}).get('debug', False)
app.config.update(
    MONGODB_HOST=config.get('mongo', {}).get('hostname'),
    MONGODB_PORT=config.get('mongo', {}).get('port'),
    MONGODB_DB=config.get('mongo', {}).get('database'),
)

db = MongoEngine(app)
api = MongoRest(app)

import activities.views
