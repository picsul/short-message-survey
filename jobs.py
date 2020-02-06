from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number

sched = BlockingScheduler()

usc_numbers = ['+18652361445', '+12022588130', '+18186205367', '+18593947313', '+15172400923']
picsul_numbers = ['+15172400923', '+18652361445']

# WEEK 2 USC Survey INFO

pacific_links = ["https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_2hLHbz5Hyf5NBTn&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_dhePwP0GqDTu5zT&Q_CHL=gl"]

mountain_links = ["https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_bENvkQCurQsEEHr&Q_CHL=gl",
                  "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_7NDerHqFiDoygkZ&Q_CHL=gl",
                  "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_1yTlsuplG4THHUh&Q_CHL=gl"]
                  
central_links = ["https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_cMcQoUkQvJ4fPxP&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_9MG6ZcTjGBSZteR&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_1Y2uCGvdVZXBjkp&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_3zcn3K7bOxN3W8R&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_5ijiq8AYRMCiZ7L&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_1B4qLoACivOVvLf&Q_CHL=gl"]

eastern_links = ["https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_9GZflsMcnfG5DF3&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_a8CSWgVFh1lXZ7D&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_7a1R5dSFJSeS073&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_cCo86CmUBi2yIh7&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_bei1a3O9UCJcZw1&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_86M4CaqRe3mXAd7&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_bDgxYnWNiNzGonP&Q_CHL=gl",
                 "https://usc.qualtrics.com/jfe/form/SV_8nWt5HjaTD9Rlw9?Q_DL=eViuJjZporF0zUp_8nWt5HjaTD9Rlw9_MLRP_8iulysbXuJYk2GN&Q_CHL=gl"]

# test jobs
#names = ['Alex', 'Josh']

#test_links = ["https://usc-survey.herokuapp.com/", "https://hunter-college-survey.herokuapp.com/"]

#@sched.scheduled_job('cron', day_of_week='thu', hour='15', minute='38', timezone='America/New_York')
#def test_message():
#    static = " should get link "

#    comb_message = []

#    links = test_links

#    for name, link in zip(names, links):
#        comb_message.append(name + static + link)

#    message_the_list_unique(picsul_numbers, comb_message)

    
#@sched.scheduled_job('cron', day_of_week='thu', hour='16', minute='45', timezone='US/Eastern')
#def test_message_2():
#    message_the_list(usc_numbers, "You should receive 4 test messages over the next 4 hours, starting in 15 minutes, let me know if you don't, and no need to click the links.")    

test_links = ["www.google.com"]

@sched.scheduled_job('cron', day_of_week='thu', hour='15', minute='03', timezone='US/Eastern')
def test_message_2():
    static = "Hi, the link is: "
    
    comb_message = []
    
    for link in test_links:
        comb_message.append(static + link)
        
    numbers = Number.query.filter_by(name = 'alex').all()
  
    message_the_list_unique(numbers, comb_message)
    
    
    
### SURVEY MESSAGE JOBS

# Eastern time people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Eastern')
def eastern_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []

    links = eastern_links

    for link in links:
        comb_message.append(static + link)
        
    eastern_numbers = Number.query.filter_by(name = 'EST').all()

    message_the_list_unique(eastern_numbers, comb_message)
   
# Central time people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Central')
def central_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []

    links = central_links

    for link in links:
        comb_message.append(static + link)
        
    central_numbers = Number.query.filter_by(name = 'CST').all()

    message_the_list_unique(central_numbers, comb_message)
    
# Mountain time people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Mountain')
def mountain_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []

    links = mountain_links

    for link in links:
        comb_message.append(static + link)
        
    mountain_numbers = Number.query.filter_by(name = 'MST').all()

    message_the_list_unique(mountain_numbers, comb_message)

# Pacific time people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Pacific')
def pacific_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []

    links = pacific_links

    for link in links:
        comb_message.append(static + link)
        
    pacific_numbers = Number.query.filter_by(name = 'PST').all()

    message_the_list_unique(pacific_numbers, comb_message)

sched.start()
