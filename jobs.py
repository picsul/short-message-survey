from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number

sched = BlockingScheduler()

usc_numbers = ['+18652361445', '+12022588130', '+18186205367', '+18593947313', '+15172400923']
picsul_numbers = ['+15172400923', '+18652361445']

link_base = "https://usc.qualtrics.com/jfe/form/"
    
link_instance = "SV_4SYnBkWsvp23LmJ?Q_DL=aLnasIxMU1FJYJd_4SYnBkWsvp23LmJ_MLRP_"

link_tail = "&Q_CHL=gl"


@sched.scheduled_job('cron', day_of_week='wed', hour='16', minute='05', timezone='US/Eastern')
def eastern_message():    
    message_the_list(picsul_numbers, "Test too", "+18652639184")
    
    
@sched.scheduled_job('cron', day_of_week='wed', hour='16', minute='07', timezone='US/Eastern')
def eastern_message():    
    message_the_list(picsul_numbers, "Test too", "+18652639184")
    
    
### SURVEY MESSAGE JOBS

### Monday messages 

### testing out 
# Eastern time people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Eastern')
def eastern_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    eastern_numbers = Number.query.filter_by(name = 'EST').all()

    numbers = [number.number for number in eastern_numbers]
    codes = [number.code for number in eastern_numbers]
    
    links = [link_base + link_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
### CST people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Central')
def central_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    central_numbers = Number.query.filter_by(name = 'CST').all()

    numbers = [number.number for number in central_numbers]
    codes = [number.code for number in central_numbers]
    
    links = [link_base + link_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
    
### MST people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Mountain')
def mountain_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    mountain_numbers = Number.query.filter_by(name = 'MST').all()

    numbers = [number.number for number in mountain_numbers]
    codes = [number.code for number in mountain_numbers]
    
    links = [link_base + link_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
### PST people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Pacific')
def pacific_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    pacific_numbers = Number.query.filter_by(name = 'PST').all()

    numbers = [number.number for number in pacific_numbers]
    codes = [number.code for number in pacific_numbers]
    
    links = [link_base + link_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)    


sched.start()
