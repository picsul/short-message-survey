import schedule
import time

# will need to import the outgoing message functions here as well
from .send_sms import outgoing_sms, message_the_list, list_of_numbers

# so we'll have a list of phone numbers, ideally in the database that makes up our list. We also want to make sure that every instance of contacting the same person gets linked up in the database. Will need to mess around with the database model in all likelihood to make sure that we have timestamps and suc

# create a scheduler instance to keep the schedule of when to trigger the survey text
the_schedule = schedule.Scheduler()

# create job instances to specify that we blast out the text to the numbers list
#the_schedule.every().monday.at("14:00").do(message_the_list, body = "Happy Monday, are you available to take the survey?")
#the_schedule.every().tuesday.at("15:00").do(message_the_list)
#the_schedule.every().wednesday.at("14:30").do(message_the_list)
#the_schedule.every().thursday.at("16:00").do(message_the_list)
#the_schedule.every().friday.at("12:00").do(message_the_list)


the_schedule.every(1).minute.do(outgoing_sms, number = "+15172400923", body = "Happy Monday, are you available to take the survey?")

# if only want to do each one once, add return schedule.CancelJob to the bottom of the message the list function

# this runs all the pending jobs at their appointed time, need to run this when the app is up
while True:
    schedule.run_pending()
    time.sleep(1)

# This is one way to do it

#def run_schedule():
#    while 1:
#        schedule.run_pending()
#        time.sleep(1)   

#if __name__ == '__main__':
#    schedule.every(10).seconds.do(run_every_10_seconds)
#    t = Thread(target=run_schedule)
#    t.start()
#    app.run()
