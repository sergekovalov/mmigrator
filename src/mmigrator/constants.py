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
> help                                                                  Get help

> init                                                                  Initialize configs
Optional command. Will run automatically on every migration operation.
Example:
mmigrator init

> [new | g] <migration name>                                            Generate new migration
Example:
mmigrator new Initial
mmigrator g Initial

> migrate                                                               Apply all resting migrations
Example:
mmigrator migrate
You can add --silent flag for dry-run (skip exceptions)
mmigrator migrate --silent

> revert                                                                Revert last migration
Example:
mmigrator revert
You can add --silent flag for dry-run (skip exceptions)
mmigrator revert --silent
'''
