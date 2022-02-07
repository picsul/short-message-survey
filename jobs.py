from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number
#from datetime import date, datetime
import datetime

sched = BlockingScheduler()

survey_prompt = "Ready to take the BIOL 102/150/160 survey? Please respond with 'y' or 'yes' when you are ready to begin."

picsul_number = "+18653289322"

datetimes = ["mon 10:10", "mon 12:40", "mon 15:00", 
	"tue 09:05", "tue 10:45", "tue 11:10", "tue 11:20", "tue 12:25", "tue 12:50", "tue 13:50", "tue 14:05", "tue 14:30", "tue 15:45", "tue 16:20", "tue 17:25", "tue 18:30",
	"wed 08:55", "wed 10:10", "wed 11:20", "wed 11:25", "wed 12:40", "wed 13:50", "wed 13:55", "wed 15:10", "wed 16:20", "wed 16:25", "wed 18:30", "wed 18:55",
	"thu 09:05", "thu 10:45", "thu 11:10", "thu 11:20", "thu 12:25", "thu 12:50", "thu 13:50", "thu 13:55", "thu 14:05", "thu 14:30", "thu 15:45", "thu 16:20", "thu 17:25", "thu 18:30", 
	"fri 10:10", "fri 12:40", "fri 15:10"]

split_list = [x.split(" ") for x in datetimes]
days = [el[0] for el in split_list]

times = [el[1] for el in split_list]
split_times = [x.split(":") for x in times]
hours = [el[0] for el in split_times]
mins = [el[1] for el in split_times]

codes = ["M1010", "M1240", "M1510", 
    "T0905", "T1045", "T1110", "T1120", "T1225", "T1250", "T1350", "T1405", "T1430", "T1545", "T1620", "T1725", "T1830",
	"W0855", "W1010", "W1120", "W1125", "W1240", "W1350", "W1355", "W1510", "W1620", "W1625", "W1830", "W1855",
	"R0905", "R1045", "R1110", "R1120", "R1225", "R1250", "R1350", "R1355", "R1405", "R1430", "R1545", "R1620", "R1725", "R1830", 
	"F1010", "F1240", "F1510"]
             

# create list of beginning of week times to index the weeks
base = datetime.datetime(2022, 2, 7, 1,1,1)
date_list = [base + datetime.timedelta(weeks=x) for x in range(13)]

# count which week we are in by comparing a time to the beginning of week times list
def week_check(time):
    diffs = []
    for i in range(0, len(date_list)):
        if time > date_list[i]:
            diffs.append(1)
        else:
            diffs.append(0)
    return str(sum(diffs))

# create a cron job to send a message to a subset of people dependent on the week
def send_message(day, hour, minute, code):
    @sched.scheduled_job('cron', day_of_week=day, hour=hour, minute=minute, timezone='America/New_York')
    def message_job():    
	# figure out which week we're in when job runs
        now = datetime.datetime.today()
        week = week_check(now)
        # get the right people for that week
        people = Number.query.filter(Number.week == week, Number.code.contains(code)).all()        
        # pull out their numbers
        message_numbers = [x.number for x in people]
        # send the surveys
        message_the_list(message_numbers, survey_prompt, picsul_number)  
        
# create the cron jobs for each unique datetime
for i in range(0,len(datetimes)):
    send_message(days[i], hours[i], mins[i], codes[i])

sched.start()
