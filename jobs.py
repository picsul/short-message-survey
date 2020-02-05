from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique

sched = BlockingScheduler()

usc_numbers = ['+18652361445', '+12022588130', '+18186205367', '+18593947313', '+15172400923']
picsul_numbers = ['+15172400923', '+18652361445']
alex_numbers = ['+15172400923']

twilio_numbers = ['+18652639199', '+18652639184']

@sched.scheduled_job('cron', day_of_week='tue', hour='15', minute='59', timezone='US/Eastern')
def test_message():
    message_the_list(picsul_numbers, "Thank you for participating in our CS education study. Please indicate the start time of your COSC 102 lab section by responding with one of the following options: A (12:20), B (1:25), C (2:30), or D (3:35).", twilio_numbers[1])

@sched.scheduled_job('cron', day_of_week='tue', hour='16', minute='38', timezone='US/Eastern')
def section_query_message():
    message_the_list(list_of_numbers, "Thank you for participating in our CS education study. Please indicate the start time of your COSC 102 lab section by responding with one of the following options: A (12:20), B (1:25), C (2:30), or D (3:35).", twilio_numbers[1])
   

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
prompt = "Are you ready to take the survey?"

# Test
@sched.scheduled_job('cron', day_of_week='wed', hour='09', minute='25', timezone='US/Eastern')
def test_message():
    print("A Numbers:")
    print(a_numbers)
    print("B Numbers:")
    print(b_numbers)
    print("C Numbers:")
    print(c_numbers)
    print("D Numbers:")
    print(d_numbers)
    message_the_list(alex_numbers, prompt, twilio_numbers[0])

# Section A
@sched.scheduled_job('cron', day_of_week='wed', hour='13', minute='15', timezone='US/Eastern')
def section_a_prompt():
    message_the_list(a_numbers, prompt, twilio_numbers[0])
    
# Section B
@sched.scheduled_job('cron', day_of_week='wed', hour='14', minute='20', timezone='US/Eastern')
def section_b_prompt():
    message_the_list(b_numbers, prompt, twilio_numbers[0])
    
# Section C
@sched.scheduled_job('cron', day_of_week='wed', hour='15', minute='25', timezone='US/Eastern')
def section_query_message():
    message_the_list(c_numbers, prompt, twilio_numbers[0])

# Section D
@sched.scheduled_job('cron', day_of_week='wed', hour='16', minute='30', timezone='US/Eastern')
def section_query_message():
    message_the_list(d_numbers, prompt, twilio_numbers[0])


sched.start()
