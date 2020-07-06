import time
import pandas as pd
import re
from datetime import datetime, timedelta

class RunEtlJob():

    def __init__(self,jname):
        self.jname = jname.split('.')[0]
        self.jd_df=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\etl_orchestrator\job_dependencies.csv')
        self.ejr_df=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\etl_orchestrator\etl_job_running_log.csv')

    def dependent_object_loaded(self):
        rejr_df=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\etl_orchestrator\etl_job_running_log.csv')
        dependent_objects=self.jd_df.loc[self.jd_df['object_name']==self.jname,'dependent_objects']
        dependent_objects=re.split(',', (dependent_objects.to_string(index=False).lstrip()))
        yesterdays_run_date=(datetime.today()-timedelta(days=1)).strftime("%d/%m/%Y")
        pre_day_status=rejr_df.loc[(rejr_df['job_name'].isin(dependent_objects))&(rejr_df['status']!='complete')]
        if pre_day_status.shape[0]==0:
            return True

    def start_etl_log(self):
        df=pd.DataFrame([[self.jname,datetime.today().strftime("%d/%m/%Y"),'','running']],columns=['job_name','run_start_timestamp','run_end_timestamp','status'])
        df.to_csv(r'C:\Users\ilkay_senturk\git\home\etl_orchestrator\etl_job_running_log.csv',header=None, mode='a',index=False)


    def update_etl_log(self,status):
        self.status=status
        lines=open(r'C:\Users\ilkay_senturk\git\home\etl_orchestrator\etl_job_running_log.csv').readlines()
        for line in lines[::-1]: #Loop the lines in reverse order
            x=re.findall(fr"{self.jname}.*running", line)
            #(?!complete)
            if x!=[]:
                del lines[-1] #delete the last line
        now=datetime.today().strftime("%d/%m/%Y")
        x="{},{},{},{}\n"
        x=x.format(self.jname,now,now,self.status)
        lines.append(x)
        open(r'C:\Users\ilkay_senturk\git\home\etl_orchestrator\etl_job_running_log.csv','w').writelines(lines)
