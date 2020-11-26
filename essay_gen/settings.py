# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from replit import db
from environs import Env

env = Env()
env.read_env()


ENV = env.str("FLASK_ENV", default="development")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY", default="changeme")
SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT", default=0)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
