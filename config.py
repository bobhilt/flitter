import os

class Config(object):
    SECRET_KEY = os.environ.get('FLITTER_SECRET_KEY') or 'notso_secret'
