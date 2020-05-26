import conf
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', 50)
pd.set_option('display.width',200)
def read_csv(SourceCSVFileName):
    SourceLocation=conf.configurations["PathCSVFile"]+r"\\"+SourceCSVFileName
    df=pd.read_csv(SourceLocation)
    print(df)
