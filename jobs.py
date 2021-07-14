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
from datetime import datetime, timedelta 

sched = BlockingScheduler()

assignments_102 = ["Lab 1a", "Lab 1b", "Lab 2a", "Lab 2b", "Lab 3a", "Lab 3b", "Lab 4a", "Lab 4b", "Lab 5a", "Lab 5b", "Lab 6", "Exam 1", "Exam 2", "Exam 3"]
assignments_111 = ["Intro to Python Homework", "Variables and Types Homework", "Operators Homework", "Conditions Homework", "Loops Homework", "Functions Homework",
                  "Classes Homework", "Libraries Homework", "Files Homework"]
assignments_505 = ["Calculator Project", "Bitmap Project", "Pandas Data Project"]
assignments_list = assignments_102 + assignments_111 + assignments_505
  
# Using current time 

@sched.scheduled_job('interval', id='main_esm_job', minutes=5, end_date='2021-05-06 23:59:00', timezone='US/Eastern')
def main_job():
    read_email_from_gmail(assignments_list)

# compile students phone number list
    
#students = Number.query.all()
students = Number.query.filter_by(name = 'Test Student').first()
student_numbers = []

for student in students:
    student_numbers.append(student.number)
    
# Scheduled Jobs 

@sched.scheduled_job('date', id='cosc_timed_1', run_date='2021-07-14 13:30:00', timezone='US/Eastern')
def cosc_timed_1():
    message_the_list(student_numbers, survey_prompt, picsul_number, "timed 1")

@sched.scheduled_job('date', id='cosc_timed_1', run_date='2021-02-22 12:30:00', timezone='US/Eastern')
def cosc_timed_1():
    message_the_list(student_numbers, survey_prompt, picsul_number, "timed 1")
    
@sched.scheduled_job('date', id='cosc_timed_2', run_date='2021-03-08 12:30:00', timezone='US/Eastern')
def cosc_timed_2():
    message_the_list(student_numbers, survey_prompt, picsul_number, "timed 2")
    
@sched.scheduled_job('date', id='cosc_timed_3', run_date='2021-03-22 12:30:00', timezone='US/Eastern')
def cosc_timed_3():
    message_the_list(student_numbers, survey_prompt, picsul_number, "timed 3")
    
@sched.scheduled_job('date', id='cosc_timed_4', run_date='2021-04-05 12:30:00', timezone='US/Eastern')
def cosc_timed_4():
    message_the_list(student_numbers, survey_prompt, picsul_number, "timed 4")
    
@sched.scheduled_job('date', id='cosc_timed_5', run_date='2021-04-19 12:30:00', timezone='US/Eastern')
def cosc_timed_5():
    message_the_list(student_numbers, survey_prompt, picsul_number, "timed 5")

sched.start()
