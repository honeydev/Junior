"""Модуль настроек проекта."""

import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    APP_NAME = os.getenv('APP_NAME', 'Junior')
    DEBUG = os.getenv('DEBUG', False)
    CSRF_ENABLED = os.getenv('CSRF_ENABLED', True)
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY', 'dsofpkoasodksap')
    SECRET_KEY = os.getenv('SECRET_KEY', 'SOSECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 'postgres://junior:junior@127.0.0.1:5432/junior',
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    OAUTH_BACKEND = os.getenv('OAUTH_BACKEND', '').split()


class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    extend_existing = True


class TestConfig(ProductionConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite://')
    OAUTH_BACKEND = os.getenv('TEST_OAUTH_BACKEND', 'github').split()
