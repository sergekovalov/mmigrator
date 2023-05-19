import os
import json
import shutil
from src.mmigrator.constants import CONFIG_FILE_NAME, BASIC_DIST, MMIGRATOR_COLLECTION
from src.mmigrator.db import connect_db


def get_db_connection():
    return connect_db({
        "host": os.getenv('MONGO_HOST'),
        "port": os.getenv('MONGO_PORT'),
        "database": os.getenv('MONGO_DB'),
        "user": os.getenv('MONGO_USER'),
        "password": os.getenv('MONGO_PASSWORD')
    })


def rm_configs():
    if os.path.exists(BASIC_DIST):
        shutil.rmtree(BASIC_DIST)

    if os.path.exists(CONFIG_FILE_NAME):
        os.unlink(CONFIG_FILE_NAME)
    
    db = get_db_connection()
    db[TEST_COLLECTION_NAME].drop()
    db[MMIGRATOR_COLLECTION].drop()


def init_config():
    with open(CONFIG_FILE_NAME, 'w') as f:
        f.write(json.dumps({
            "dist": BASIC_DIST,
            "connection": {
                "host": os.getenv('MONGO_HOST'),
                "port": os.getenv('MONGO_PORT'),
                "database": os.getenv('MONGO_DB'),
                "user": os.getenv('MONGO_USER'),
                "password": os.getenv('MONGO_PASSWORD')
            }
        }))


TEST_COLLECTION_NAME = 'some_collection'


TEST_MIGRATION_TEMPLATE = f'''
def up(db):
    db.create_collection("{TEST_COLLECTION_NAME}")


def down(db):
    db.drop_collection("{TEST_COLLECTION_NAME}")
'''
