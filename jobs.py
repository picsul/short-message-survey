from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number
import datetime
from sms_app import app, db

sched = BlockingScheduler()

survey_prompt = "Ready to take the BIOL 102 survey? Please respond with 'y' or 'yes' when you are ready to begin."


picsul_number = "+18652639199"

datetimes = ["mon 21:30", "wed 12:20", "fri 12:20", "tue 11:00", "thu 11:00", "tue 12:35", "thu 12:35", "tue 14:10", "thu 14:10"]

split_list = [x.split(" ") for x in datetimes]
days = [el[0] for el in split_list]

times = [el[1] for el in split_list]
split_times = [x.split(":") for x in times]
hours = [el[0] for el in split_times]
mins = [el[1] for el in split_times]

codes = ["M1220", "W1220", "F1220", "T1100", "R1100", "T1235", "R1235", "T1410", "R1410"]

# create list of beginning of week times to index the weeks
base = datetime.datetime(2023, 2, 13, 1,1,1)
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

jobs = []
        
def message_job(code):    
    with app.app_context():
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
    job = sched.add_job(message_job, 'cron', day_of_week=days[i], hour=hours[i], minute=mins[i], args=[codes[i]], timezone='America/New_York')
    jobs.append(job)

# create an empty list to hold job references

# access job attributes using the job references
for job in jobs:
    job_id = job.id
    job_name = job.name
    job_next_run_time = job.next_run_time

    print(f'Job ID: {job_id}')
    print(f'Job name: {job_name}')
    print(f'Next run time: {job_next_run_time}')

# start the scheduler
sched.start()
