from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers

sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes=1)
#def josh_message():
#    outgoing_sms('+18652361445', 'Come on, man!')

@sched.scheduled_job('cron', day_of_week='fri', hour='10', minute='11', timezone='America/New_York')
def josh_message():
    outgoing_sms('+15172400923', 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
    
@sched.scheduled_job('cron', day_of_week='fri', hour='10', minute='11', timezone='America/New_York')
def josh_message():
    outgoing_sms('+18652361445','Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')

sched.start()
