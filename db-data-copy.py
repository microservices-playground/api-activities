import MySQLdb
import yaml
import progressbar
from pymongo import MongoClient


def load_configuration():
    with open('config.yml', 'r') as f:
        config_file = f.read()
    return yaml.load(config_file)


def get_cursor(dbconf):
    db = MySQLdb.connect(host=dbconf.get('hostname'), user=dbconf.get('username'), passwd=dbconf.get('password'),
                         db=dbconf.get('database'), charset='utf8')
    return db.cursor(MySQLdb.cursors.DictCursor)


def get_legacy_activities(dbcursor):
    query = """
    SELECT
      u.id AS user_id,
      a.date AS created_at,
      IF (a.type != 7, p.username, NULL) AS performed_by,
      IF (a.type != 7, up.value, NULL) AS performer_avatar,
      b.name AS badge_name,
      b.image AS badge_image,
      CASE
        WHEN a.type = 1 THEN 'notification'
        WHEN a.type = 2 THEN 'like'
        WHEN a.type = 3 THEN 'comment'
        WHEN a.type = 4 THEN 'repost'
        WHEN a.type = 5 THEN 'follow'
        WHEN a.type = 6 THEN 'mention'
        WHEN a.type = 7 THEN 'badge'
      END AS type,
      IF(a.type IN (2, 3, 4, 6, 7), a.related_id, NULL) AS post_id,
      pp.value AS post_image,
      a.clicked AS clicked
    FROM activities a
    LEFT JOIN users p ON a.performer_id = p.id
    LEFT JOIN users u ON a.user_id = u.id
    LEFT JOIN users_parameters up ON up.user_id = p.id AND up.parameter_id = 4
    LEFT JOIN posts_parameters pp ON pp.post_id = a.related_id AND pp.parameter_id = 6 AND a.type IN (2, 3, 4, 6, 7)
    LEFT JOIN badges b ON b.id = a.performer_id AND a.type = 7
    """
    dbcursor.execute(query)
    return dbcursor.fetchall()


def get_collection(dbconf):
    client = MongoClient(dbconf.get('hostname'), dbconf.get('port'))
    db = client[dbconf.get('database')]
    db.drop_collection('activities')
    db.create_collection('activities')
    return db.activities


config = load_configuration()
cursor = get_cursor(config.get('mysql', {}))
legacy_activities = get_legacy_activities(cursor)
collection = get_collection(config.get('mongo', {}))
bar = progressbar.ProgressBar()

for row in bar(legacy_activities):
    activity = {
        'user_id': row['user_id'],
        'created_at': row['created_at'],
        'type': row['type'],
        'performed_by': row['performed_by'],
        'performer_avatar': row['performer_avatar']
    }

    if row['type'] in ('like', 'comment', 'repost', 'mention'):
        activity['post_id'] = row['post_id']
        activity['post_image'] = row['post_image']

    if row['type'] == 'badge':
        activity['badge_name'] = row['badge_name']
        activity['badge_image'] = row['badge_image']

    activity['clicked'] = True if row['clicked'] == 1 else False

    collection.insert_one(activity)

print 'Migration successful'
