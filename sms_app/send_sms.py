from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')


client = Client(account_sid, auth_token)

def outgoing_sms(number, body):
    message = client.messages \
                .create(
                     body = body,
                     from_='+18652639199',
                     to = number 
                 )

    print(message.sid)





list_of_numbers = [] # ideally the numbers will be stored in the database and we will pull them from there instead of just coding them here


def message_the_list(num_list, body = body):
    for num in num_list:
        outgoing_sms(num, body)
