from . import app, db
from .models import Question, Answer
from flask import url_for, request, session
from twilio.twiml.messaging_response import MessagingResponse

@app.route('/answer/<question_id>', methods=['POST'])
def answer(question_id):
    question = Question.query.get(question_id)

    db.save(Answer(content=extract_content(question),
                   question=question,
                   session_id=session_id()))

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
    response.redirect(url=url_for('question', question_id=question.id),
                      method='GET')
    return str(response)


def goodbye_twiml():
    if is_sms_request():
        response = MessagingResponse()
        response.message("Thanks!")
    if 'question_id' in session:
        del session['question_id']
        del session['start_time']
    return str(response)


def is_sms_request():
    return 'MessageSid' in request.values.keys()

def session_id():
    return request.values.get('CallSid') or request.values['MessageSid']
