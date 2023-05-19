import os
import json
from .constants import CONFIG_FILE_NAME, CONFIG_FILE_TEMPLATE


class ConfigManager(object):
    @staticmethod
    def init_config():
        if not os.path.exists(CONFIG_FILE_NAME):
            conf = json.dumps(CONFIG_FILE_TEMPLATE, indent=4)
            
            with open(CONFIG_FILE_NAME, 'w') as f:
                f.write(conf)

    @staticmethod
    def read_config() -> dict:
        with open(CONFIG_FILE_NAME, 'r') as f:
            return json.loads(f.read())
