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
   
sched.start()
