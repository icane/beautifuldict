"""Unit tests for class Baseconfig."""

import pytest
from beautifuldict.baseconfig import Baseconfig

BASE_PATH = {
    'base_path': 'beautifuldict/test/'
}

DB_CONFIG = {
    'db': {
        'mysql': {
            'host': 'localhost',
            'port': '3306',
            'database': 'test',
            'user': 'test',
            'password': 'xyz'
        }
    }
}
FILE_CONFIG = {
    'file': {
        'input': {
            'path': 'data/input/',
            'filemask': '*.txt'
        },
        'output': {
            'path': 'data/output',
        },
        'sql': {
            'path': 'sql/',
            'filemask': '*.sql'
        }
    }
}


def test_init():
    """Check if an instance is correctly initialized."""
    config = Baseconfig(BASE_PATH)
    assert config.base_path == 'beautifuldict/test/'


def test_add():
    """Check if a configuration variable is correctly added."""
    config = Baseconfig(BASE_PATH)
    config.add(DB_CONFIG)
    config.add(FILE_CONFIG)
    assert config.db.mysql.port == '3306'
    assert config.db.mysql['port'] == '3306'
    assert config.file.input.path == 'data/input/'
    assert config.file.input['path'] == 'data/input/'


def test_clean():
    """Check if a configuration variable is correctly removed."""
    config = Baseconfig(BASE_PATH)
    config.add(DB_CONFIG)
    assert config.db is not None
    config.clean('db')
    assert config == {'base_path': 'beautifuldict/test/'}


if __name__ == '__main__':
    pytest.main()
