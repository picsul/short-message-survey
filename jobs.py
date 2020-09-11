from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique, parse_email
from sms_app.scan_email import read_email_from_gmail, survey_prompt, picsul_number
from sms_app.models import Number
import twilio
import smtplib
import time
import imaplib
import email
import os 

sched = BlockingScheduler()

# COSC 102
# Labs
## Lab 1
@sched.scheduled_job('interval', id='cosc102_lab1a', minutes=1, end_date='2020-09-06 23:59:00', timezone='US/Eastern')
def cosc102_lab1a():
    read_email_from_gmail("Lab 1a")

@sched.scheduled_job('interval', id='cosc102_lab1b', minutes=1, end_date='2020-09-13 23:59:00', timezone='US/Eastern')
def cosc102_lab1b():
    read_email_from_gmail("Lab 1b")

## Lab 2
@sched.scheduled_job('interval', id='cosc102_lab2a', minutes=1, end_date='2020-09-20 23:59:00', timezone='US/Eastern')
def cosc102_lab2a():
    read_email_from_gmail("Lab 2a")
    
@sched.scheduled_job('interval', id='cosc102_lab2b', minutes=1, end_date='2020-09-27 23:59:00', timezone='US/Eastern')
def cosc102_lab2b():
    read_email_from_gmail("Lab 2b")

## Lab 3    
@sched.scheduled_job('interval', id='cosc102_lab3a', minutes=1, end_date='2020-10-04 23:59:00', timezone='US/Eastern')
def cosc102_lab3a():
    read_email_from_gmail("Lab 3a")
    
@sched.scheduled_job('interval', id='cosc102_lab3b', minutes=1, end_date='2020-10-11 23:59:00', timezone='US/Eastern')
def cosc102_lab3b():
    read_email_from_gmail("Lab 3b")
  
## Lab 4  
#@sched.scheduled_job('interval', id='cosc102_lab4a', minutes=1, end_date='2020-10-18 23:59:00', timezone='US/Eastern')
#def cosc102_lab4a():
#    read_email_from_gmail("Lab 4a")
    
#@sched.scheduled_job('interval', id='cosc102_lab4b', minutes=1, end_date='2020-10-25 23:59:00', timezone='US/Eastern')
#def cosc102_lab4b():
#    read_email_from_gmail("Lab 4b")

## Lab 5
#@sched.scheduled_job('interval', id='cosc102_lab5a', minutes=1, end_date='2020-11-08 23:59:00', timezone='US/Eastern')
#def cosc102_lab5a():
#    read_email_from_gmail("Lab 5a")
    
#@sched.scheduled_job('interval', id='cosc102_lab5b', minutes=1, end_date='2020-11-15 23:59:00', timezone='US/Eastern')
#def cosc102_lab5b():
#    read_email_from_gmail("Lab 5b")
  
## Lab 6    
#@sched.scheduled_job('interval', id='cosc102_lab6', minutes=1, end_date='2020-11-26 23:59:00', timezone='US/Eastern')
#def cosc102_lab6():
#    read_email_from_gmail("Lab 6")

## Exam 1 
@sched.scheduled_job('interval', id='cosc102_exam1', minutes=1, end_date='2020-09-09 23:59:00', timezone='US/Eastern')
def cosc102_exam1():
    read_email_from_gmail("Exam 1")
    
    
# Homework COSC 111    
## HW Programming Language
@sched.scheduled_job('interval', id='cosc111_homework_prog_lang', minutes=1, end_date='2020-09-01 20:00:00', timezone='US/Eastern')
def cosc111_homework_prog_lang():
    read_email_from_gmail("Programming Language Homework")
    
## HW Intro to Python 
@sched.scheduled_job('interval', id='cosc111_homework_intro_python', minutes=1, start_date='2020-08-31 08:00:00', end_date='2020-09-08 20:00:00', timezone='US/Eastern')
def cosc111_homework_intro_python():
    read_email_from_gmail("Intro to Python Homework")
    
## HW Variables and Types
@sched.scheduled_job('interval', id='cosc111_homework_var_types', minutes=1, start_date='2020-09-07 08:00:00', end_date='2020-09-15 20:00:00', timezone='US/Eastern')
def cosc111_homework_var_types():
    read_email_from_gmail("Variables and Types Homework")
    
## HW Operators
@sched.scheduled_job('interval', id='cosc111_homework_operators', minutes=1, start_date='2020-09-14 08:00:00', end_date='2020-09-22 20:00:00', timezone='US/Eastern')
def cosc111_homework_operators():
    read_email_from_gmail("Operators Homework")
    
## HW Conditions
@sched.scheduled_job('interval', id='cosc111_homework_conditions', minutes=1, start_date='2020-09-21 08:00:00', end_date='2020-09-29 20:00:00', timezone='US/Eastern')
def cosc111_homework_conditions():
    read_email_from_gmail("Conditions Homework")
    
## HW Loops
@sched.scheduled_job('interval', id='cosc111_homework_loops', minutes=1, start_date='2020-09-28 08:00:00', end_date='2020-10-06 20:00:00', timezone='US/Eastern')
def cosc111_homework_Loops():
    read_email_from_gmail("Loops Homework")
    
## HW Functions
#@sched.scheduled_job('interval', id='cosc111_homework_functions', minutes=1, start_date='2020-10-05 08:00:00', end_date='2020-10-13 20:00:00', timezone='US/Eastern')
#def cosc111_homework_functions():
#    read_email_from_gmail("Functions Homework")
    

#students = Number.query.filter_by(name = 'NA').all()

#student_numbers = []

#for student in students:
#    student_numbers.append(student.number)
    
#@sched.scheduled_job('cron', day_of_week='mon', hour='14', minute='55', timezone='US/Eastern')
#def post_reminder():
#    message_the_list(student_numbers, message, picsul_number)

sched.start()
