import conf
import pandas as pd
import os
from os import listdir
from os.path import isfile, join

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', 50)
pd.set_option('display.width',200)

class ViewCSV():

    def __init__(self,source_csv_file_name,source_csv_file_path):
        self.source_csv_file_name=source_csv_file_name
        self.source_csv_file_path=source_csv_file_path
        self.source_location_with_file=self.source_csv_file_path+r"\\"+self.source_csv_file_name

    def read_csv(self):
        try:
            return pd.read_csv(self.source_location_with_file ,index_col=False,encoding='latin1')
        except:
            print('In correct File name/path.')
            print ('See the below list of files can be read in '+self.source_csv_file_path)
            onlyfiles = [f for f in listdir(self.source_csv_file_path) if isfile(join(self.source_csv_file_path, f))]
            print(onlyfiles)

    def file_size_csv(self):
        csv_file_size=os.path.getsize(self.source_location_with_file)
        print("File",self.source_csv_file_name.upper(),"is",csv_file_size,"byte")

    def sample_data(self,number_of_records,head=True):
        df=pd.read_csv(self.source_location_with_file ,index_col=False,encoding='latin1')
        if head!=True:
            tail_out=df.tail(number_of_records)
            print(tail_out)
        else:
            head_out=df.head(number_of_records)
            print(head_out)
