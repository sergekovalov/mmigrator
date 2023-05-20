# MongoDb Migrator
Migration engine for MongoDB

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
optional, wil l run automatically on any migration command*
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
```

#### from code:
```py
MigrationManager.migrate()
```


### Revert migrations
#### CLI
```bash
$ mmigrator revert
```

#### from code:
```py
MigrationManager.revert()
```