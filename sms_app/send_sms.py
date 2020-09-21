from twilio.rest import Client
import twilio
import os
from .models import Number
from sms_app import app, db

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

def outgoing_sms(number, body, out_num):
    message = client.messages \
                .create(
                     body = body,
                     from_= out_num,
                     to = number 
                 )

    return message.sid
    
list_of_numbers = [] 

#for i in range(0, Number.query.count()):
#    try:
#        num = Number.query.get(i+1)
#        list_of_numbers.append(num.number)
#    except AttributeError:
#        pass
        
def message_the_list(num_list, body, from_num, assignment):
    for num in num_list:
        try:
            sms = outgoing_sms(num, body, from_num)
            db.save(Instance(sid = sms, assign = assignment))
        except twilio.base.exceptions.TwilioRestException:
            pass 
         
def message_the_list_unique(num_list, body, from_num):
    for num, mess in zip(num_list, body):
        outgoing_sms(num, mess, from_num)
        
def parse_email(message, assignment):
    if 'notifications@instructure.com' in message['from']:
        subject = message['subject']
        if assignment in subject:
            if not 'Re-Submission' in message['Subject']:
                return True
            else:
                pass
            
