from logging.config import dictConfig

from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='bx%>q`2vqrH4XTo,>QaO#?:mXwToIoW.',
    url='ls-8b72fae5a481f475a66501e5ffc079873ff4b2cf.cszrrfo7ueks.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x1b\xac\xf9_\xb0\xb1\x84p\xe5\x85\xab0\xba\xc7\xcb\x8c'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5, # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

