import os
import json
import re
from ..process import process
from ..constants import CONFIG_FILE_NAME, CONFIG_FILE_TEMPLATE
from .helpers import load_var


class ConfigManager(object):
    @staticmethod
    def init_config():
        @process('Initializing configs')
        def init():
            conf = json.dumps(CONFIG_FILE_TEMPLATE, indent=4)
            
            with open(CONFIG_FILE_NAME, 'w') as f:
                f.write(conf)
            
        if not os.path.exists(CONFIG_FILE_NAME):
            init()

    @staticmethod
    def read_config():
        with open(CONFIG_FILE_NAME, 'r') as f:
            cfg = json.loads(f.read())

        for k, v in cfg['connection'].items():
            if v and re.match(r'^.+\[.+\]$', v):
                file, var = re.sub(r'[\[\]]', ' ', v).strip().split(' ')
                cfg['connection'][k] = load_var(file, var)

        return cfg

    @staticmethod
    def init_dist(dist):
        if not os.path.exists(dist):
            os.mkdir(dist)
