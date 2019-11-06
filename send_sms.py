# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC9e0f935aff43f17417570e515f9616b1'
auth_token = '09fd39abcfd117e291ab5f5c19396058'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey Josh, how are you this evening? Text me back.",
                     from_='+16306086087',
                     to='+18652361445'
                 )

print(message.sid)

