import smtplib
import time
import imaplib
import email
import os 

survey_prompt = "Ready to take the COSC 102 / 111 survey? Please respond to this message when you are ready to begin. You will have 5 minutes to complete the survey once you begin, but the survey should take less than a minute."
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
                        # to deal with non participating studnets that arent found in the database
                        except AttributeError:
                            pass
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')
                    
        mail.logout()
            
    except Exception as e:
        print(str(e))
    
