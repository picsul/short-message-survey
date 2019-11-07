from twilio.rest import Client

from smsapp.ignore import twilio


def get_client(username: str, password: str) -> Client:
    return Client(
        username=username,
        password=password,
    )


if __name__ == '__main__':
    client = get_client(twilio['ssid'], twilio['secret_key'])

    message = client.messages.create(
        body="Hey Josh, how are you this evening? Text me back.",
        from_='+16306086087',
        to='+18652361445'
    )

    print(message.sid)
