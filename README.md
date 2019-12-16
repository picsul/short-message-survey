# Short Message Survey

*Short Message Survey* is an app for sending out text-based ESM surveys.

## License

Copyright 2019 PICSUL

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgment

This material is based upon work supported by the National Science Foundation under Grant No. 1937700. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the authors and do not reflect the views of the National Science Foundation.

## Setup



## Installation

### Setting up the virtual environment

- `brew install python3 -venv` (only have to do first time)
- `python3 -m venv my_venv` (only have to do first time)
- `source my_venv/bin/activate`

### Installing requirements

- `pip install -r requirements.txt` (only have to do first time)

### Setting up database

- `sqlite3 survey.db` (only have to do first time)

### Checking that Python works (requires v.3)

- `python --version` (only have to do first time)

### Adding Twilio credentials

- `source twilio.env` (*may* have to do every time)

#### Check that creds were added

- `python` (only for checking; not necessary)
- `import os` (only have to do first time)
- `os.environ.get('TWILIO_ACCOUNT_SID')` (only for checking; not necessary)
- `os.environ.get('TWILIO_AUTH_TOKEN')` (only for checking; not necessary)

### Updating the database and running the server

- `python manage.py db upgrade` (only have to do first time)
- `python manage.py dbseed` (only have to do first time)
- `python manage.py runserver` 

### Telling Twilio to send HTTP requests to forward requests to our number to our local server

- `twilio login` 
- `brew tap twilio/brew && brew install twilio` (only have to do first time)
- `twilio phone-numbers:update "+<add number>" --sms-url="http://localhost:5000/message"`

## Example

![Imgur](https://i.imgur.com/phHIZRt.png)
