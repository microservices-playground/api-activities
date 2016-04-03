from flask import jsonify, request, abort
from . import app, session
from flask_cors import cross_origin
from documents import Status
from mongoalchemy.util import FieldNotFoundException
from mongoalchemy.exceptions import BadValueException, BadResultException
from context import user_context


@app.route('/status')
@cross_origin(methods=['GET', 'PUT'])
@user_context
def get_status(user_id):
    try:
        status = session.query(Status).filter(Status.user_id == user_id).one()
    except BadResultException:
        status = Status(user_id=user_id, new_activities=0)
        session.save(status)

    return jsonify(status.to_dict())


@app.route('/status', methods=['PUT'])
@cross_origin(methods=['GET', 'PUT'])
@user_context
def put_status(user_id):
    try:
        # TODO introduce validation or json schema
        query = session.query(Status).filter(Status.user_id == user_id)
        query.set(**request.json).execute()

        return jsonify(query.one().to_dict())
    except (FieldNotFoundException, BadValueException):
        abort(400)
