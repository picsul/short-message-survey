from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number

sched = BlockingScheduler()

twilio_numbers = ['+18652639199', '+18652639184']

# post-survey reminder
#nums = [number.number for number in Number.query.all()]
nums = ["+19313063791", "+13018362777", "+19012828292", "+14233550342", "+16158154541", "+18653820776", "+18656221002", "+14073104075", "+18656077555", "+18655676872", "+16158814866"]

message = "Thanks again for participating in the COSC 102 study. Please provide your UTK NetID so that we can process your participant payment. Thanks!"

@sched.scheduled_job('cron', day_of_week='mon', hour='14', minute='55', timezone='US/Eastern')
def post_reminder():
    message_the_list(nums, message, twilio_numbers[0])

sched.start()
