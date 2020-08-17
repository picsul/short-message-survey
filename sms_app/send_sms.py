from twilio.rest import Client
import twilio
import os
from .models import Number

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

survey_prompt = "Please respond to this text to begin the survey"
picsul_number = "+18652639184"

client = Client(account_sid, auth_token)

def outgoing_sms(number, body, out_num):
    message = client.messages \
                .create(
                     body = body,
                     from_= out_num,
                     to = number 
                 )

    print(message.sid)
    
    
#'+18652639184' Static message #
#'+18652639199' survey loop #

list_of_numbers = [] 

for i in range(0, Number.query.count()):
    try:
        num = Number.query.get(i+1)
        list_of_numbers.append(num.number)
    except AttributeError:
        pass

#def message_the_list(num_list, body, from_num):
#    for num in num_list:
#        outgoing_sms(num, body, from_num)
        
def message_the_list(num_list, body, from_num):
    for num in num_list:
        try:
            outgoing_sms(num, body, from_num)
        except twilio.base.exceptions.TwilioRestException:
            pass 
         
def message_the_list_unique(num_list, body, from_num):
    for num, mess in zip(num_list, body):
        outgoing_sms(num, mess, from_num)
        
def parse_email(message, assignment):
    if 'notifications@instructure.com' in message['from']:
        subject = message['subject']
        if assignment in subject:
            name = message['from'].split("<")[0].strip(' "')
            number = Number.query.filter_by(name = name).first()
            outgoing_sms(number.number, survey_prompt, picsul_number)
            mail.store(i, '+X-GM-LABELS', '\\Trash')
            mail.expunge()
        else:
            pass
            
