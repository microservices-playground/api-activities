import MySQLdb
import yaml


def load_configuration():
    with open('config.yml', 'r') as f:
        config_file = f.read()
    return yaml.load(config_file)


def get_cursor(dbconf):
    db = MySQLdb.connect(host=dbconf.get('hostname'), user=dbconf.get('username'), passwd=dbconf.get('password'),
                         db=dbconf.get('database'))
    return db.cursor()


config = load_configuration()
cursor = get_cursor(config.get('mysql', {}))


