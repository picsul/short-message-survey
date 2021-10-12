from . import app
from .models import Survey
from flask import url_for, session
from twilio.twiml.messaging_response import MessagingResponse
import random

@app.route('/message')
def sms_survey():
    response = MessagingResponse()

    #survey = Survey.query.first()
    survey = Survey.query.get(random.randint(1,4))
    
    if survey_error(survey, response.message):
        return str(response)

    if 'question_id' in session:
        response.redirect(url_for('answer',
                                  question_id=session['question_id']))
    else:
        welcome_user(survey, response.message)
        redirect_to_first_question(response, survey)
    return str(response)


def redirect_to_first_question(response, survey):
    first_question = survey.questions.order_by('id').first()
    first_question_url = url_for('question', question_id=first_question.id)
    response.redirect(url=first_question_url, method='GET')


def welcome_user(survey, send_function):
    welcome_text = "Please respond to the following items on a scale of strongly disagree to strongly agree (1-7)."
    send_function(welcome_text)

def survey_error(survey, send_function):
    if not survey:
        send_function('Sorry, but there are no surveys to be answered.')
        return True
    elif not survey.has_questions:
        send_function('Sorry, there are no questions for this survey.')
        return True
    return False

# Static Response 
@app.route('/static')
def sms_static():
    resp = MessagingResponse()
    
    resp.message("Please use the link above to access the survey.")
    
    return str(resp)
