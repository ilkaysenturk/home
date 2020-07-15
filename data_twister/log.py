import sys
import conf
import FormatDateTime

#File names and the Paths for the logs are stored in Configuration file conf.py
#This will provide less code modification in the future

LogFileName=conf.configurations["ExampleLogFileName"]
LogfilePath=conf.configurations["PathLogFile"]
FullPathAndLogFileName=LogfilePath+LogFileName

#To initate the log with given Job name
def log_start(JobName):
    OpenLogFileAsW=open(FullPathAndLogFileName,'w')
    sys.stdout=OpenLogFileAsW
    now=FormatDateTime.FormatDateTime() #If no date parameter is passed then sysdate will be used  
    print("******************************************************************************")
    print("********** Log started for "+JobName+" job at " +now+" **********")
    print("******************************************************************************")
    OpenLogFileAsW.close()

#To append log messages at any point of data process
def log_append(LogToAppend):
    OpenLogFileAsA=open(FullPathAndLogFileName,'a')
    sys.stdout=OpenLogFileAsA
    now=FormatDateTime.FormatDateTime()
    print(now+' '+LogToAppend)
    OpenLogFileAsA.close()

#To Finish the log at anytime desired
def log_finish(JobName):
    OpenLogFileAsA=open(FullPathAndLogFileName,'a')
    sys.stdout=OpenLogFileAsA
    now=FormatDateTime.FormatDateTime()
    print("******************************************************************************")
    print("********** Log Finished for "+JobName+" job at " +now+" **********")
    print("******************************************************************************")
    OpenLogFileAsA.close()
