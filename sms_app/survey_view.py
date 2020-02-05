from . import app
from .models import Survey
from flask import url_for, session, request
from twilio.twiml.messaging_response import MessagingResponse

@app.route('/message')
def sms_survey():
    response = MessagingResponse()

    survey = Survey.query.first()
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
    #welcome_text = 'Welcome to the %s' % survey.title
    welcome_text = 'Please answer the following 4 questions on your feelings about COSC 102 on a scale of 1 - 5: 1 = not at all, 5 = a lot' 
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
    
    mess = request.values['Body']
    
    mess = mess.strip().upper()
    
    if mess not in ['A', 'B', 'C', 'D']:
         resp.message("Please respond with A, B, C, or D")
         return str(resp)
    else:
        resp.message("Thanks for providing that information!")
        return str(resp)
