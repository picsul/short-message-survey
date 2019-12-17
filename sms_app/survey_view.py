from . import app
from .models import Survey
from flask import url_for, session, request
from twilio.twiml.messaging_response import MessagingResponse
from sms_app.send_sms import client

@app.route('/message')
def sms_survey():
    response = MessagingResponse()

    #survey = Survey.query.first()
    
    #print(from_num)
    #print(to_num)
    #print(message_text)
    #print(survey)
    #print('question_id' in session)

    if survey_error(survey, response.message):
        return str(response)

    if 'question_id' in session:
        response.redirect(url_for('answer',
                                  question_id=session['question_id']))
    else:
        from_num = request.values['From']
        to_num = request.values['To']
        
        messages = client.messages.list(from_=to_num, to=from_num, limit=1)
        message_text = messages[0].body
        
        if message_text == "Ready to take survey 1?":
            survey = Survey.query.get(1)
        elif message_text == "Ready to take survey 2?":
            survey = Survey.query.get(2)
        else:
            print("Sorry couldn't figure it out")
        
        welcome_user(survey, response.message)
        redirect_to_first_question(response, survey)
    return str(response)


def redirect_to_first_question(response, survey):
    first_question = survey.questions.order_by('id').first()
    first_question_url = url_for('question', question_id=first_question.id)
    response.redirect(url=first_question_url, method='GET')


def welcome_user(survey, send_function):
    welcome_text = 'Welcome to the %s' % survey.title
    send_function(welcome_text)

def survey_error(survey, send_function):
    if not survey:
        send_function('Sorry, but there are no surveys to be answered.')
        return True
    elif not survey.has_questions:
        send_function('Sorry, there are no questions for this survey.')
        return True
    return False
