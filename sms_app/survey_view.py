from . import app
from .models import Survey
from flask import url_for, session, request
from twilio.twiml.messaging_response import MessagingResponse
from sms_app.send_sms import client
from sms_app.scan_email import survey_prompt, welcome_message
import datetime

@app.route('/message')
def sms_survey():
    response = MessagingResponse()
    
    now = datetime.datetime.now()
    
    # Get the to/from numbers from the latest request
    from_num = request.values['From']
    to_num = request.values['To']
       
    # Get the message most recently sent from us
    messages = client.messages.list(from_=to_num, to=from_num, limit=1)
    message_text = messages[0].body
        
    # new code with 5 minute time limit, and reprompt reset

    if message_text == survey_prompt:
        if 'instance_id' in session:
            del session['instance_id']
        if 'question_id' in session:
            del session['question_id']
        if 'start_time' in session:
            del session['start_time']
        session['instance_id'] = messages[0].sid

    if 'question_id' in session:
        delta = now - session['start_time']
        if delta.seconds > 300:
            del session['start_time']
            del session['question_id']
            del session['instance_id']
            response.message("The time to complete the survey has expired")
        else:
            response.redirect(url_for('answer', question_id=session['question_id']))
    else:
        survey = Survey.query.first()
            
        if survey_error(survey, response.message):
            return str(response)
        
        welcome_user(survey, response.message)
        redirect_to_first_question(response, survey)
    return str(response)

def redirect_to_first_question(response, survey):
    first_question = survey.questions.order_by('id').first()
    first_question_url = url_for('question', question_id=first_question.id)
    session['start_time'] = datetime.datetime.now()
    response.redirect(url=first_question_url, method='GET')

def welcome_user(survey, send_function):
    welcome_text = welcome_message
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
    
    resp.message("If you have any issues accessing the survey, please contact us at jmrosenberg@utk.edu")
    
    return str(resp)
    
