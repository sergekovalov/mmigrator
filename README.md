# MongoDB Migrator
Migration engine for MongoDB

### Supports drivers:
- Pymongo

### Installation

```bash
$ python -m pip install mmigrator
```

### Usage
### From code
#### Init configs
```py
from mmigrator import MigrationManager
...
MigrationManager.init()
```

#### Create migration
```py
from mmigrator import MigrationManager
...
MigrationManager.generate('SomeName')
```

#### Run migrations
```py
from mmigrator import MigrationManager
...
MigrationManager.migrate()
```


#### Revert migrations
```py
from mmigrator import MigrationManager
...
MigrationManager.revert()
```