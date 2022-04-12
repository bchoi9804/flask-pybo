from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

#@bp.route('/')
#def index():
#    return 'Pybo index'

@bp.route('/')
def index():
    #question_list = Question.query.order_by(Question.create_date.desc()) #질문 목록 데이터, 작성일시 기준으로 역순으로 정렬
    #return render_template('question/question_list.html', question_list=question_list) #템플릿파일
    return redirect(url_for('question._list'))

#@bp.route('/detail/<int:question_id>/')
#def detail(question_id):
#    question = Question.query.get_or_404(question_id)
#    return render_template('question/question_detail.html', question=question)