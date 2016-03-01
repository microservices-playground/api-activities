import yaml
import pymongo
from flask import Flask

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


@app.route("/activities")
def get_activities():
    activities = get_collection('activities').find({"user_id": 12}).sort([
        ("created_at", pymongo.DESCENDING)
    ])

    return "Hello World 123!"

if __name__ == "__main__":
    app.run()
