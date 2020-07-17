#This is the inital version of the Code and needs to be re-factored
#for modules and object classes

import boto3 #AWS S3 Library
import cx_Oracle #Oracle Libraries
import conn #Connection configuration file
from datetime import datetime, timedelta
import os #Operating System Library
import logging
import time

#Identify the business date
b_date= datetime.now()-timedelta()
b_date=b_date.strftime('%d %b %y')

#Configure the logger with
#File mode= Append
#Level of logging=info
file_name='aws_s3_to_oracle_'+b_date+'.log'
logging.basicConfig(filename=file_name, filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Log for AWS S3 file download routine '+b_date)
try:
    #Establish a new connection
    #Get the connection details from conn.py file
    with cx_Oracle.connect(conn.username,
                           conn.password,
                           conn.dsn,
                           encoding=conn.encoding) as connection:
     #Create a cursor
      with connection.cursor() as cursor:
          #Get the daily log entities with no successful status value
          cursor.execute("select count(*)\
                            from s3_day_load_log\
                           where load_status !=:load_status",["successful"])
          row=cursor.fetchone()
          #If daily log entities with unsuccessful status returns row count
          if row[0]!=0:
              logging.info('There is/are uncomplete log record/s updating them...')
              #Update the unseccessful daily load log entities to Failed
              cursor.execute("update s3_day_load_log\
                                 set load_status=:load_status\
                                 where load_status != 'successful'",["failed"] )
              logging.info('Update Finished...')
              connection.commit()
          #Create boto3 instance to reach S3 objects
          s3 = boto3.resource('s3')
          #Check if all objects are ready in the source to download
          logging.info('Cheking if the source objects are available in the source...')
          source_ready=0
          while source_ready<1:
              #Check the associated bucket if the complete flag file is there
              bucket=s3.Bucket('flvbbk61exg')
              objs=list(bucket.objects.filter(Prefix='complete_flag_file.txt'))
              if len(objs)>0:
                  source_ready=1
                  #Insert the today's daily load entity
                  cursor.execute("insert into s3_day_load_log\
                                   (load_business_date,load_status,load_start_timestamp)\
                                  values (:x,:y,sysdate)",[b_date,"loading"])
                  connection.commit()
                  #Loop through Buckets and files objects in S3
                  for bucket in s3.buckets.all():
                      for obj in bucket.objects.all():
                          #Get the size of the file in AWS S3 bucket
                          file_size_in_aws=s3.Object(bucket.name,obj.key).content_length
                          #Insert the entity of the file to files load log
                          cursor.execute("insert into s3_files_load_log\
                                        (bucket_name,file_name,load_status,load_start_timestamp)\
                                        values (:x,:y,:z,sysdate)",[bucket.name,obj.key,"loading"])
                          connection.commit()
                          print('{0}:{1}'.format(bucket.name, obj.key))
                          #Download the file from AWS
                          s3.Bucket(bucket.name).download_file(obj.key,obj.key)
                          #Get the size of the file in local environment
                          file_size_in_local=os.path.getsize(obj.key)
                          #Compare the downloaded file size against the AWS source
                          if file_size_in_aws==file_size_in_local:
                              load_status="successful"
                          else:
                              load_status='failed'
                              #Update files log upon successful completion
                          cursor.execute("update s3_files_load_log\
                                             set load_status=:load_status,\
                                          load_end_timestamp=sysdate,\
                                             file_size=:file_size_in_local\
                                            where load_status = 'loading'",[load_status,file_size_in_local])
                          connection.commit()
                  #Update the day load entitiy as successful
                  cursor.execute("update s3_day_load_log\
                                     set load_status=:load_status,\
                                         load_end_timestamp=sysdate\
                                   where load_status = 'loading'",["successful"] )
                  connection.commit()
              time.sleep(10)
except cx_Oracle.Error as error:
    print('Error occured')
    print(error)
