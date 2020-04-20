from apscheduler.schedulers.blocking import BlockingScheduler
from sms_app.send_sms import outgoing_sms, message_the_list, list_of_numbers, message_the_list_unique
from sms_app.models import Number
from datetime import date, datetime

sched = BlockingScheduler()

link_base = "https://usc.qualtrics.com/jfe/form/"
    
link_tail = "&Q_CHL=gl"

test_instance = "SV_4SYnBkWsvp23LmJ?Q_DL=IunX81MIL25ovHh_4SYnBkWsvp23LmJ_MLRP_"

# monday 4/20
link_instance_mon = "SV_b166qIhL6OXUdx3?Q_DL=zEb1chDZqGMjroK_b166qIhL6OXUdx3_MLRP_"
# friday 4/24
link_instance_fri = "SV_01xn9Duxb02kVy5?Q_DL=gzAgkZQuo2q56uR_01xn9Duxb02kVy5_MLRP_"

links = [
# monday 4/20
"SV_b166qIhL6OXUdx3?Q_DL=zEb1chDZqGMjroK_b166qIhL6OXUdx3_MLRP_",
# friday 4/24
"SV_01xn9Duxb02kVy5?Q_DL=gzAgkZQuo2q56uR_01xn9Duxb02kVy5_MLRP_",
# monday 4/27
"SV_0fA6bQrQ0TnGutD?Q_DL=MzrHA6kLGuOPwKz_0fA6bQrQ0TnGutD_MLRP_",
# friday 5/1
"SV_bg4ZgpZ7gjubPPn?Q_DL=CdCTJLzeOLFtcxr_bg4ZgpZ7gjubPPn_MLRP_",
# monday 5/4 
"SV_bBFyCc5oHDQlNUp?Q_DL=QMBrd1dcOG30Z6h_bBFyCc5oHDQlNUp_MLRP_",
# friday 5/8
"SV_9pBBtHBF2YldKw5?Q_DL=a9IEwPIXQVoOAiB_9pBBtHBF2YldKw5_MLRP_",
# monday 5/11
"SV_7NSMa6xOe83NbiR?Q_DL=LlUBlfYRISKSf0H_7NSMa6xOe83NbiR_MLRP_",
# friday 5/15
"SV_b1QZFd35eakcjJj?Q_DL=dGzy6tko5WVWBK3_b1QZFd35eakcjJj_MLRP_",
# monday 5/18
"SV_3g79EkRPQ3n5OYJ?Q_DL=p8enaW0n5u0B0kM_3g79EkRPQ3n5OYJ_MLRP_",
# friday 5/22
"SV_emkJl73owizVQsB?Q_DL=sC4e8qROJEm31b8_emkJl73owizVQsB_MLRP_",
# monday 5/25
"SV_9Bo2TjditiSZKvP?Q_DL=ggH4r6H4qyt1Skk_9Bo2TjditiSZKvP_MLRP_",
# friday 5/29
"SV_1GPgqHR5fQevvEh?Q_DL=jpWjhIoXuM2xjIw_1GPgqHR5fQevvEh_MLRP_",
# monday 6/1
"SV_b8xdrwAjhME94fX?Q_DL=qzbcQZtBlOoEE6d_b8xdrwAjhME94fX_MLRP_",
# friday 6/5
"SV_cSBx2VX2YwurTJr?Q_DL=wssXQqXU2EAeSpM_cSBx2VX2YwurTJr_MLRP_",
# monday 6/8
"SV_2fuglwsEE5FOJV3?Q_DL=5qeLMqu58xX8riD_2fuglwsEE5FOJV3_MLRP_",
# friday 6/12
"SV_d5NWBFuiTV61UNL?Q_DL=K0qR8FXM2h86HVI_d5NWBFuiTV61UNL_MLRP_",
# monday 6/15
"SV_bxEaQTtrkK8HXJH?Q_DL=qQpJ5gtQNz04DK0_bxEaQTtrkK8HXJH_MLRP_",
# friday 6/19
"SV_0qYrtsifBpGsT6R?Q_DL=kp6rCSV2fJUzc9p_0qYrtsifBpGsT6R_MLRP_",
# monday 6/22
"SV_cBWTVwBMcEtBD6J?Q_DL=MsorZekgq49bg92_cBWTVwBMcEtBD6J_MLRP_",
# friday 6/26
"SV_cNr3RMrNYnqm29v?Q_DL=IS1GATAKJHx1vS0_cNr3RMrNYnqm29v_MLRP_",
# monday 6/29
"SV_cHGlSgdKzpL3Zad?Q_DL=lPes8RAhGH9aogf_cHGlSgdKzpL3Zad_MLRP_"]

send_dates = ['2020-04-20 17:00:00', '2020-04-24 17:00:00', '2020-04-27 17:00:00',
              '2020-05-01 17:00:00', '2020-05-04 17:00:00', '2020-05-08 17:00:00',
              '2020-05-11 17:00:00', '2020-05-15 17:00:00', '2020-05-18 17:00:00',              
              '2020-05-22 17:00:00', '2020-05-25 17:00:00', '2020-05-29 17:00:00',
              '2020-06-01 17:00:00', '2020-06-05 17:00:00', '2020-06-08 17:00:00',
              '2020-06-12 17:00:00', '2020-06-15 17:00:00', '2020-06-19 17:00:00',
              '2020-06-22 17:00:00', '2020-06-26 17:00:00', '2020-06-29 17:00:00']

timezones = {'EST':'US/Eastern', 'CST':'US/Central', 'MST':'US/Mountain', 'PST':'US/Pacific'}

def send_message(date, survey_link, timezone, filter_key):
    @sched.scheduled_job('date', run_date=date, timezone=timezone)
    def message_job():
        static = "Please complete this short survey related to your recent teaching and planning: "
    
        comb_message = []
    
        message_numbers = Number.query.filter_by(name = filter_key).all()
    
        numbers = [number.number for number in message_numbers]
        codes = [number.code for number in message_numbers]
    
        links = [link_base + survey_link + code + link_tail for code in codes]
    
        for link in links:
            comb_message.append(static + link)
    
        message_the_list_unique(numbers, comb_message)    
        
for date in send_dates:
    for timezone in timezones:
        send_message(date, links[send_dates.index(date)], timezones[timezone], timezone)        

### Test job
#@sched.scheduled_job('date', run_date='2020-04-18 16:26:00', timezone='US/Eastern')
#def test_message_picsul():
#    static = "Please complete this short survey related to your recent teaching and planning: "

#    comb_message = []
    
#    picsul_numbers = Number.query.filter_by(name = 'picsul').all()

#    numbers = [number.number for number in picsul_numbers]
#    codes = [number.code for number in picsul_numbers]
    
#    links = [link_base + test_instance + code + link_tail for code in codes]

#    for link in links:
#        comb_message.append(static + link)
    
#    message_the_list_unique(numbers, comb_message)
      
#sched.print_jobs()

sched.start()
