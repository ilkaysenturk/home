#This is the Library that we need to play with data
from pandas import DataFrame, read_csv
import pandas as pd


#This to visualize the populated/modified data
import matplotlib.pyplot as plt

#To find out the version of the Python
import sys

import os

#only needed to determine Matplotlib version number
import matplotlib as mt
import conf

#Enable inline plotting !!!This might not be needed though
#matplotlib inline
PathToSave=conf.configurations["PathCSVFile"]

#Get the versions
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' +mt. __version__)
print('File Location '+PathToSave)

#Create sample CSV file to play with if not exists

#Stage data into lists
cars=['ford','mercedes','nissan','bmw']
years=[2000,2002,2004,2015]
DataSet=list(zip(cars,years)) #Merge to data list into one

#Create the DataFrame
df=pd.DataFrame(data=DataSet, columns=['Cars','Years'])

FileNameToSave=conf.configurations["ExampleCSVFile"]
FullPathWithFile=PathToSave+FileNameToSave

df.to_csv(FullPathWithFile,index=False,header=False)
if os.path.exists(FullPathWithFile):
    print("File has been crreated in "+ FullPathWithFile)
else:
    Print("File hasn't been created")
