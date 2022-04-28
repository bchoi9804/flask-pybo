from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x1b\xac\xf9_\xb0\xb1\x84p\xe5\x85\xab0\xba\xc7\xcb\x8c'