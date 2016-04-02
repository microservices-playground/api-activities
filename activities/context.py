from flask import request, abort
from functools import wraps


def user_context(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        user_id = request.headers.get('X-Foodlove-User-Id', None)

        if user_id is not None:
            return function(user_id=int(user_id), *args, **kwargs)
        else:
            abort(401)
    return decorated_function
