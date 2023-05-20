import sys
sys.path.append('./')

import os
import json
from src.mmigrator.migration_manager import MigrationManager
from src.mmigrator.constants import CONFIG_FILE_NAME, BASIC_DIST, MIGRATION_TEMPLATE
from dotenv import load_dotenv
import pytest
from helpers import rm_configs, init_config, get_db_connection, TEST_COLLECTION_NAME, TEST_MIGRATION_TEMPLATE

load_dotenv()


@pytest.fixture(autouse=True)
def run_before_and_after_tests(tmpdir):
    rm_configs()

    yield

    rm_configs()


def test_init():
    MigrationManager.init()
    
    assert os.path.exists(CONFIG_FILE_NAME)

    with open(CONFIG_FILE_NAME, 'r') as f:
        cfg = json.loads(f.read())
    
    assert cfg.get('dist') is not None
    assert cfg.get('connection') is not None


def test_create_migration():
    init_config()
    
    MigrationManager().generate('SomeMigration')
    
    file, = [f.rsplit(".")[0] for f in os.listdir(BASIC_DIST)[::-1] if not f.startswith('__')]

    assert file is not None
    
    with open(f'{BASIC_DIST}/{file}.py', 'r') as f:
        mig = f.read()

    assert mig.strip() == MIGRATION_TEMPLATE.strip()


def test_migrate():
    init_config()

    db = get_db_connection()
    
    assert TEST_COLLECTION_NAME not in db.list_collection_names()
    
    MigrationManager().generate('SomeMigration')
    
    file, = [f.rsplit(".")[0] for f in os.listdir(BASIC_DIST)[::-1] if not f.startswith('__')]
    
    with open(f'{BASIC_DIST}/{file}.py', 'w') as f:
        f.write(TEST_MIGRATION_TEMPLATE)
    
    MigrationManager().migrate()
    
    assert TEST_COLLECTION_NAME in db.list_collection_names()


def test_revert():
    init_config()
    
    db = get_db_connection()

    MigrationManager().generate('SomeMigration')
    
    file, = [f.rsplit(".")[0] for f in os.listdir(BASIC_DIST)[::-1] if not f.startswith('__')]
    
    with open(f'{BASIC_DIST}/{file}.py', 'w') as f:
        f.write(TEST_MIGRATION_TEMPLATE)
    
    MigrationManager().migrate()
    
    assert TEST_COLLECTION_NAME in db.list_collection_names()
    
    MigrationManager().revert()
    
    assert TEST_COLLECTION_NAME not in db.list_collection_names()
