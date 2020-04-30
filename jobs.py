from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number

sched = BlockingScheduler()

twilio_numbers = ['+18652639199', '+18652639184']

# post-survey reminder
nums = [number.number for number in Number.query.all()]

message = "Thank you so much for participating in our COSC 102 study this semester! If you haven't already, please complete the end of the semester survey: https://bit.ly/cosc-102-ps. Your response is very valuable to us and greatly appreciated."

@sched.scheduled_job('cron', day_of_week='thu', hour='15', minute='00', timezone='US/Eastern')
def post_reminder():
    message_the_list(nums, message, twilio_numbers[0])

sched.start()
