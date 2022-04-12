import os
#pybo.db라는 데이터베이스 파일을 프로젝트의 루트 디렉터리에 저장하려는 것이다.

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db')) #데이터베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False #이벤트 처리옵션 -> 비활성화
SECRET_KEY = "dev" #플라스크 환경 변수 SECRET_KEY