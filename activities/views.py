from activities import api
from flask_mongorest.methods import *
from flask_mongorest.views import ResourceView
from resources import ActivityResource


@api.register(name='activities', url='/activities')
class ActivityView(ResourceView):
    resource = ActivityResource
    methods = [List]
