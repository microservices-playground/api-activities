from flask_mongorest.resources import Resource
from documents import Activity


class ActivityResource(Resource):
    document = Activity
