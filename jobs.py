from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique, parse_email
from sms_app.models import Number
import smtplib
import time
import imaplib
import email
import os 

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = os.environ.get("EMAIL_ADDRESS") + ORG_EMAIL
FROM_PWD    = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

sched = BlockingScheduler()

survey_prompt = "Please respond to this text to begin the survey"
picsul_number = os.environ.get("TWILIO_NUMBER_1")

def read_email_from_gmail(assignment):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        id_list = list(reversed(id_list))
        for i in id_list[0:10]:
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    if parse_email(msg, assignment):
                        name = msg['from'].split("<")[0].strip(' "')
                        number = Number.query.filter_by(name = name).first()
                        try:
                            outgoing_sms(number.number, survey_prompt, picsul_number)
                            mail.store(i, '+X-GM-LABELS', '\\Trash')
                            mail.expunge()
                        except twilio.base.exceptions.TwilioRestException:
                            pass 
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')
                    
        mail.logout()
            
    except Exception as e:
        print(str(e))
        
@sched.scheduled_job('interval', id='lesson_1', minutes=1)
def lesson_1():
    read_email_from_gmail("Lesson Plan #1")

@sched.scheduled_job('interval', id='lesson_2', minutes=1)
def lesson_2():
    read_email_from_gmail("Lesson Plan #2")

#@sched.scheduled_job('cron', day_of_week='mon', hour='14', minute='55', timezone='US/Eastern')
#def post_reminder():
#    message_the_list(nums, message, twilio_numbers[0])

sched.start()
