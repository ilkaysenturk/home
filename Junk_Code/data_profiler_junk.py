import pandas as pd
import numpy as np
import read_csv as rc
import os

#example_cars.csv
#oscar_age_female.csv

#Read the CV file and put it to Pandas Data Frame
csv_file=rc.ViewCSV('oscar_age_female.csv',r'C:\Users\ilkay_senturk\git\home\data_twister\data')
df=csv_file.read_csv()

#Get the number of columns and rows
number_of_rows_in_df, number_of_columns_in_df = df.shape

#Get the column names of Daata Frame
columns_in_df=df.columns

dict_data_types_in_df=dict(df.dtypes)
length_of_dict_data_types_in_df=len(dict_data_types_in_df)
dict_distinct_count_df=dict(df.nunique())
dict_null_count_df=dict(df.isnull().sum(axis = 0))
dict_max_df=dict(df.max())
dict_min_df=dict(df.min())
dict_mean_df=dict(df.mean())
dict_std_dev_df=dict(df.std())
dict_sum_df=dict(df.sum(numeric_only=True))

print()
print('********Data Object Name:bla bla********')
print()
print('Row Count='+str(number_of_rows_in_df))
print()
print('Number of columns_in_df='+str(number_of_columns_in_df))
print()
csv_file.file_size_csv()
print()

count=0
for x,y in dict_data_types_in_df.items(): #Seperate the dictionary items into two
    if count==0:
        print('Column Name  Data Type  Uniqe   %Uniqe   Nulls  %Null\
  Max Value  Min Value    Average    Std Dev    Sum')
        print('-----------  ---------  ------  -------  -----  -----\
  ---------  -----------  ---------  ---------  ---------')
    x_ljust=str(x).ljust(9,' ')
    y_ljust=str(y).ljust(10,' ')
    dict_val_distinct_count_df=dict_distinct_count_df[x]
    dict_val_distinct_count_df_ljust=str(dict_val_distinct_count_df).ljust(7,' ')
    percent_unique=(dict_val_distinct_count_df/number_of_rows_in_df)*100
    percent_unique_ljust=str(round(percent_unique,1)).ljust(8,' ')
    dict_val_null_count_df=dict_null_count_df[x]
    dict_val_null_count_df_ljust=str(dict_val_null_count_df).ljust(7,' ')
    percent_null=(dict_val_null_count_df/number_of_rows_in_df)*100
    percent_null_ljust=str(round(percent_null,1)).ljust(8,' ')
    max_val=dict_max_df[x]
    max_val_ljust=str(max_val)[0:10].lstrip().ljust(10,' ')
    min_val=dict_min_df[x]
    min_val_ljust=str(min_val)[0:10].lstrip().ljust(13,' ')
    mean_val_ljust='0'.ljust(12,' ')
    stddev_val_ljust='0'.ljust(10,' ')
    sum_val_ljust='0'.ljust(10,' ')

    if y!='object':
        mean_val=dict_mean_df[x]
        mean_val_ljust=str(round(mean_val,1)).ljust(12,' ')
        stddev_val=dict_std_dev_df[x]
        stddev_val_ljust=str(round(stddev_val,1)).ljust(10,' ')
        sum_val=dict_sum_df[x]
        sum_val_ljust=str(round(sum_val,1)).ljust(10,' ')

    print(x_ljust,'  ',y_ljust,dict_val_distinct_count_df_ljust,
    percent_unique_ljust,dict_val_null_count_df_ljust,
    percent_null_ljust,max_val_ljust,min_val_ljust+mean_val_ljust,
    stddev_val_ljust,sum_val_ljust)

    count+=1

    if count==length_of_dict_data_types_in_df:
        print('-----------  ---------  ------  -------  -----  -----\
  ---------  -----------  ---------  ---------  ---------')

csv_file.sample_data(5,True)
csv_file.sample_data(5,False)
