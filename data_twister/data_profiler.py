import pandas as pd
import numpy as np
import read_csv as rc

#example_cars.csv
#oscar_age_female.csv

df=rc.read_csv('oscar_age_female.csv')
NumberOfRows, NumberOfColumns = df.shape
columns=df.columns
data_types=dict(df.dtypes)
DictionaryLength=len(data_types)
distinct_count=dict(df.nunique())
null_count=dict(df.isnull().sum(axis = 0))
MaxValuePerColumn=dict(df.max())
MinValuePerColumn=dict(df.min())

MeanValuesPerColumn=dict(df.mean())
StdDev=dict(df.std())
SumValuesPerColumn=dict(df.sum(numeric_only=True))


print()
print('********Data Object Name:bla bla********')
print()
print('Row Count='+str(NumberOfRows))
print('Number of Columns='+str(NumberOfColumns))
print()
count=0
for x,y in data_types.items():
    if count==0:

        print('Column Name  Data Type  Uniqe   %Uniqe   Nulls  %Null\
  Max Value  Min Value    Average    Std Dev    Sum')
        print('-----------  ---------  ------  -------  -----  -----\
  ---------  -----------  ---------  ---------  ---------')
    x_ljust=str(x).ljust(11,' ')
    y_ljust=str(y).ljust(11,' ')
    number_of_distinct_values=distinct_count[x]
    number_of_distinct_values_ljust=str(number_of_distinct_values).ljust(8,' ')
    percent_unique=(number_of_distinct_values/NumberOfRows)*100
    percent_unique_ljust=str(round(percent_unique,1)).ljust(9,' ')
    NumberOfNullValuesPerColumn=null_count[x]
    NumberOfNullValuesPerColumn_ljust=str(NumberOfNullValuesPerColumn).ljust(7,' ')
    percent_null=(NumberOfNullValuesPerColumn/NumberOfRows)*100
    percent_null_ljust=str(round(percent_null,1)).ljust(8,' ')
    max_val=MaxValuePerColumn[x]
    max_val_ljust=str(max_val)[0:10].lstrip().ljust(10,' ')
    min_val=MinValuePerColumn[x]
    min_val_ljust=str(min_val)[0:10].lstrip().ljust(13,' ')

    mean_val_ljust='0'.ljust(12,' ')
    stddev_val_ljust='0'.ljust(10,' ')
    sum_val_ljust='0'.ljust(10,' ')

    if y!='object':
        mean_val=MeanValuesPerColumn[x]
        mean_val_ljust=str(round(mean_val,1)).ljust(12,' ')
        stddev_val=StdDev[x]
        stddev_val_ljust=str(round(stddev_val,1)).ljust(10,' ')
        sum_val=SumValuesPerColumn[x]
        sum_val_ljust=str(round(sum_val,1)).ljust(10,' ')

    print(x_ljust+'  '+y_ljust+number_of_distinct_values_ljust+
    percent_unique_ljust+NumberOfNullValuesPerColumn_ljust+
    percent_null_ljust+max_val_ljust+min_val_ljust+mean_val_ljust+
    stddev_val_ljust+sum_val_ljust)

    count+=1

    if count==DictionaryLength:
        print('-----------  ---------  ------  -------  -----  -----\
  ---------  -----------  ---------  ---------  ---------')
