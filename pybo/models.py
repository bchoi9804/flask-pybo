from pybo import db

question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model): # 질문 모델 속성
    id = db.Column(db.Integer, primary_key=True) # 데이터 타입_고유 번호와 같은 숫자값에 사용 / 고유 번호 id에 지정한 primary_key는 id 속성을 기본 키로 지정한다.
    #기본 키로 지정하면 중복된 값을 가질 수 없게 된다. 고유 번호는 모델에서 각 데이터를 구분하는 유효한 값으로 중복되면 안 된다. 
    subject = db.Column(db.String(200), nullable=False) # 제목처럼 글자 수가 제한된 텍스트에 사용
    #nullable은 속성에 빈값을 허용할 것인지를 결정한다. 지정하지 않으면 해당 속성은 기본으로 빈값을 허용한다. nullable=False는 속성에 빈값을 허용하지 않는다는 의미
    content = db.Column(db.Text(), nullable=False) # 글 내용처럼 글자 수를 제한할 수 없는 텍스트
    create_date = db.Column(db.DateTime(), nullable=False) # 작성일시는 날짜와 시각에 해당하는 DateTime을 사용
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) #질문모델과 연결(어떤 질문에 대한 답변인지 알아야함), 외부키 사용(질문테이블의 id컬럼의미)
    #ondelete='CASCADE'에 의해 데이터베이스에서 쿼리를 이용하여 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제된다.
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan')) #답변 모델 객체에서 질문 모델 객체의 제목을 참조하려면 db.relationship을 사용해야 함, backref 역참조 
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime())
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id', ondelete='CASCADE'), nullable=True)
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey(
        'answer.id', ondelete='CASCADE'), nullable=True)
    answer = db.relationship('Answer', backref=db.backref('comment_set'))