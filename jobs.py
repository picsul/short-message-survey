from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique, parse_email
from sms_app.scan_email import read_email_from_gmail, survey_prompt, picsul_number
#from sms_app.models import Number
import twilio
import smtplib
import time
import imaplib
import email
import os 

sched = BlockingScheduler()

#@sched.scheduled_job('interval', id='cosc102_lab1a', minutes=1)
#def cosc102_lab1a():
#    read_email_from_gmail("Lab 1a")
    
#@sched.scheduled_job('interval', id='cosc102_lab1a', minutes=1, end_date='2020-09-06 23:59:00', timezone='US/Eastern')
#def cosc102_lab1a():
#    read_email_from_gmail("Lab 1a")
    
#@sched.scheduled_job('interval', id='cosc102_lab1b', minutes=1, end_date='2020-09-23 23:59:00', timezone='US/Eastern')
#def cosc102_lab1b():
#    read_email_from_gmail("Lab 1b")
    

#students = Number.query.filter_by(name = 'NA').all()

#student_numbers = []

#for student in students:
#    student_numbers.append(student.number)
    
#@sched.scheduled_job('cron', day_of_week='mon', hour='14', minute='55', timezone='US/Eastern')
#def post_reminder():
#    message_the_list(student_numbers, message, picsul_number)

sched.start()
