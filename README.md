# MongoDB Migrator
Migration engine for MongoDB

### Supports drivers:
- Pymongo

### Installation

```bash
$ python -m pip install mmigrator
```

### Usage
### CLI

#### Help
```bash
$ mmigrator help
```

#### Init configs
optional, will run automatically on any command*
```bash
$ mmigrator init
```

#### Create migration
```bash
$ mmigrator g SomeName
# or
$ mmigrator new SomeName
```

#### Run migrations
```bash
$ mmigrator migrate
```


#### Revert migrations
```bash
$ mmigrator revert
```

### From code
#### Init configs
```py
from mmigrator import MigrationManager
...
MigrationManager.init()
```

#### Create migration
```py
MigrationManager.generate('SomeName')
```

#### Run migrations
```py
MigrationManager.migrate()
```


#### Revert migrations
```py
MigrationManager.revert()
```