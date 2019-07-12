import os
from os import path

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'as1234df8asdkfj13lik4hjz13kljh4'
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
	# Set config values for Flask-Security.
	# We're using PBKDF2 with salt.
	SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
	SECURITY_PASSWORD_SALT = 'asd8f7asdfkjql3k4jrlkjdlkvia7sd8oruq3kjrnqkljwheflckajsdufiau7sydf'
	SECURITY_POST_LOGIN_VIEW = '/admin'
	AWS_ACCESS_KEY_ID = 'AKIAJJYDSUAAQQIZNGQQ'
	AWS_SECRET_ACCESS_KEY = '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'
	PROJECT_ROOT = path.dirname(__file__)

class DevelopmentConfig(Config):
	S3_BUCKET = "allstaradmin-dev"
	DEVELOPMENT = True
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "postgresql://localhost/allstaradmin_dev"

class StagingConfig(Config):
	S3_BUCKET = "allstaradmin-staging"
	DEVELOPMENT = True
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
	S3_BUCKET = "allstaradmin-production"
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
