from flask import jsonify, request, abort
from . import app, session
from documents import Activity
from pymongo import DESCENDING
from flask_cors import cross_origin
from mongoalchemy.exceptions import BadValueException, BadResultException

USER_ID = 12
PAGE_SIZE = 15


@app.route('/activities')
@cross_origin()
def list_activities():
    try:
        page = int(request.args.get('page', 0))
        assert page >= 0
    except (ValueError, AssertionError):
        page = 0

    activities = session.query(Activity).filter(Activity.user_id == USER_ID).sort((Activity.created_at, DESCENDING)) \
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
@cross_origin()
def patch_activity(activity_id):
    try:
        activity = session.query(Activity).filter(Activity.mongo_id == activity_id, Activity.user_id == USER_ID).one()
    except (BadValueException, BadResultException):
        abort(404)

    activity.clicked = True

    return jsonify(activity.to_dict())
