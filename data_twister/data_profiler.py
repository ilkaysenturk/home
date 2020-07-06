import pandas as pd
import numpy as np
import view_csv as wc
import os
import sys
#import matplotlib.pyplot as plt
from layout_objects import Insert

#This Module Runs function profile_csv_view which accepts two arguments
#See fallowing csv files and thier path that are used in the test runs
#example_cars.csv
#oscar_age_female.csv
#C:\Users\ilkay_senturk\git\home\data_twister\data

def profile_csv_view(source_csv_file_name,source_csv_file_path):
    # Read the CV file and put it to Pandas Data Frame
    csv_file=wc.ViewCSV(source_csv_file_name,source_csv_file_path)
    df=csv_file.read_csv()

    # Get the number of columns and rows
    try:
        number_of_rows_in_df, number_of_columns_in_df = df.shape
    except:
        return
    # Get the column names of Data Frame
    columns_in_df=df.columns
    #Get the maximim length of column names
    max_length_of_column_name=columns_in_df.str.len().max()
    # Store the Data Frame Column Analyses Information in dictionaries
    dict_data_types_in_df=dict(df.dtypes)
    length_of_dict_data_types_in_df=len(dict_data_types_in_df)
    dict_distinct_count_df=dict(df.nunique())
    dict_null_count_df=dict(df.isnull().sum(axis = 0))
    dict_max_df=dict(df.max())
    dict_min_df=dict(df.min())
    dict_mean_df=dict(df.mean())
    dict_std_dev_df=dict(df.std())
    dict_sum_df=dict(df.sum(numeric_only=True))
    #pd.DataFrame(max)

    # Present CSV file information.
    Insert.line_space()
    hdr=Insert('Data Object Name: '+str(source_csv_file_name).upper())
    hdr.header()
    #print('********Data Object Name: ',str(source_csv_file_name).upper(),'********')
    Insert.line_space()
    print('Row Count='+str(number_of_rows_in_df))
    Insert.line_space()
    print('Number of columns_in_df='+str(number_of_columns_in_df))
    Insert.line_space()
    csv_file.file_size_csv()
    Insert.line_space()

    # Iterate through data frame to calculate stats

    count=0
    for x,y in dict_data_types_in_df.items(): # Seperate the dictionary items into two
        if count==0:
            tline=''
            tcount=0
            while tcount <= max_length_of_column_name:
                tline=tline+'-'
                tcount+=1
            # Add formatted header of the data frame output
            print('Column Name                          Data Type  Unique  %Unique  Nulls  %Null  Max Value  Min Value    Average    Std Dev    Sum')
            print(tline,'--------- ------  -------  -----  -----  ---------  -----------  ---------  ---------  ---------')
        # Populate the x=colum and y=data type values
        x_ljust=str(x).ljust(max_length_of_column_name,' ')
        y_ljust=str(y).ljust(10,' ')
        # Population of Column "Unique"
        dict_val_distinct_count_df=dict_distinct_count_df[x]
        dict_val_distinct_count_df_ljust=str(dict_val_distinct_count_df).ljust(7,' ')
        # Population of Column "%Unique"
        percent_unique=(dict_val_distinct_count_df/number_of_rows_in_df)*100
        percent_unique_ljust=str(round(percent_unique,1)).ljust(8,' ')
        # Population of Column "Nulls"
        dict_val_null_count_df=dict_null_count_df[x]
        dict_val_null_count_df_ljust=str(dict_val_null_count_df).ljust(6,' ')
        # Population of Column "%Nulls"
        percent_null=(dict_val_null_count_df/number_of_rows_in_df)*100
        percent_null_ljust=str(round(percent_null,1)).ljust(6,' ')
        # Population of Column "Max Value"
        try:
            max_val=dict_max_df[x]
        except KeyError:
            max_val=''
        max_val_ljust=str(max_val)[0:10].lstrip().ljust(10,' ')
        # Population of Column "Min Value"
        try:
            min_val=dict_min_df[x]
        except KeyError:
            min_val=''
        min_val_ljust=str(min_val)[0:10].lstrip().ljust(13,' ')
        # Population of Column "Avarage"
        mean_val_ljust='0'.ljust(10,' ')
        # Population of Column "Std Dev"
        stddev_val_ljust='0'.ljust(10,' ')
        # Population of Column "Sum"
        sum_val_ljust='0'.ljust(10,' ')
        # Exclude the non-numeric fields from not aplicable calculations Eg. Avarage
        if y!='object':
            mean_val=dict_mean_df[x]
            mean_val_ljust=str(round(mean_val,1)).ljust(10,' ')
            stddev_val=dict_std_dev_df[x]
            stddev_val_ljust=str(round(stddev_val,1)).ljust(10,' ')
            sum_val=dict_sum_df[x]
            sum_val_ljust=str(round(sum_val,1)).ljust(10,' ')


        # Print the calculations
        print(x_ljust,'  ',y_ljust,dict_val_distinct_count_df_ljust,
        percent_unique_ljust,dict_val_null_count_df_ljust,
        percent_null_ljust,max_val_ljust,min_val_ljust+mean_val_ljust,
        stddev_val_ljust,sum_val_ljust)


        count+=1

        # Print the footer
        if count==length_of_dict_data_types_in_df:
            print(tline,'---------  ------  -------  -----  -----  ---------  -----------  ---------  ---------  ---------')

    # Present top 5 records from data frame

    Insert.line_space()
    hdr=Insert('Top 5 Records')
    hdr.header()
    Insert.seperator_line()
    csv_file.sample_data(5,True)

    # Present bottom 5 record from data frame
    Insert.line_space()
    hdr=Insert('Bottom 5 Records')
    hdr.header()
    Insert.seperator_line()
    csv_file.sample_data(5,False)

    Insert.line_space()
    Insert.footer()

if __name__== '__main__':
    # Map command line arguments to function arguments.
    profile_csv_view(*sys.argv[1:])
