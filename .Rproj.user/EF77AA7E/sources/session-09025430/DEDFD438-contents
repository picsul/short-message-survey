from . import app
from twilio.twiml.messaging_response import MessagingResponse
from .models import Question
from flask import url_for, request, session

@app.route('/question/<question_id>')
def question(question_id):
    question = Question.query.get(question_id)
    session['question_id'] = question.id
    return sms_twiml(question)

def is_sms_request():
    return 'MessageSid' in request.values.keys()

def sms_twiml(question):
    response = MessagingResponse()
    response.message(question.content)
    #response.message(SMS_INSTRUCTIONS[question.kind])
    return str(response)

SMS_INSTRUCTIONS = {
        Question.TEXT: 'Please type your answer',
        Question.BOOLEAN: 'Please type yes or no (or y or n)',
        Question.NUMERIC: 'Please type a number between one and seven'
}
