#from . import app
#from . import question_view
#from . import answer_view
from . import survey_view
from flask import render_template, Blueprint
from .models import Question

bp = Blueprint('survey', __name__)

# change this to current app if it doesn't work
@bp.route('/')
def root():
    questions = Question.query.all()
    return render_template('index.html', questions=questions)
