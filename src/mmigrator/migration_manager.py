import os
from .db import connect_db
from .config_manager import ConfigManager
from .migration import Migration


class MigrationManager(object):
    __db = None
    __config: dict = None
    __schema: dict = None
    __dist: str = None
    __current_migration: str = None
    
    @property
    def current_migration(self):
        return self.__current_migration
    
    @current_migration.setter
    def current_migration(self, new_version):
        self.__schema['current-migration'] = new_version

    def __init__(self):
        MigrationManager.init()
        
        self.__config = ConfigManager.read_config()
        self.__schema = ConfigManager.read_schema()
        
        self.__current_migration = self.__schema['current-migration']

        self.__dist = self.__config['dist']

        if not os.path.exists(self.__dist):
            os.mkdir(self.__dist)

        self.__db = connect_db(self.__config['connection'])
    
    @staticmethod
    def init():
        ConfigManager.init_config()
        ConfigManager.init_schema()

    def __get_files_list(self) -> (list[str], int):
        files = [f.rsplit(".")[0] for f in os.listdir(self.__dist)[::-1] if not f.startswith('__')]
        files = sorted(files, key=lambda x: int(x.split('_', 1)[0]))
        index = files.index(self.current_migration) if self.current_migration in files else -1

        return files, index

    def generate(self, name):
        mig = Migration(name=name, dist=self.__dist)
        mig.generate()
        
        print(f'\nSuccessfully created new migration {mig.name}\n')

    def revert(self):
        files, last_index = self.__get_files_list()
        prev_index = last_index-1
        
        if last_index < 0:
            print('No migrations to revert')
            return
        
        print('Reverting last migration...')

        file = files[last_index]

        mig = Migration(name=file, dist=self.__dist, db=self.__db)
        
        mig.revert()
        
        if last_index > 0:
            print(f'Current migration is...{files[prev_index]}')

        if prev_index > 0:
            self.current_migration = files[prev_index]
        else:
            self.current_migration = None
        
        self.collect_schema()

        ConfigManager.persist_schema(self.__schema)

    def migrate(self):
        files, last_index = self.__get_files_list()
        files = files[last_index + 1:]

        if len(files) == 0:
            print('No migrations to apply')
            return

        print('Running migrations...')

        try:
            for file in files:
                print(f'\tApplying {file}...')
    
                mig = Migration(
                    name=file,
                    dist=self.__dist,
                    db=self.__db
                )
    
                mig.migrate()
    
                self.current_migration = file
                self.collect_schema()
        except Exception as e:
            print(e)
        finally:
            ConfigManager.persist_schema(self.__schema)
    
    def collect_schema(self):
        self.__schema['collections'] = {}
        
        for collection in self.__db.list_collection_names():
            self.__schema['collections'][collection] = {}
