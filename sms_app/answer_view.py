from . import db
from .models import Question, Answer, Instance
from flask import url_for, request, session, Blueprint
from twilio.twiml.messaging_response import MessagingResponse
from .logic import tester

answer_bp = Blueprint('answer_view_bp', __name__, url_prefix = '/answer')

@answer_bp.route('/<question_id>', methods=['POST'])
def answer(question_id):
    question = Question.query.get(question_id)
    
    instance = Instance.query.get(session['instance_id'])

    db.save(Answer(content=extract_content(question),
                   question=question,
                   session_id=session_id(),
                   instance=instance))

    # check if there is a question test
    if question.test != None:
        next_question_id = tester(extract_content(question), question.test, question.yes, question.no)
        print(extract_content(question))
        print(question.test)
        print(question.yes)
        print(question.no)
        print(eval(question.test(extract_content(question))))
        print(next_question_id)
        if next_question_id != 0:
            next_question = Question.query.get(next_question_id)
        else:
            next_question = False
            return goodbye_twiml()
    else:
        next_question = question.next()
    
    if next_question:
        return redirect_twiml(next_question)
    else:
        return goodbye_twiml()

def extract_content(question):
    if is_sms_request():
        return request.values['Body']

def redirect_twiml(question):
    response = MessagingResponse()
    response.redirect(url=url_for('question_view_bp.question', question_id=question.id),
                      method='GET')
    return str(response)

def goodbye_twiml():
    if is_sms_request():
        response = MessagingResponse()
        response.message("Thank you!")
    if 'question_id' in session:
        del session['question_id']
        del session['start_time']
    return str(response)

def is_sms_request():
    return 'MessageSid' in request.values.keys()

def session_id():
    return request.values.get('CallSid') or request.values['MessageSid']
