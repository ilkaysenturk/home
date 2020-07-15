If you want to run these python code you need to place the data files into
specific location and modify the file location lines in the scripts

eg. 
Currently
df_a=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\playsport_ab_test\data\data_daily_activity.csv') 

Yours would be
df_a=pd.read_csv(r'C:\<your location path>\data_daily_activity.csv') 