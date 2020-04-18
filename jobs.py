from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number
from datetime import date, datetime

sched = BlockingScheduler()

link_base = "https://usc.qualtrics.com/jfe/form/"
    
# this changes each time
#link_instance = "SV_4SYnBkWsvp23LmJ?Q_DL=aLnasIxMU1FJYJd_4SYnBkWsvp23LmJ_MLRP_"

link_tail = "&Q_CHL=gl"

test_instance = "SV_4SYnBkWsvp23LmJ?Q_DL=IunX81MIL25ovHh_4SYnBkWsvp23LmJ_MLRP_"

# monday 4/20
link_instance_mon = "SV_b166qIhL6OXUdx3?Q_DL=zEb1chDZqGMjroK_b166qIhL6OXUdx3_MLRP_"
# friday 4/24
link_instance_fri = "SV_01xn9Duxb02kVy5?Q_DL=gzAgkZQuo2q56uR_01xn9Duxb02kVy5_MLRP_"


# monday 4/27
#link_instance_mon = "SV_0fA6bQrQ0TnGutD?Q_DL=MzrHA6kLGuOPwKz_0fA6bQrQ0TnGutD_MLRP_"
# friday 5/1
#link_instance_fri = "SV_bg4ZgpZ7gjubPPn?Q_DL=CdCTJLzeOLFtcxr_bg4ZgpZ7gjubPPn_MLRP_"
# monday 5/4 
#link_instance_mon = "SV_bBFyCc5oHDQlNUp?Q_DL=QMBrd1dcOG30Z6h_bBFyCc5oHDQlNUp_MLRP_"
# friday 5/8
#link_instance_fri = "SV_9pBBtHBF2YldKw5?Q_DL=a9IEwPIXQVoOAiB_9pBBtHBF2YldKw5_MLRP_"
# monday 5/11
#link_instance_mon = "SV_7NSMa6xOe83NbiR?Q_DL=LlUBlfYRISKSf0H_7NSMa6xOe83NbiR_MLRP_"
# friday 5/15
#link_instance_fri = "SV_b1QZFd35eakcjJj?Q_DL=dGzy6tko5WVWBK3_b1QZFd35eakcjJj_MLRP_"
# monday 5/18
#link_instance_mon = "SV_3g79EkRPQ3n5OYJ?Q_DL=p8enaW0n5u0B0kM_3g79EkRPQ3n5OYJ_MLRP_"
# friday 5/22
#link_instance_fri = "SV_emkJl73owizVQsB?Q_DL=sC4e8qROJEm31b8_emkJl73owizVQsB_MLRP_"
# monday 5/25
#link_instance_mon = "SV_9Bo2TjditiSZKvP?Q_DL=ggH4r6H4qyt1Skk_9Bo2TjditiSZKvP_MLRP_"
# friday 5/29
#link_instance_fri = "SV_1GPgqHR5fQevvEh?Q_DL=jpWjhIoXuM2xjIw_1GPgqHR5fQevvEh_MLRP_"
# monday 6/1
#link_instance_mon = "SV_b8xdrwAjhME94fX?Q_DL=qzbcQZtBlOoEE6d_b8xdrwAjhME94fX_MLRP_"
# friday 6/5
#link_instance_fri = "SV_cSBx2VX2YwurTJr?Q_DL=wssXQqXU2EAeSpM_cSBx2VX2YwurTJr_MLRP_"
# monday 6/8
#link_instance_mon = "SV_2fuglwsEE5FOJV3?Q_DL=5qeLMqu58xX8riD_2fuglwsEE5FOJV3_MLRP_"
# friday 6/12
#link_instance_fri = "SV_d5NWBFuiTV61UNL?Q_DL=K0qR8FXM2h86HVI_d5NWBFuiTV61UNL_MLRP_"
# monday 6/15
#link_instance_mon = "SV_bxEaQTtrkK8HXJH?Q_DL=qQpJ5gtQNz04DK0_bxEaQTtrkK8HXJH_MLRP_"
# friday 6/19
#link_instance_fri = "SV_0qYrtsifBpGsT6R?Q_DL=kp6rCSV2fJUzc9p_0qYrtsifBpGsT6R_MLRP_"
# monday 6/22
#link_instance_mon = "SV_cBWTVwBMcEtBD6J?Q_DL=MsorZekgq49bg92_cBWTVwBMcEtBD6J_MLRP_"
# friday 6/26
#link_instance_fri = "SV_cNr3RMrNYnqm29v?Q_DL=IS1GATAKJHx1vS0_cNr3RMrNYnqm29v_MLRP_"
# monday 6/29
#link_instance_mon = "SV_cHGlSgdKzpL3Zad?Q_DL=lPes8RAhGH9aogf_cHGlSgdKzpL3Zad_MLRP_"


