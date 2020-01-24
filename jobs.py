from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers

sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes=1)
#def josh_message():
#    outgoing_sms('+18652361445', 'Come on, man!')

new_list = ['+15172400923']

@sched.scheduled_job('cron', day_of_week='wed', hour='12', minute='18', timezone='America/New_York')
def message():
    message_the_list(list_of_numbers, '+19179949576', 'Ready to take survey 1?')
    

@sched.scheduled_job('cron', day_of_week='fri', hour='11', minute='08', timezone='America/New_York')
def message():
    message_the_list(new_list, '+19179949576', 'Ready to take survey 1?')
    

@sched.scheduled_job('cron', day_of_week='thu', hour='11', minute='12', timezone='America/New_York')
def message():
    message_the_list(new_list, '+19179949576', 'Ready to take survey 2?')
        
    
@sched.scheduled_job('interval', weeks = 1, start_date = '2020-01-28 9:30:00', end_date = '2020-05-12 10:00:00', timezone='America/New_York')
def pre_survey():
    message_the_list(list_of_numbers, '+19179949576', 'Ready to take survey 1?')
    
@sched.scheduled_job('interval', weeks = 1, start_date = '2020-01-28 11:15:00', end_date = '2020-05-12 12:00:00', timezone='America/New_York')
def post_survey():
    message_the_list(list_of_numbers, '+19179949576', 'Ready to take survey 2?')
        
sched.start()
