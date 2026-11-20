from .config import API_KEY_PATTERN_NAME

import os


def get_keys():
    keys = []
    for key in os.environ:
        if API_KEY_PATTERN_NAME in key:
            keys.append(key.split("=", 1))
    return keys
