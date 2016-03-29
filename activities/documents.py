from mongoalchemy.document import Document
from mongoalchemy.fields import *


class Activity(Document):
    config_collection_name = 'activity'
    config_polymorphic = 'type'
    config_polymorphic_collection = True
    config_extra_fields = 'ignore'

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

    def __str__(self):
        return '%s: like by %s' % (self.created_at, self.performed_by)


class Comment(Activity):
    config_polymorphic_identity = 'comment'

    post_id = IntField()
    post_image = StringField()

    def __str__(self):
        return '%s: comment by %s' % (self.created_at, self.performed_by)


class Repost(Activity):
    config_polymorphic_identity = 'repost'

    post_id = IntField()
    post_image = StringField()

    def __str__(self):
        return '%s: repost by %s' % (self.created_at, self.performed_by)


class Follow(Activity):
    config_polymorphic_identity = 'follow'

    def __str__(self):
        return '%s: follow by %s' % (self.created_at, self.performed_by)


class Mention(Activity):
    config_polymorphic_identity = 'mention'

    post_id = IntField()
    post_image = StringField()

    def __str__(self):
        return '%s: mention by %s' % (self.created_at, self.performed_by)


class Badge(Activity):
    config_polymorphic_identity = 'badge'

    badge_name = StringField()
    badge_image = StringField()

    def __str__(self):
        return '%s: badge by %s' % (self.created_at, self.performed_by)
