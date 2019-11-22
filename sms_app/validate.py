from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# import some_stuff_probably, the outgoing message functions

# response validation functions


def validate_text(user_input):
    text = user_input
    text = text.strip()
    message = "Please make sure your response is alphabetic characters only"
    if text.isalpha():
        return 1
    else:
        return message

def validate_numeric(user_input):
    text = user_input
    text = text.strip()
    message = "Please make sure your response is numeric characters only"
    if text.isdigit():
        return 1
    else:
        return message

def validate_scale(user_input):
    text = user_input
    text = text.strip()
    message = "Please answer with a digit between 1 and 5"
    if text.isdigit and text in ['1', '2', '3', '4', '5']:
        return 1
    else:
        return message


# something like this will go into the question asking functions, will need to make sure it doesn't mess with the count of questions. Also need to make sure it's only saving the "verified" version

body = request.values.get('Body', None)

answer = validate_text(message_body)

attempt = 1

wait_until = datetime.now() + timedelta(hours=1)

while answer != 1 and attempt < 5: 
    resp = MessagingResponse()
    resp.message = answer
    str(resp) # is this right? How do I send the response? 
    
    # increment the attempt
    attempt += 1

    if wait_until < datetime.now():
        break

    # get new message and revalidate
    body = request.values.get('Body', None)
    answer = validate_text(message_body)



# How do we protect against SQL injection type stuff?
