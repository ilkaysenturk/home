import pandas as pd
import matplotlib.pyplot as plt

def retention_rate(start_date,group):
    #extract the each data files as pandas data frame
    df_a=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\playsport_ab_test\data\data_daily_activity.csv')
    df_m=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\playsport_ab_test\data\data_daily_matches.csv')

    #Fetch the players started on a given start date and test group
    df_a=df_a.loc[(df_a['abTestGroup']==group)&(df_a['date']==start_date),'userId']

    #Join the players who are selected for their test group and start date with
    #their match playing data
    df=pd.merge(df_a,df_m ,on='userId',how='inner')

    #Give me the total number of unique players at start date
    x=df.loc[df['date']==start_date,:]
    number_of_unique_players_at_day_one=x.userId.nunique()

    #Calculate the retention rate grouped by each day
    df=((df.groupby('date')['userId'].nunique())/(number_of_unique_players_at_day_one))*100
    df.to_frame()
    return (df)

#List of test groups
grps=['test_group_a','test_group_b','control_group']
df_m=pd.DataFrame(columns=[''])

#Loop through test groups
for i in grps:
    df_m[i]=retention_rate('2020-05-01',i)
    df_m[i]

df_m.reset_index(inplace = True)
print(df_m)

#Show as graph
df_m.plot(x='date', y=grps)
plt.show()
