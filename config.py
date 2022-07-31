# Это файл конфигурации приложения


class Config(object):
    DEBUG = True
    #SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}

