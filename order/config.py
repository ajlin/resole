import os
from collections import namedtuple

# NB: variables are stored as dictionaries in order to prioritize environment variables

# tup for prioritize_env_variables(). first val looks for env variable, second is hard coded
EnvironmentVariable = namedtuple('EnvironmentVariable','external internal')

# get env var else use internal var
def ConfigVar(external,internal):
    # get environmental var named `external`, else use `internal`
    # could do this w/a namedtuple and an iteration over vars(Config) if i need a custom datatype for whatever reason
    return os.environ.get(external) or internal

class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # gets environment variable SECRET_KEY or defaults to hard coded string
    # os.environ.get('SECRET_KEY') or 'this is my secret key'
    SECRET_KEY = ConfigVar(
        external = 'SECRET_KEY',
        internal = 'this is my secret key'
    )

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

class DevConfig(Config):
    DEBUG = True
    HOST = ConfigVar(
        external = 'HOST',
        internal = '0.0.0.0'
    )
    PORT = ConfigVar(
        external = 'PORT',
        internal = 8080
    )

    # local sqlite
    DB_NAME = 'orders.db'
    SQLALCHEMY_DATABASE_URI = ConfigVar(
        external = 'DATABASE_URL',
        internal = 'sqlite:///' + os.path.join(BASE_DIR, DB_NAME)

    DATABASE_CONNECT_OPTIONS = {}

    # local uploads
    UPLOADED_PHOTOS_DEST = ConfigVar(
        external = 'UPLOAD_DIR',
        internal = os.path.join(basedir, 'uploads')

class ProductionConfig(Config):
    # HOST, PORT, SECRET_KEY handling, db connection, ...
    # upload connection better handled via environment vars?  dunno what to do here