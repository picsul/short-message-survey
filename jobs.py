from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers

sched = BlockingScheduler()

usc_numbers = ['+18652361445', '+12022588130', '+1‪8652361445'‬, '+18186205367']
picsul_numbers = ['+15172400923', '+18652361445']

# test jobs

@sched.scheduled_job('cron', day_of_week='fri', hour='13', minute='03', timezone='America/New_York')
def josh_message():
    message_the_list(picsul_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
    
@sched.scheduled_job('cron', day_of_week='fri', hour='13', minute='55', timezone='America/New_York')
def test_demo_1():
    message_the_list(picsul_numbers,'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')

@sched.scheduled_job('cron', day_of_week='fri', hour='14', minute='15', timezone='America/New_York')
def test_demo_2():
    message_the_list(picsul_numbers,'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')

# demo jobs    
    
@sched.scheduled_job('cron', day_of_week='mon', hour='13', minute='55', timezone='America/New_York')
def demo_message_1():
    message_the_list(usc_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
@sched.scheduled_job('cron', day_of_week='mon', hour='14', minute='15', timezone='America/New_York')
def demo_message_2():
    message_the_list(usc_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
    
sched.start()
