class Development(object):
    """Base configuration"""

    user = 'flask000user'
    password = 'postrootpass'
    hostname = '172.28.0.2'  #環境にあわせて変更
    port = '5432'
    database = 'flask000db'

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class Testing(object):
    user = 'flask000user'
    password = 'postrootpass'
    hostname = '172.28.0.2' #環境にあわせて変更
    port = '5432'
    database = 'flask000db'

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class Production(object):
    """Base configuration"""

    user = ''
    password = ''
    hostname = ''
    port = ''
    database = ''
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc//{user}:{password}@{hostname}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False