from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
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

#            for response_part in data:
#                if isinstance(response_part, tuple):
#                    msg = email.message_from_string(response_part[1])
#                    email_subject = msg['subject']
#                    email_from = msg['from']
#                    print('From : ' + email_from + '\n')
#                    print('Subject : ' + email_subject + '\n')

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()

        for i in reversed(id_list)[1:10]:
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                print('From : ' + email_from + '\n')
                print('Subject : ' + email_subject + '\n')
            
        except Exception as e:
            print(str(e))


@sched.scheduled_job('interval', id='my_job_id', minutes=1)
def check_email():
    read_email_from_gmail()

#@sched.scheduled_job('cron', day_of_week='mon', hour='14', minute='55', timezone='US/Eastern')
#def post_reminder():
#    message_the_list(nums, message, twilio_numbers[0])

sched.start()
