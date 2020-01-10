from twilio.rest import Client
import os
from .models import Number

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')


client = Client(account_sid, auth_token)

def outgoing_sms(number, body):
    message = client.messages \
                .create(
                     body = body,
                     from_='+18652639184',
                     to = number 
                 )

    print(message.sid)

# This is the database query for the questions module, I'll need something like this
# question = Question.query.get(question_id)

# This is the database Saving code
#    db.save(Answer(content=extract_content(question),
#                   question=question,
#                   session_id=session_id()))

#number = Number.query.get()


list_of_numbers = [] 

for i in range(0, Number.query.count()):
    num = Number.query.get(i+1)
    list_of_numbers.append(num.number)


def message_the_list(num_list, body):
    for num in num_list:
        outgoing_sms(num, body)
