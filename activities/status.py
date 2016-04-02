from flask import jsonify
from . import app, session
from flask_cors import cross_origin


@app.route('/status')
@cross_origin()
def get_status():
    return jsonify(new_activities=3)


@app.route('/status', methods=['PUT'])
@cross_origin()
def put_status():
    return jsonify(new_activities=0)
