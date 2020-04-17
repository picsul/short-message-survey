from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number

sched = BlockingScheduler()

usc_numbers = ['+18652361445', '+12022588130', '+18186205367', '+18593947313', '+15172400923']
picsul_numbers = ['+15172400923', '+18652361445']

link_base = "https://usc.qualtrics.com/jfe/form/"
    
# this changes each time
link_instance = "SV_4SYnBkWsvp23LmJ?Q_DL=aLnasIxMU1FJYJd_4SYnBkWsvp23LmJ_MLRP_"

link_tail = "&Q_CHL=gl"


### Test jobs
    
@sched.scheduled_job('cron', day_of_week='fri', hour='12', minute='20', timezone='US/Eastern')
def test_message_picsul():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    picsul_numbers = Number.query.filter_by(name = 'picsul').all()

    numbers = [number.number for number in picsul_numbers]
    codes = [number.code for number in picsul_numbers]
    
    links = [link_base + link_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Eastern')
def test_message_():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    usc_numbers = Number.query.filter_by(name = 'usc').all()

    numbers = [number.number for number in usc_numbers]
    codes = [number.code for number in usc_numbers]
    
    links = [link_base + link_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
### SURVEY MESSAGE JOBS

### Monday messages 

### EST people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Eastern')
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
