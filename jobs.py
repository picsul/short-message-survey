from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms

sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes=1)
#def josh_message():
#    outgoing_sms('+18652361445', 'Come on, man!')

@sched.scheduled_job('cron', day_of_week='sun', hour='20', minute='40', timezone='America/New_York')
def josh_message():
    outgoing_sms('+18652361445', 'I hope you get this, man!')
    
@sched.scheduled_job('cron', day_of_week='sun', hour='20', minute='45', timezone='America/New_York')
def josh_message():
    outgoing_sms('+15172400923', 'I hope you get this, man!')

sched.start()
