#This is a config file to be used to configure project floders, file names
#and hard coded values etc. This will allow us to make configuration changes
#qiocker and with less code modifications in the project.


ProjectHome= r'C:\Users\ilkay_senturk\git\home'
ProjectFolder= r'\data_twister'
DataFolder= r'\data'
LogFolder= r'\log'

configurations={"ExampleLogFileName": r"\example.log",
                 "PathLogFile": ProjectHome + ProjectFolder + LogFolder,
                 "ExampleCSVFile":r"\example_cars.csv",
                 "PathCSVFile": ProjectHome + ProjectFolder + DataFolder}
