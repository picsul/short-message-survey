from twilio.rest import Client
import twilio
import os
from .models import Number
import datetime

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

    print(message.sid)

def message_the_list(num_list, body, from_num):
    for num in num_list:
        try:
            outgoing_sms(num, body, from_num)
            db.save(Instance(sid = sms, assign = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        except twilio.base.exceptions.TwilioRestException:
            pass   
         
def message_the_list_unique(num_list, body, from_num):
    for num, mess in zip(num_list, body):
        outgoing_sms(num, mess, from_num)
