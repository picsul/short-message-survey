# Short Message Survey

*Short Message Survey* is an app for sending out text-based ESM surveys.

## To-do in the immediate term

- Create a minimal viable product locally
- Taking the local instance and figuring out how to deploy it (via some cloud service; possibly AWS)

## Functionality

### Necessary functionality

- Send messages at random intervals within some parameters
  - Parameters: which days, which hours
  - In general, and in just one case, something like 3-5 messages per day per person for two weeks
- Be able to take between roughly 5-1,000 phone numbers and to send messages on a (semi-random) schedule
- Has to be more-or-less instantaneous 
- Store the data we receive
- Prioritize data privacy/confidentiality and the safety of storing the data
- Allow natural text (i.e., "I'm at the library studying with friends") as well as more closed-form types of answers (i.e., A-E or 1-5)
- Includes tests

### Desired functionality

- Doing some kind of validation of responses
- Making a python library available to others (free and open-source)

### Other ideas

- Be able to allow users to nominate to share their location
- Be able to take audio/photos
- Making an R package available to others (free and open-source)
- Having a web interface (for $ and open-source)
- Having the functionality to do some kind of intervention via a chat bot

## Acknowledgment

This material is based upon work supported by the National Science Foundation under Grant No. 1937700. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the authors and do not reflect the views of the National Science Foundation.

# Installation

## Setting up the virtual environment

- `brew install python3 -venv`
- `python3 -m venv venv`
- `source venv/bin/activate`

## Installing requirements

- `pip install -r requirements.txt`

## Setting up database

- `sqlite3 survey.db`

## Checking that Python works (requires v.3)

- `python --version`

## Adding Twilio credentials

- `source twilio.env`

## Check that creds were added

- `os.environ.get('TWILIO_ACCOUNT_SID')`
- `os.environ.get('TWILIO_AUTH_TOKEN')`

## Updating the database and running the server

- `python manage.py db upgrade`
- `python manage.py dbseed`
- `python manage.py runserver`

## Telling Twilio to send HTTP requests to forward requests to our number to our local server

- `brew tap twilio/brew && brew install twilio`
- `twilio phone-numbers:update "+18652639199" --sms-url="http://localhost:5000/message"`

# Example

![Imgur](https://i.imgur.com/phHIZRt.png)
