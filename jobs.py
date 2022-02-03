from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number
#from datetime import date, datetime
import datetime

sched = BlockingScheduler()

#message_numbers = Number.query.filter(Number.code.contains("X")).all()
#nums = [x.number for x in message_numbers]

survey_prompt = "Ready to take the BIOL 102/150/160 survey? Please respond with 'y' or 'yes' when you are ready to begin."

picsul_number = "+18653289322"

#@sched.scheduled_job('date', id='bio_test', run_date='2021-10-11 23:38:00', timezone='US/Eastern')
#def bio_timed_1():
#    message_the_list(nums, survey_prompt, picsul_number)    

#@sched.scheduled_job('cron', id='bio_test', day_of_week = 'mon', hour = 23, minute = 56, timezone='US/Eastern')
#def bio_timed_1():
#    message_the_list(nums, survey_prompt, picsul_number)  
    
#datetimes = ["fri 10:05", "fri 11:20", "fri 12:35", "fri 15:05", "fri 15:35", "mon 12:35",
#             "mon 15:05", "tue 10:05", "tue 10:40", "tue 11:05", "tue 12:45", "tue 14:00",
#             "tue 14:25", "tue 15:40", "tue 15:50", "tue 16:20", "tue 17:20", "tue 17:36", 
#             "tue 9:00",  "thu 10:40", "thu 11:05", "thu 12:20", "thu 12:45", "thu 14:00", 
#             "thu 14:25", "thu 15:05", "thu 15:40", "thu 17:20", "thu 8:50",  "thu 9:00", 
#             "thu 9:50",  "wed 13:50", "wed 10:05", "wed 11:20", "wed 12:35", "wed 15:05", 
#             "wed 16:20", "wed 17:20", "wed 17:35", "wed 18:50"] 

#datetimes = ["mon 10:10", "mon 12:40", "mon 15:10", 
#	"tue 09:05", "tue 10:45", "tue 11:10", "tue 11:20", "tue 12:25", "tue 12:50", "tue 13:50", "tue 14:05", "tue 14:30", "tue 15:45", "tue 16:20", "tue 17:25", "tue 18:30",
#	"wed 08:55", "wed 10:10", "wed 11:20", "wed 11:25", "wed 12:40", "wed 13:50", "wed 13:55", "wed 15:10", "wed 16:20", "wed 16:25", "wed 18:30", "wed 18:55",
#	"thu 09:05", "thu 10:45", "thu 11:10", "thu 11:20", "thu 12:25", "thu 12:50", "thu 13:50", "thu 13:55", "thu 14:05", "thu 14:30", "thu 15:45", "thu 16:20", "thu 17:25", "thu 18:30", 
#	"fri 10:10", "fri 12:40", "fri 15:10"]

### FAKE TESTING VERSION SO I CAN MESS WITH THE TIMES. DELETE THIS########################
datetimes = ["mon 10:10", "mon 12:40", "mon 15:10", 
	"tue 09:05", "tue 10:45", "tue 11:10", "tue 11:20", "tue 12:25", "tue 12:50", "tue 13:50", "tue 14:05", "tue 14:30", "tue 15:45", "tue 16:20", "tue 17:25", "tue 18:30",
	"wed 08:55", "wed 10:10", "wed 11:20", "wed 11:25", "wed 12:40", "wed 13:50", "wed 13:55", "wed 15:10", "wed 16:20", "wed 16:25", "wed 18:30", "wed 18:55",
	"thu 09:05", "thu 10:45", "thu 11:10", "thu 11:20", "thu 12:25", "thu 12:50", "thu 13:50", "thu 13:55", "thu 14:05", "thu 14:30", "thu 15:35", "thu 15:32", "thu 17:25", "thu 18:30", 
	"fri 10:10", "fri 12:40", "fri 15:10"]
##############################################################################################

split_list = [x.split(" ") for x in datetimes]
days = [el[0] for el in split_list]

times = [el[1] for el in split_list]
split_times = [x.split(":") for x in times]
hours = [el[0] for el in split_times]
mins = [el[1] for el in split_times]

#codes = ["F1005", "F1120", "F1235", "F305", "F335", "M1235",
#         "M305", "T1005", "T1040", "T1105", "T1245", "T200",
#         "T225", "T340", "T350", "T420", "T520", "T536",
#         "T900", "TR1040", "TR1105", "TR1220", "TR1245", "TR200",
#         "TR225", "TR305", "TR340", "TR520", "TR850", "TR900",
#         "TR950", "W150", "W1005", "W1120", "W1235", "W305",
#         "W420", "W520", "W535", "W650"]

codes = ["M1010", "M1240", "M1510", 
    "T0905", "T1045", "T1110", "T1120", "T1225", "T1250", "T1350", "T1405", "T1430", "T1545", "T1620", "T1725", "T1830",
	"W0855", "W1010", "W1120", "W1125", "W1240", "W1350", "W1355", "W1510", "W1620", "W1625", "W1830", "W1855",
	"R0905", "R1045", "R1110", "R1120", "R1225", "R1250", "R1350", "R1355", "R1405", "R1430", "R1545", "R1620", "R1725", "R1830", 
	"F1010", "F1240", "F1510"]
             
#codes = ["XXX", "YYY"]

#need to update and check that diffs variable sometime within the job as it's running and before it checkes the database

# create list of beginning of week times
# CHANGE THIS FOR TESTING THEN CHANGE BACK to 2022, 2, 7
base = datetime.datetime(2022, 2, 3, 1,1,1)
###########################################
date_list = [base + datetime.timedelta(weeks=x) for x in range(13)]

def week_check(time):
    diffs = []
    for i in range(0, len(date_list)):
        if time > date_list[i]:
            diffs.append(1)
        else:
            diffs.append(0)
    return str(sum(diffs))

def send_message(day, hour, minute, code):
    @sched.scheduled_job('cron', day_of_week=day, hour=hour, minute=minute, timezone='America/New_York')
    def message_job():    
        now = datetime.datetime.today()
        week = week_check(now)
        # get the right people
        #people = Number.query.filter(Number.code.contains(code)).all()
        people = Number.query.filter(Number.week == week, Number.code.contains(code)).all()        
        # pull out their numbers
        message_numbers = [x.number for x in people]
        # send the surveys
        message_the_list(message_numbers, survey_prompt, picsul_number)  
        
for i in range(0,len(datetimes)):
    send_message(days[i], hours[i], mins[i], codes[i])

sched.start()
