from mongoalchemy.document import Document
from mongoalchemy.fields import *


class Activity(Document):
    config_collection_name = 'activity'
    config_polymorphic = 'type'
    config_polymorphic_collection = True

    type = StringField()
    performed_by = StringField()
    performer_avatar = StringField()
    created_at = DateTimeField()
    clicked = BoolField()
    user_id = IntField()

    def __str__(self):
        return '%s: activity by %s' % (self.created_at, self.performed_by)


class Like(Activity):
    config_polymorphic_identity = 'like'

    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'type': self.type,
            'performed_by': self.performed_by,
            'performer_avatar': self.performer_avatar,
            'post_id': self.post_id,
            'post_image': self.post_image,
            'created_at': self.created_at.isoformat(),
            'clicked': self.clicked
        }


class Comment(Activity):
    config_polymorphic_identity = 'comment'

    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'type': self.type,
            'performed_by': self.performed_by,
            'performer_avatar': self.performer_avatar,
            'post_id': self.post_id,
            'post_image': self.post_image,
            'created_at': self.created_at.isoformat(),
            'clicked': self.clicked
        }


class Repost(Activity):
    config_polymorphic_identity = 'repost'

    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'type': self.type,
            'performed_by': self.performed_by,
            'performer_avatar': self.performer_avatar,
            'post_id': self.post_id,
            'post_image': self.post_image,
            'created_at': self.created_at.isoformat(),
            'clicked': self.clicked
        }


class Follow(Activity):
    config_polymorphic_identity = 'follow'

    def to_dict(self):
        return {
            'type': self.type,
            'performed_by': self.performed_by,
            'performer_avatar': self.performer_avatar,
            'created_at': self.created_at.isoformat(),
            'clicked': self.clicked
        }


class Mention(Activity):
    config_polymorphic_identity = 'mention'

    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'type': self.type,
            'performed_by': self.performed_by,
            'performer_avatar': self.performer_avatar,
            'post_id': self.post_id,
            'post_image': self.post_image,
            'created_at': self.created_at.isoformat(),
            'clicked': self.clicked
        }


class Badge(Activity):
    config_polymorphic_identity = 'badge'

    badge_name = StringField()
    badge_image = StringField()

    def to_dict(self):
        return {
            'type': self.type,
            'performed_by': self.performed_by,
            'performer_avatar': self.performer_avatar,
            'badge_name': self.badge_name,
            'badge_image': self.badge_image,
            'created_at': self.created_at.isoformat(),
            'clicked': self.clicked
        }
