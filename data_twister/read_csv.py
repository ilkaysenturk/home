import conf
import pandas as pd
from os import listdir
from os.path import isfile, join

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', 50)
pd.set_option('display.width',200)
def read_csv(SourceCSVFileName):
    SourceLocation=conf.configurations["PathCSVFile"]
    SourceLocationWithFile=SourceLocation+r"\\"+SourceCSVFileName
    try:
        return pd.read_csv(SourceLocationWithFile ,index_col=False)
    except:
       print('Incorrect File name/path.')
       print ('See the below list of files can be read in '+SourceLocation)
       onlyfiles = [f for f in listdir(SourceLocation) if isfile(join(SourceLocation, f))]
       print(onlyfiles)
