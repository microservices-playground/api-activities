from flask import jsonify, request
from . import app, session
from documents import Activity
from pymongo import DESCENDING
from flask_cors import cross_origin

PAGE_SIZE = 15


@app.route('/activities')
@cross_origin()
def list_activities():
    try:
        page = int(request.args.get('page', 0))
        assert page >= 0
    except (ValueError, AssertionError):
        page = 0

    activities = session.query(Activity).filter(Activity.user_id == 12).sort((Activity.created_at, DESCENDING)) \
        .limit(PAGE_SIZE).skip(page * PAGE_SIZE)

    meta = {
        'total': activities.count(),
        'offset': page * PAGE_SIZE,
        'count': activities.count(with_limit_and_skip=True)
    }

    # res = [activity.to_dict() for activity in activities]
    res = map(lambda activity: activity.to_dict(), activities)

    return jsonify(results=res, meta=meta)
