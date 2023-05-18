CONFIG_FILE_NAME = 'mmigrator.config.json'
CONFIG_FILE_TEMPLATE = {
    'dist': 'migrations',
    'connection': {
        'host': '',
        'port': '',
        'database': '',
        'user': '',
        'password': ''
    }
}

SCHEMA_FILE_NAME = 'mmigrator.schema.json'
SCHEMA_FILE_TEMPLATE = {
    'current-migration': None,
    'collections': {}
}


MIGRATION_TEMPLATE = '''
def up(db):
    pass


def down(db):
    pass
'''


HELP_TEMPLATE = '''
Available commands:
> help                                   Get help

> [new | g] <migration name>             Generate new migration
Example:
mmigrator new Initial
mmigrator g Initial

> migrate                                Apply all resting migrations
Example:
mmigrator migrate

> revert                                 Revert last migration
Example:
mmigrator revert
'''