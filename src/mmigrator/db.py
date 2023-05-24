import pymongo


def connect_db(connection):
    mongo_user = connection['user']
    mongo_db = connection['database']
    mongo_password = connection['password']
    mongo_host = connection['host']
    mongo_port = connection['port']

    if not (mongo_host or mongo_port or mongo_port):
        raise Exception('MongoDb credentials must be provided')
    
    mongo_auth = f'{mongo_user}:{mongo_password}@' if mongo_user and mongo_password else ''
    
    connection_string = f'mongodb://{mongo_auth}{mongo_host}:{mongo_port}/{mongo_db}'

    client = pymongo.MongoClient(connection_string, int(mongo_port))[mongo_db]
    
    return client
