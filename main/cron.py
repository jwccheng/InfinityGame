from django_cron import CronJobBase, Schedule
from account.models import Account
from django.db.models import F
# for user in Account.objects.all():
    #     stcAmount = Account.objects.filter(username=user).values(('stc_Float'))
    #     firstSTC = float(stcAmount[0]['stc_Float'])
    #     stiAmount = Account.objects.filter(username=user).values(('sti_W'))
    #     firstSTI = float(stiAmount[0]['sti_W'])
    #     dropSTI = (firstSTI * 0.01)
    #     Account.objects.filter(username=user).update(stc_Float=(F('stc_Float')-firstSTC))
    #     Account.objects.filter(username=user).update(cmic_W=(F('cmic_W')+firstSTC))
    #     Account.objects.filter(username=user).update(sti_W=(F('sti_W')-dropSTI))
    #     Account.objects.filter(username=user).update(stc_W=(F('stc_W')+dropSTI))

    #     print(firstSTC)
# class MyCronJob(CronJobBase):
#     RUN_AT_TIMES =  ['00:05']

#     schedule = Schedule(run_at_times=RUN_AT_TIMES)
#     code = 'main.my_cron_job' 
#     def do(self):
#         Account.objects.filter(username="admin").update(stc_W=(F('stc_W')+1))
#         print("Test Again Again")
#         pass    # do your thing here