### Test jobs
@sched.scheduled_job('date', run_date=datetime(2020, 4, 18, 4, 17), timezone='US/Eastern')
def test_message_picsul():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    picsul_numbers = Number.query.filter_by(name = 'picsul').all()

    numbers = [number.number for number in picsul_numbers]
    codes = [number.code for number in picsul_numbers]
    
    links = [link_base + test_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
@sched.scheduled_job('cron', day_of_week='fri', hour='12', minute='50', timezone='US/Eastern')
def test_message_picsul():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    picsul_numbers = Number.query.filter_by(name = 'picsul').all()

    numbers = [number.number for number in picsul_numbers]
    codes = [number.code for number in picsul_numbers]
    
    links = [link_base + test_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
@sched.scheduled_job('cron', day_of_week='fri', hour='13', minute='22', timezone='US/Eastern')
def test_message_2():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    usc_numbers = Number.query.filter_by(name = 'usc').all()

    numbers = [number.number for number in usc_numbers]
    codes = [number.code for number in usc_numbers]
    
    links = [link_base + test_instance + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
### SURVEY MESSAGE JOBS

### Monday messages 

### EST people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Eastern')
def eastern_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    eastern_numbers = Number.query.filter_by(name = 'EST').all()

    numbers = [number.number for number in eastern_numbers]
    codes = [number.code for number in eastern_numbers]
    
    links = [link_base + link_instance_mon + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
### CST people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Central')
def central_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    central_numbers = Number.query.filter_by(name = 'CST').all()

    numbers = [number.number for number in central_numbers]
    codes = [number.code for number in central_numbers]
    
    links = [link_base + link_instance_mon + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
    
### MST people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Mountain')
def mountain_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    mountain_numbers = Number.query.filter_by(name = 'MST').all()

    numbers = [number.number for number in mountain_numbers]
    codes = [number.code for number in mountain_numbers]
    
    links = [link_base + link_instance_mon + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)
    
### PST people
@sched.scheduled_job('cron', day_of_week='mon', hour='17', minute='00', timezone='US/Pacific')
def pacific_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    pacific_numbers = Number.query.filter_by(name = 'PST').all()

    numbers = [number.number for number in pacific_numbers]
    codes = [number.code for number in pacific_numbers]
    
    links = [link_base + link_instance_mon + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)    

### Friday messages 

### EST people
@sched.scheduled_job('cron', day_of_week='fri', hour='17', minute='00', timezone='US/Eastern')
def eastern_message():
    static = "Please complete this short survey related to your recent teaching and planning: "

    comb_message = []
    
    eastern_numbers = Number.query.filter_by(name = 'EST').all()

    numbers = [number.number for number in eastern_numbers]
    codes = [number.code for number in eastern_numbers]
    
    links = [link_base + link_instance_fri + code + link_tail for code in codes]

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
    
    links = [link_base + link_instance_fri + code + link_tail for code in codes]

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
    
    links = [link_base + link_instance_fri + code + link_tail for code in codes]

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
    
    links = [link_base + link_instance_fri + code + link_tail for code in codes]

    for link in links:
        comb_message.append(static + link)
    
    message_the_list_unique(numbers, comb_message)    


sched.start()
