from . import app
from .models import Survey
from flask import url_for, session, request
from sms_app.send_sms import client
from twilio.twiml.messaging_response import MessagingResponse
import random

survey_prompt = "Ready to take the BIOL 102/150/160 survey? Please respond with 'y' or 'yes' when you are ready to begin."
sorry_message = "If you have any issues with the survey, please contact us at jmrosenberg@utk.edu."

@app.route('/message')
def sms_survey():
    response = MessagingResponse()
    
    from_num = request.values['From']
    to_num = request.values['To']
    #print(request)
       
    # Get the message most recently sent from us
    messages = client.messages.list(from_=to_num, to=from_num, limit=1)
    message_text = messages[0].body
    print(messages[0].body)
    
    if message_text == survey_prompt:
        if 'question_id' in session:
            del session['question_id']
        if 'start_time' in session:
            del session['start_time']
    
    if message_text == "Thank you!" or message_text = sorry_message:
        resp = MessagingResponse()
        resp.message(sorry_message)
        return str(resp)
    else:
        if 'question_id' in session:
            response.redirect(url_for('answer',
                                  question_id=session['question_id']))
        else:
            survey = Survey.query.get(random.randint(1,4))
    
            if survey_error(survey, response.message):
                return str(response)
            
            welcome_user(survey, response.message)
            redirect_to_first_question(response, survey)
        return str(response)


def redirect_to_first_question(response, survey):
    first_question = survey.questions.order_by('id').first()
    first_question_url = url_for('question', question_id=first_question.id)
    response.redirect(url=first_question_url, method='GET')


def welcome_user(survey, send_function):
    welcome_text = "Please respond with your agreement to the following statement on a scale from strongly disagree (1) to strongly agree (7)."
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
    
    resp.message("If you have any issues with the survey, please contact us at jmrosenberg@utk.edu.")
    
    return str(resp)
