from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes='1')
def josh_message():
    outgoing_sms('+18652361445', 'Come on, man!')

sched.start()
