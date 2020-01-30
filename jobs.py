from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique

sched = BlockingScheduler()

usc_numbers = ['+18652361445', '+12022588130', '+18186205367', '+18593947313', '+15172400923']
picsul_numbers = ['+15172400923', '+18652361445']

# WEEK 1 USC Survey INFO
pacific_numbers =["+12098317150", "+12148835738"]

pacific_links = ["https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_2hLHbz5Hyf5NBTn&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_dhePwP0GqDTu5zT&Q_CHL=gl"]

mountain_numbers = ["+14802083551", "+14802801912", "+19015696541"]

mountain_links = ["https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_bENvkQCurQsEEHr&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_7NDerHqFiDoygkZ&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_1yTlsuplG4THHUh&Q_CHL=gl"]

central_numbers = ["+14175690640", "+12192019242", "+18652371887", "+18653613083", "+17329778383", "+12345678907"]

central_links = ["https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_cMcQoUkQvJ4fPxP&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_9MG6ZcTjGBSZteR&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_1Y2uCGvdVZXBjkp&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_3zcn3K7bOxN3W8R&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_5ijiq8AYRMCiZ7L&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_1B4qLoACivOVvLf&Q_CHL=gl"]

eastern_numbers = ["+18657760368", "+16098946523", "+19195186191", "+18609675255", "+18436019708", "+12198690083", "+13152430245", "+14042772811"]

eastern_links = ["https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_9GZflsMcnfG5DF3&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_a8CSWgVFh1lXZ7D&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_7a1R5dSFJSeS073&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_cCo86CmUBi2yIh7&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_bei1a3O9UCJcZw1&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_86M4CaqRe3mXAd7&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_bDgxYnWNiNzGonP&Q_CHL=gl",
 "https://usc.qualtrics.com/jfe/form/SV_esS5PaMIPbo4M9T?Q_DL=5C1pioU1MyPvipn_esS5PaMIPbo4M9T_MLRP_8iulysbXuJYk2GN&Q_CHL=gl"]

# test jobs
names = ['Alex', 'Josh']

test_links = ["https://usc-survey.herokuapp.com/", "https://hunter-college-survey.herokuapp.com/"]

@sched.scheduled_job('cron', day_of_week='thu', hour='12', minute='46', timezone='America/New_York')
def test_message():
    static = " should get link "

    comb_message = []

    links = test_links

    for name, link in zip(names, links):
        comb_message.append(name + static + link)

    message_the_list_unique(picsul_numbers, comb_message)
      
### SURVEY MESSAGE JOBS


@sched.scheduled_job('cron', day_of_week='thu', hour='13', minute='36', timezone='America/New_York')
def test_message_2():
    message_the_list(picsul_numbers, "test message")

# Eastern time people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Eastern')
def eastern_message():
    static = "Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: "

    comb_message = []

    links = eastern_links

    for link in links:
        comb_message.append(static + link)

    message_the_list_unique(picsul_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
# Central time people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Central')
def central_message():
    message_the_list_unique(picsul_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
# Mountain time people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Mountain')
def mountain_message():
    message_the_list_unique(picsul_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
# Pacific time people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Pacific')
def pacific_message():
    message_the_list_unique(picsul_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   


#@sched.scheduled_job('cron', day_of_week='mon', hour='09', minute='19', timezone='America/New_York')
#def test_demo_1():
#    message_the_list(picsul_numbers,'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')

#@sched.scheduled_job('cron', day_of_week='mon', hour='09', minute='35', timezone='America/New_York')
#def test_demo_2():
#    message_the_list(picsul_numbers,'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')

# demo jobs    
    
#@sched.scheduled_job('cron', day_of_week='mon', hour='13', minute='55', timezone='America/New_York')
#def demo_message_1():
#    message_the_list(usc_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
#@sched.scheduled_job('cron', day_of_week='mon', hour='14', minute='15', timezone='America/New_York')
#def demo_message_2():
#    message_the_list(usc_numbers, 'Please complete this short survey related to your teaching and the planning related to your teaching over the past few days: http://bit.ly/sm-math')
   
    
sched.start()
