# MongoDb Migrator
Migration engine for MongoDB\
Supports CLI

## Installation

```bash
$ python -m pip install mmigrator
```

## Configuration
`init` command (see below) will create a *mmigrator.config.json* file
with following structure:

```json
{
    "dist": "migrations",
    "connection": {
        "host": "",
        "port": "",
        "database": "",
        "user": "",
        "password": ""
    }
}
```
Connection variables could be set from .env|.json files.\
e.g. from .env file:
```json
"host": ".env[MONGO_HOST]",
"port": ".env[MONGO_PORT]",
"database": ".env[MONGO_DB]",
"user": ".env[MONGO_USER]",
"password": ".env[MONGO_PASSWORD]"
```

## Usage

### Help
```bash
$ mmigrator help
```

### Init configs
optional, will run automatically on any migration command*
#### CLI 
```bash
$ mmigrator init
```

#### from code:
```py
from mmigrator import MigrationManager
...
MigrationManager.init()
```

### Create migration
#### CLI
```bash
$ mmigrator g SomeName
# or
$ mmigrator new SomeName
```

#### from code:
```py
MigrationManager.generate("SomeName")
```

### Run migrations
#### CLI
```bash
$ mmigrator migrate
# or add --silent flag for dry-run (skip exceptions)
$ mmigrator migrate --silent
```

#### from code:
```py
MigrationManager.migrate()
# or add silent=True flag for dry-run (skip exceptions)
MigrationManager.migrate(silent=True)

```


### Revert migrations
#### CLI
```bash
$ mmigrator revert
# or add --silent flag for dry-run (skip exceptions)
$ mmigrator revert --silent
```

#### from code:
```py
MigrationManager.revert()
# or add silent=True flag for dry-run (skip exceptions)
MigrationManager.revert(silent=True)
```