# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('{{cookiecutter.app_name | upper}}_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'project1',
        'host': 'mongodb://localhost/prod'
    }

class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    MONGODB_SETTINGS = {
        'db': 'project1',
        'host': 'mongodb://localhost/dev1'
    }
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'project1',
        'host': 'mongodb://localhost/test'
    }
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
