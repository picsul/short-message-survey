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
    
    
datetimes = ["fri 10:05", "fri 11:20", "fri 12:35", "fri 15:05", "fri 15:35", "mon 12:35",
             "mon 15:05", "tue 10:05", "tue 10:40", "tue 11:05", "tue 12:45", "tue 14:00",
             "tue 14:25", "tue 15:40", "tue 15:50", "tue 16:20", "tue 17:20", "tue 17:36", 
             "tue 9:00",  "thu 10:40", "thu 11:05", "thu 12:20", "thu 12:45", "thu 14:00", 
             "thu 14:25", "thu 15:05", "thu 15:40", "thu 17:20", "thu 8:50",  "thu 9:00", 
             "thu 9:50",  "wed 13:50", "wed 10:05", "wed 11:20", "wed 12:35", "wed 15:05", 
             "wed 16:20", "wed 17:20", "wed 17:35", "wed 18:50"] 

split_list = [x.split(" ") for x in datetimes]
days = [el[0] for el in split_list]

times = [el[1] for el in split_list]
split_times = [x.split(":") for x in times]
hours = [el[0] for el in split_times]
mins = [el[1] for el in split_times]




@sched.scheduled_job('cron', day_of_week='tue', hour='10', minute='30', timezone='America/New_York')
def message_pre():
    message_the_list(student_numbers, '+19179949576', pre_message)
    
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
