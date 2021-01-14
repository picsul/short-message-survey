from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique, parse_email, message_the_list_static
from sms_app.scan_email import read_email_from_gmail, survey_prompt, picsul_number, picsul_number_static, survey_reminder
from sms_app.models import Number
import twilio
import smtplib
import time
import imaplib
import email
import os 

sched = BlockingScheduler()

assignments_list = ["Final Exam", "Lab 6", "Lab 5a", "Lab 4a", "Lab 3a"]

from datetime import datetime, timedelta 
  
# Using current time 

## One job   
@sched.scheduled_job('date', id='cosc_timed_1', run_date='2021-01-14 15:15:00', timezone='US/Eastern')
def single_job():
    t1 = datetime.now() 
    read_email_from_gmail(assignments_list)
    t2 = datetime.now()
    print(t2-t1)
    
#l3a = ["Lab 3a"]
#l4a = ["Lab 4a"]
#l5a = ["Lab 5a"]
#l6 = ["Lab 6"]
#exam = ["Final Exam"]

#@sched.scheduled_job('interval', id='cosc102_lab1a', minutes=1, end_date='2020-09-06 23:59:00', timezone='US/Eastern')
  
# 5 jobs with a different list object just containing 1 thing

#t1 = datetime.now()

#@sched.scheduled_job('date', id='l3a', run_date='2021-01-11 23:35:00', timezone='US/Eastern')
#def cosc102_lab3a():
#    read_email_from_gmail(l3a)
    
#@sched.scheduled_job('date', id='l4a', run_date='2021-01-11 23:35:00', timezone='US/Eastern')
#def cosc102_lab4a():
#    read_email_from_gmail(l4a)
    
#@sched.scheduled_job('date', id='l5a', run_date='2021-01-11 23:35:00', timezone='US/Eastern')
#def cosc102_lab5a():
#    read_email_from_gmail(l5a)
  
#@sched.scheduled_job('date', id='l6', run_date='2021-01-11 23:35:00', timezone='US/Eastern')
#def cosc102_lab6():
#    read_email_from_gmail(l6)

#@sched.scheduled_job('date', id='exam', run_date='2021-01-11 23:35:00', timezone='US/Eastern')
#def cosc102_exam1():
#    read_email_from_gmail(exam)

#t2 = datetime.now()

#print(t2-t1)
#####

sched.start()
