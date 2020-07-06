import run_etl_job as run
import os
import time

def Job1():
    job_name=os.path.basename(__file__)
    job=run.RunEtlJob(job_name)
    job.start_etl_log()
    while True:
        if job.dependent_object_loaded():
            try:
                time.sleep(10)
            except:
                job.update_etl_log('failed')
            else:
                job.update_etl_log('complete')
            break
