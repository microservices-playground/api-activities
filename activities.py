import yaml
import pymongo
from flask import Flask, Response
from bson.json_util import dumps

app = Flask(__name__)
app.debug = True

with open('config.yml', 'r') as f:
    config_file = f.read()

config = yaml.load(config_file)


def get_collection(collection_name):
    mongo_config = config.get('mongo', {})
    client = pymongo.MongoClient(mongo_config.get('hostname'), mongo_config.get('port'))
    db = client[mongo_config.get('database')]
    return db[collection_name]

# date               : '',
# performer_id       : '',
# performer_username : '',
# performer_avatar   : '',
# type               : '',
# related_id         : '',
# related_image      : '',
# info               : '',
# clicked            : ''
@app.route("/activities")
def get_activities():
    cursor = get_collection('activities').find({"user_id": 12}, {"_id": 0, "user_id": 0}).sort([
        ("created_at", pymongo.DESCENDING)
    ])

    return Response(dumps(cursor), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()
