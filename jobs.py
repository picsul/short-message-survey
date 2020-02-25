from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number

sched = BlockingScheduler()

usc_numbers = ['+18652361445', '+12022588130', '+18186205367', '+18593947313', '+15172400923']
picsul_numbers = ['+15172400923', '+18652361445']

timezones = [
'US/Pacific',
'US/Eastern',
'US/Central',
'US/Central',
'US/Eastern',
'US/Eastern',
'US/Eastern',
'US/Pacific',
'US/Central',
'US/Central',
'US/Eastern',
'US/Eastern',
'US/Mountain',
'US/Mountain',
'US/Eastern',
'US/Eastern',
'US/Central',
'US/Mountain',
'US/Central']


    
### SURVEY MESSAGE JOBS

### Monday messages 
    
# Eastern time people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Eastern')
def eastern_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    eastern_indices = [i for i, time in enumerate(timezones) if time == 'US/Eastern']
    eastern_links = [links_w5_mon[i] for i in eastern_indices]

    links = eastern_links

    for link in links:
        comb_message.append(static + link)
        
    eastern_numbers = Number.query.filter_by(name = 'EST').all()

    message_the_list_unique(eastern_numbers, comb_message)
   
# Central time people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Central')
def central_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    central_indices = [i for i, time in enumerate(timezones) if time == 'US/Central']
    central_links = [links_w5_mon[i] for i in central_indices]

    links = central_links

    for link in links:
        comb_message.append(static + link)
        
    central_numbers = Number.query.filter_by(name = 'CST').all()

    message_the_list_unique(central_numbers, comb_message)
    
# Mountain time people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Mountain')
def mountain_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    mountain_indices = [i for i, time in enumerate(timezones) if time == 'US/Mountain']
    mountain_links = [links_w5_mon[i] for i in mountain_indices]

    links = mountain_links

    for link in links:
        comb_message.append(static + link)
        
    mountain_numbers = Number.query.filter_by(name = 'MST').all()

    message_the_list_unique(mountain_numbers, comb_message)

# Pacific time people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Pacific')
def pacific_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    pacific_indices = [i for i, time in enumerate(timezones) if time == 'US/Pacific']
    pacific_links = [links_w5_mon[i] for i in pacific_indices]

    links = pacific_links

    for link in links:
        comb_message.append(static + link)
        
    pacific_numbers = Number.query.filter_by(name = 'PST').all()

    message_the_list_unique(pacific_numbers, comb_message)
    

sched.start()
