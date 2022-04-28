from config.default import * #config/default.py파일에 정의되어 있는 모든 내용을 사용한다는 의미다.
#즉 development.py에서 default.py의 환경변수의 값을 그대로 사용할 수 있다.

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"