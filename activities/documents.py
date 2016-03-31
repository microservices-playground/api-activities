from mongoalchemy.document import Document
from mongoalchemy.fields import *


class Activity(Document):
    config_collection_name = 'activity'
    config_polymorphic = 'type'
    config_polymorphic_collection = True

    type = StringField()
    created_at = DateTimeField()
    clicked = BoolField()
    user_id = IntField()


class Like(Activity):
    config_polymorphic_identity = 'like'

    performed_by = StringField()
    performer_avatar = StringField()
    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'id': self.mongo_id.__str__(),
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

    performed_by = StringField()
    performer_avatar = StringField()
    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'id': self.mongo_id.__str__(),
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

    performed_by = StringField()
    performer_avatar = StringField()
    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'id': self.mongo_id.__str__(),
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

    performed_by = StringField()
    performer_avatar = StringField()

    def to_dict(self):
        return {
            'id': self.mongo_id.__str__(),
            'type': self.type,
            'performed_by': self.performed_by,
            'performer_avatar': self.performer_avatar,
            'created_at': self.created_at.isoformat(),
            'clicked': self.clicked
        }


class Mention(Activity):
    config_polymorphic_identity = 'mention'

    performed_by = StringField()
    performer_avatar = StringField()
    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'id': self.mongo_id.__str__(),
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
    post_id = IntField()
    post_image = StringField()

    def to_dict(self):
        return {
            'id': str(self.mongo_id),
            'type': self.type,
            'badge_name': self.badge_name,
            'badge_image': self.badge_image,
            'post_id': self.post_id,
            'post_image': self.post_image,
            'created_at': self.created_at.isoformat(),
            'clicked': self.clicked
        }
