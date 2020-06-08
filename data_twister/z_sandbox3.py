import conf
import pandas as pd
import os
#investments_VC.csv
#oscar_age_female.csv
df=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\data_twister\data\oscar_age_female.csv' ,index_col=False,encoding='latin1')

out=df.describe()
print(out)
