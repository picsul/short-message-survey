from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number
from datetime import date, datetime

sched = BlockingScheduler()

message_numbers = Number.query.filter_by(code = 'XXX').all()

survey_prompt = "Hi alex"

picsul_number = "+18653289322"

@sched.scheduled_job('date', id='bio_test', run_date='2021-10-10 23:00:00', timezone='US/Eastern')
def bio_timed_1():
    message_the_list(message_numbers, survey_prompt, picsul_number)      

sched.start()
