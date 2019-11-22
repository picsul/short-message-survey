# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    print(body)

    resp = MessagingResponse()

    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")
    else:
        resp.message("Whatever")

    # Start our response
    # resp = MessagingResponse()

    # Add a message
    # resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)


from twilio.rest import Client
import time
import schedule
from threading import Thread

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC95b72498be67f507f91808f694b99e40'
auth_token = '7787c2f7ebc9b0bbde1c916f729f39dc'
client = Client(account_sid, auth_token)

def message_1():
    message = client.messages \
                .create(
                     body="Just.",
                     from_='+18652639199',
                     to='+15172400923'
                 )

    print(message.sid)

start_time = time.time()

def run_every_10_seconds():
    print("Running periodic task!")
    #print "Elapsed time: " + str(time.time() - start_time)
    #message = client.messages \
    #            .create(
    #                 body="Repeatedly.",
    #                 from_='+18652639199',
    #                 to='+15172400923'
    #             )


def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    #schedule.every(10).seconds.do(run_every_10_seconds)
    #t = Thread(target=run_schedule)
    #t.start()
    #print "Start time: " + str(start_time)
    message_1()
    app.run(debug=True)




