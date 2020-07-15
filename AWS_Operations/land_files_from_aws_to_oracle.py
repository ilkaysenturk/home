#This is the inital version of the Code and needs to be re-factored
#for modules and object classes

import boto3
import cx_Oracle #Oracle Libraries
import conn #Connection configuration file
from datetime import datetime, timedelta
import os

#Identify the business date
b_date= datetime.now()-timedelta()
b_date=b_date.strftime('%d %b %y')

try:
    #Establish a new connection
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
          if row[0]!=0:
              #Update the daily load log entities to Failed with no status
              cursor.execute("update s3_day_load_log\
                                 set load_status=:load_status\
                                 where load_status != 'successful'",["failed"] )
          #Insert the daily load entity
          cursor.execute("insert into s3_day_load_log\
                           (load_business_date,load_status,load_start_timestamp)\
                          values (:x,:y,sysdate)",[b_date,"loading"])
          connection.commit()
          s3 = boto3.resource('s3')
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
except cx_Oracle.Error as error:
    print('Error occured')
    print(error)
