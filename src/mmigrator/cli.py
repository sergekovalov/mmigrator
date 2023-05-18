#!/usr/bin/python

import sys
from .migration_manager import MigrationManager
from .constants import HELP_TEMPLATE

args = sys.argv[1:]


if __name__ == '__main__':
    if len(args) == 0:
        exit()
    
    if args[0] == 'help':
        print(HELP_TEMPLATE)
    
    elif args[0] == 'init':
        MigrationManager.init()
    
    elif args[0] in ['new', 'g']:
        MigrationManager().generate(args[1])
    
    elif args[0] == 'migrate':
        MigrationManager().migrate()
    
    elif args[0] == 'revert':
        MigrationManager().revert()
