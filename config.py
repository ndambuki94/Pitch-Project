import os
from flask import Flask

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:future2019@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/images'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = 'nzilani94'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:future2019@localhost/pitches'
    DEBUG = True

class TestConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    }
