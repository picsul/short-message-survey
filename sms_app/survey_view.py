from .models import Survey
from flask import url_for, session, request, Blueprint
from sms_app.send_sms import client
from twilio.twiml.messaging_response import MessagingResponse
import random
import pytz
import datetime
from .config import confi

survey_prompt = confi['survey_prompt']
sorry_message = confi['sorry_message']
time_expired = confi['time_expired']
welcome_text = confi['welcome_text']
time_limit = confi['time_limit']

survey_bp = Blueprint('survey_view_bp', __name__, url_prefix = '/survey')

@survey_bp.route('/message')
def sms_survey():
    response = MessagingResponse()
    
    now = datetime.datetime.now(pytz.utc)
    
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

    if (message_text == "Thank you!" or message_text == sorry_message):
       resp = MessagingResponse()
       resp.message(sorry_message)
       return str(resp)
    else:
       if 'question_id' in session:
           delta = now - session['start_time']
           if delta.seconds > time_limit:
               del session['start_time']
               del session['question_id']
               del session['instance_id']
               response.message(time_expired)
           else:
               response.redirect(url_for('answer_view_bp.answer', question_id=session['question_id']))
       else:
           survey = Survey.query.first()

           if survey_error(survey, response.message):
              return str(response)

           welcome_user(survey, response.message)
           redirect_to_first_question(response, survey)
       return str(response)


def redirect_to_first_question(response, survey):
    first_question = survey.questions.order_by('id').first()
    first_question_url = url_for('question_view_bp.question', question_id=first_question.id)
    session['start_time'] = datetime.datetime.now()
    response.redirect(url=first_question_url, method='GET')


def welcome_user(survey, send_function):
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
@survey_bp.route('/static')
def sms_static():
    resp = MessagingResponse()
    
    resp.message(sorry_message)
    
    return str(resp)
