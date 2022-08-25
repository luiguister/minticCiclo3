import os

class configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'contraseña'