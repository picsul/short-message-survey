from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number
from datetime import date, datetime

sched = BlockingScheduler()

message_numbers = Number.query.filter_by(code = 'XXX').all()

survey_prompt = "Hi alex"

picsul_number = "+18653289322"

@sched.scheduled_job('date', id='bio_test', run_date='2021-10-11 10:46:00', timezone='US/Eastern')
def bio_timed_1():
    message_the_list(message_numbers, survey_prompt, picsul_number)      
    
# template
# as a weekly cron job - check the hunter version
# Say this is mondays at 1234
@sched.scheduled_job('date', id='bio_test', run_date='2021-10-11 12:06:00', timezone='US/Eastern')
def bio_timed_1():
    # get the right people
    people = Number.query.filter(Number.name.contains('al')).all()
    # pull out their numbers
    message_numbers = [x.number for x in people]
    message_the_list(message_numbers, survey_prompt, picsul_number)      

sched.start()
