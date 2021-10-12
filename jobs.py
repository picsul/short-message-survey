from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number
from datetime import date, datetime

sched = BlockingScheduler()

message_numbers = Number.query.filter_by(code = 'XXX').all()
nums = [x.number for x in message_numbers]

survey_prompt = """Ready to take the Bio 127 pre-class survey? Please respond when you are ready to begin. 
                 You will have 5 minutes to complete the survey once you begin, but the survey should only take 1-2 minutes."""

picsul_number = "+18653289322"

@sched.scheduled_job('date', id='bio_test', run_date='2021-10-11 23:38:00', timezone='US/Eastern')
def bio_timed_1():
    message_the_list(nums, survey_prompt, picsul_number)  
    
    
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

codes = ["F1005", "F1120", "F1235", "F305", "F335", "M1235",
         "M305", "T1005", "T1040", "T1105", "T1245", "T200",
         "T225", "T340", "T350", "T420", "T520", "T536",
         "T900", "TR1040", "TR1105", "TR1220", "TR1245", "TR200",
         "TR225", "TR305", "TR340", "TR520", "TR850", "TR900",
         "TR950", "W150", "W1005", "W1120", "W1235", "W305",
         "W420", "W520", "W535", "W650"]

def send_message(day, hour, minute, code):
    @sched.scheduled_job('cron', day_of_week=date, hour=hour, minute=minute, timezone='America/New_York')
    def message_job(code): 
        # get the right people
        people = Number.query.filter(Number.code.contains(code)).all()
        # pull out their numbers
        message_numbers = [x.number for x in people]
        # send the surveys
        message_the_list(message_numbers, survey_prompt, picsul_number)  
        # need to change the survey prompt
        
#for i in range(0,len(datetimes)):
#    send_message(days[i], hours[i], mins[i], codes[i])

sched.start()
