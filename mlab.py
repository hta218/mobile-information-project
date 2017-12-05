import mongoengine

# mongodb://admin:admin@ds129776.mlab.com:29776/thongtindidong
host = "ds129776.mlab.com"
port = 29776
db_name = "thongtindidong"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
