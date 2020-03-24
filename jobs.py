from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number

sched = BlockingScheduler()

usc_numbers = ['+18652361445', '+12022588130', '+18186205367', '+18593947313', '+15172400923']
picsul_numbers = ['+15172400923', '+18652361445', '+18656072492']
alex_numbers = ['+15172400923']

twilio_numbers = ['+18652639199', '+18652639184']

#@sched.scheduled_job('cron', day_of_week='tue', hour='15', minute='59', timezone='US/Eastern')
#def test_message():
#    message_the_list(picsul_numbers, "Thank you for participating in our CS education study. Please indicate the start time of your COSC 102 lab section by responding with one of the following options: A (12:20), B (1:25), C (2:30), or D (3:35).", twilio_numbers[1])

# section times 1220, 125, 230, 335, all 50 minutes long
# launch times 115 220 325 430

# Get the numbers from the database
# Section A

ace = Number.query.filter_by(name = "A").all()

a_numbers = []

for thing in ace:
    a_numbers.append(thing.number)

# Section B
    
bez = Number.query.filter_by(name = "B").all()

b_numbers = []

for thing in bez:
    b_numbers.append(thing.number)
    
# Section C

sez = Number.query.filter_by(name = "C").all()

c_numbers = []

for thing in sez:
    c_numbers.append(thing.number)
    
# Section D
    
dez = Number.query.filter_by(name = "D").all()

d_numbers = []

for thing in dez:
    d_numbers.append(thing.number)

# Initial Prompt message
prompt = "Are you ready to take the COSC 102 survey? Please respond when you are ready to begin. You will have 5 minutes to complete the survey once you begin, but the survey should only take 1-2 minutes."

# Test
#@sched.scheduled_job('cron', day_of_week='wed', hour='12', minute='47', timezone='US/Eastern')
#def test_message():
#    message_the_list(picsul_numbers, prompt, twilio_numbers[0])

# Section A
# Tuesday after Lecture
#@sched.scheduled_job('cron', day_of_week='thu', hour='11', minute='00', timezone='US/Eastern')
#def section_a_prompt():
#    message_the_list(a_numbers, prompt, twilio_numbers[0])

# Wednesday after lab
@sched.scheduled_job('cron', day_of_week='wed', hour='10', minute='00', timezone='US/Eastern')
def section_a_prompt():
    message_the_list(a_numbers, prompt, twilio_numbers[0])
    
# Section B
# Tuesday after lecture
#@sched.scheduled_job('cron', day_of_week='thu', hour='11', minute='00', timezone='US/Eastern')
#def section_b_prompt():
#    message_the_list(b_numbers, prompt, twilio_numbers[0])

# Wednesday after lab
@sched.scheduled_job('cron', day_of_week='wed', hour='10', minute='00', timezone='US/Eastern')
def section_b_prompt():
    message_the_list(b_numbers, prompt, twilio_numbers[0])
    
# Section C
# Tuesday after lecture
#@sched.scheduled_job('cron', day_of_week='thu', hour='11', minute='00', timezone='US/Eastern')
#def section_query_message():
#    message_the_list(c_numbers, prompt, twilio_numbers[0])

# Wednesday after lab
@sched.scheduled_job('cron', day_of_week='wed', hour='10', minute='00', timezone='US/Eastern')
def section_query_message():
    message_the_list(c_numbers, prompt, twilio_numbers[0])

# Section D
# Tuesday after lecture
#@sched.scheduled_job('cron', day_of_week='thu', hour='11', minute='00', timezone='US/Eastern')
#def section_query_message():
#    message_the_list(d_numbers, prompt, twilio_numbers[0])
    
# Wednesday after lab
@sched.scheduled_job('cron', day_of_week='wed', hour='10', minute='00', timezone='US/Eastern')
def section_query_message():
    message_the_list(d_numbers, prompt, twilio_numbers[0])


sched.start()
