
from sms_app.send_sms import outgoing_sms, parse_email
from sms_app.models import Number, Instance
from sms_app import app, db
import twilio
import smtplib
import time
import imaplib
import email
import os 
# remove this later
from random import random

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = os.environ.get("EMAIL_ADDRESS") + ORG_EMAIL
FROM_PWD    = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

survey_prompt = "Ready to take the COSC 102 / 111 survey? Please respond to this message when you are ready to begin. You will have 5 minutes to complete the survey once you begin, but the survey should take less than a minute."
welcome_message = 'Please indicate your agreement at this moment with the following statements about your experiences in COSC 102 / 111 on a 1-5 scale, with 1 indicating strong disagreement, 3 indicating that you neither agree nor disagree, and 5 indicating strong agreement.' 
survey_reminder = "Thank you for responding to the text message surveys about your experiences in COSC 102 or 111 this semester! We have just one more thing to ask of you, to complete our end of the semester survey. You should have received an email this morning with more details and the link to the survey, so please complete that at your earliest convenience. Thank you."
picsul_number = os.environ.get("TWILIO_NUMBER_1")
picsul_number_static = os.environ.get("TWILIO_NUMBER_2")

def read_email_from_gmail(assignments):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        id_list = list(reversed(id_list))
        for i in id_list:
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):

            # get the email message into a readable format, get the name readable, and query the database
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    name = msg['from'].split("<")[0].strip(' "')
                    number = Number.query.filter_by(name = name).first()
                    #number = Number.query.filter_by(name = 'alex').first()

                    # print message info so that I can make sure it's still running 
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    #print(assignment)
                    print('Subject : ' + email_subject + '\n')

                # If the name (confusingly named 'number') isn't in the database, delete the message
                    if number is None:
                        mail.store(i, '+X-GM-LABELS', '\\Trash')
                        mail.expunge()

            # If the number is in the database, and if it's for a correct assignment, send the survey prompt, unless twilio complains
                    for assignment in assignments:
                        if parse_email(msg, assignment):
                            try:
                                sms = outgoing_sms(number.number, survey_prompt, picsul_number)
                                db.save(Instance(sid = sms, assign = assignment))
                                mail.store(i, '+X-GM-LABELS', '\\Trash')
                                mail.expunge()
                            except twilio.base.exceptions.TwilioRestException:
                                pass 

            # There are a lot of emails about assessments, and we definitely never want those, so move them to trash
                    #elif 'Assessment' in msg['subject']:
                        #mail.store(i, '+X-GM-LABELS', '\\Trash')
                        #mail.expunge()

        mail.logout()
            
    except Exception as e:
        print(str(e))
    
