#!/usr/bin/env python3

import sys
from .migration_manager import MigrationManager
from .constants import HELP_TEMPLATE


args = sys.argv[1:]


def get_args_with_option(option):
    arg, *opt = args

    if len(opt) and opt[0] != option:
        raise Exception(f'Unrecognized parameter {opt}')

    return arg, opt[0] if len(opt) else None


def main():
    if len(args) == 0:
        exit()
    
    if args[0] == 'help':
        print(HELP_TEMPLATE)
    
    elif args[0] == 'init':
        MigrationManager.init()
    
    elif args[0] in ['new', 'g']:
        MigrationManager().generate(args[1])
    
    elif args[0] == 'migrate':
        _, run_silently = get_args_with_option('--silent')

        MigrationManager().migrate(silent=bool(run_silently))
    
    elif args[0] == 'revert':
        _, run_silently = get_args_with_option('--silent')

        MigrationManager().revert(silent=bool(run_silently))
