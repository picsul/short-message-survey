from .config import confi
from .models import Survey, Controller, Number
from .answer_view import extract_content
from flask import url_for, session, request, Blueprint
from sms_app.send_sms import client
from twilio.twiml.messaging_response import MessagingResponse
import os

control_bp = Blueprint('control_view_bp', __name__, "/control")
controller_message = confi['controller_message']
survey_prompt = confi['survey_prompt']
phone_number = confi['phone_number']

@control_bp.route('/routing')
def control():
    from_num = request.values['From']
    
    response = MessagingResponse()
    
    msg = extract_content() # request.values['Body']
    
    if 'purpose' in session:
        if session['purpose'] == "check":
            if session['checker']:
                response.redirect(url_for('control_view_bp.checker_check'))
            else:
                response.redirect(url_for('control_view_bp.checker'))
        if session['purpose'] == "trigger":
            if session['trigger']:
                response.redirect(url_for('control_view_bp.trigger_check'))
            else:
                response.redirect(url_for('control_view_bp.trigger'))
    elif session['live']:
        if msg == 1:
            session['purpose'] = "check"
            response.redirect(url_for('control_view_bp.checker'))
        elif msg == 2:
            session['purpose'] = "trigger"
            response.redirect(url_for('control_view_bp.trigger'))
        else:
            response.message("I'm sorry, please choose 1 or 2")
    else:
        resp.message(controller_message)
        session['live'] = True
        return str(response)
      
@control_bp.route('/checker')
def checker():
    session['checker'] = True
    response.message("Please enter PIN to check survey status")
      
      
@control_bp.route('/checker_check')
def checker_check():
    pin = os.environ.get(pin)
    if msg == pin and Controller.query.filter_by(number = from_num).first() is not None:
        pass # define whatever the checking behavior is here, perhaps in a separate module
    else:
        response.message("Sorry incorrect pin")
        return str(response)
      
@control_bp.route('/trigger')
def trigger():
    session['trigger'] = True
    response.message("Please enter PIN to trigger a message")
    return str(response)
  
@control_bp.route('/trigger_check')
def trigger_check():
    pin = os.environ.get(pin)
    if msg == pin and Controller.query.filter_by(number = from_num).first() is not None:
        message_the_list(Number.query.all(), survey_prompt, phone_number)
    else:
        response.message("Sorry incorrect pin")
        return str(response)
    
