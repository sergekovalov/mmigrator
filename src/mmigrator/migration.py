from importlib import util
import snakecase
import sys
import os
from datetime import datetime
from .constants import MIGRATION_TEMPLATE


class Migration(object):
    __name = None
    __filename = None
    __db = None
    __dist = None

    @property
    def name(self):
        return self.__name

    def __init__(self, name, dist, db=None):
        self.__name = name
        self.__dist = dist
        self.__filename = f'{os.getcwd()}/{dist}/{name}.py'
        self.__db = db

    def generate(self):
        self.__name = f'{self.__get_time_mark()}_{snakecase.convert(self.__name)}'

        with open(f'{self.__dist}/{self.__name}.py', 'w') as file:
            file.write(MIGRATION_TEMPLATE.strip() + '\n')
    
    def __get_time_mark(self):
        d = datetime.now()
        month = f'{"0" if d.month < 10 else ""}{d.month}'
        day = f'{"0" if d.day < 10 else ""}{d.day}'
        hour = f'{"0" if d.hour < 10 else ""}{d.hour}'
        minute = f'{"0" if d.minute < 10 else ""}{d.minute}'
        second = f'{"0" if d.second < 10 else ""}{d.second}'
        
        return f'{d.year}{month}{day}{hour}{minute}{second}'
    
    def __load_func(self, func_name):
        spec = util.spec_from_file_location(self.__dist, self.__filename)
        module = util.module_from_spec(spec)
        sys.modules[self.__dist] = module
        spec.loader.exec_module(module)
        func = getattr(module, func_name)
        
        return func
    
    def migrate(self, silent=False):
        try:
            up = self.__load_func('up')

            up(self.__db)
        except Exception as e:
            if not silent:
                raise Exception(f'Error: {str(e)}')
    
    def revert(self, silent=False):
        try:
            down = self.__load_func('down')

            down(self.__db)
        except Exception as e:
            if not silent:
                raise Exception(f'Error: {str(e)}')
