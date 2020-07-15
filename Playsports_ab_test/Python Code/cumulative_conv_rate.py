import pandas as pd
import matplotlib.pyplot as plt

def cumulative_conv(start_date,group):
    #extract the each data files as pandas data frame
    df_a=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\playsport_ab_test\data\data_daily_activity.csv')
    df_p=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\playsport_ab_test\data\data_in_app_purchases.csv')

    #Fetch the players started on a given start date and test group
    df_a=df_a.loc[(df_a['abTestGroup']==group)&(df_a['date']==start_date),'userId']

    #Join the players who are selected for their test group and start date with
    #their purchase data
    df=pd.merge(df_a,df_p ,on='userId',how='inner')

    #Give me the total number of unique players at start date
    x=df.loc[df['date']==start_date,:]
    number_of_unique_players_at_day_one=df_a.shape[0]

    #Calculate the cumulative conversion rate grouped by date
    df=df.groupby('date').userId.nunique()
    df=df.cumsum()/number_of_unique_players_at_day_one
    df.to_frame()
    return (df)

#List of test groups
grps=['test_group_a','test_group_b','control_group']
df_m=pd.DataFrame(columns=[''])

#Loop through test groups
for i in grps:
    df_m[i]=cumulative_conv('2020-05-01',i)
    df_m[i]

df_m.reset_index(inplace = True)
print(df_m)

#Show as graph
df_m.plot(x='date', y=grps)
plt.show()
