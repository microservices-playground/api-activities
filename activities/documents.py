from mongoengine import *


class Activity(Document):
    type = StringField()
    performed_by = StringField()
    performer_avatar = StringField()
    created_at = DateTimeField()
    post_id = IntField()
    post_image = StringField()
    badge_name = StringField()
    badge_image = StringField()
    clicked = BooleanField()
    user_id = IntField()
