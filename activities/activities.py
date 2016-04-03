from flask import jsonify, request, abort
from . import app, session
from documents import Activity
from pymongo import DESCENDING
from flask_cors import cross_origin
from mongoalchemy.util import FieldNotFoundException
from mongoalchemy.exceptions import BadValueException
from context import user_context

PAGE_SIZE = 15


@app.route('/activities')
@cross_origin(methods=['GET'])
@user_context
def list_activities(user_id):
    try:
        page = int(request.args.get('page', 0))
        assert page >= 0
    except (ValueError, AssertionError):
        page = 0

    activities = session.query(Activity).filter(Activity.user_id == user_id).sort((Activity.created_at, DESCENDING)) \
        .limit(PAGE_SIZE).skip(page * PAGE_SIZE)

    meta = {
        'total': activities.count(),
        'offset': page * PAGE_SIZE,
        'count': activities.count(with_limit_and_skip=True)
    }

    # res = [activity.to_dict() for activity in activities]
    res = map(lambda activity: activity.to_dict(), activities)

    return jsonify(results=res, meta=meta)


@app.route('/activities/<activity_id>', methods=['PATCH'])
@cross_origin(methods=['PATCH'])
@user_context
def patch_activity(user_id, activity_id):
    try:
        # TODO introduce validation or json schema
        query = session.query(Activity).filter(Activity.mongo_id == activity_id, Activity.user_id == user_id)
        query.set(**request.json).execute()

        return jsonify(query.one().to_dict())
    except (FieldNotFoundException, BadValueException):
        abort(400)
