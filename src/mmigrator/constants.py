CONFIG_FILE_NAME = 'mmigrator.config.json'
MMIGRATOR_COLLECTION = '__mmigrator__'

BASIC_DIST = 'migrations'

CONFIG_FILE_TEMPLATE = {
    'dist': BASIC_DIST,
    'connection': {
        'host': '',
        'port': '',
        'database': '',
        'user': '',
        'password': ''
    }
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
