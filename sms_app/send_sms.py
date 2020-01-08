from twilio.rest import Client
import os
from .models import Number

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

def outgoing_sms(number, origin, body):
    message = client.messages \
                .create(
                     body = body,
                     from_= origin,
                     to = number 
                 )

    print(message.sid)

list_of_numbers = [] 

for i in range(0, Number.query.count()):
    num = Number.query.get(i+1)
    list_of_numbers.append(num.number)

    
def message_the_list(num_list, origin, body):
    for num in num_list:
        outgoing_sms(num, origin, body)
