import pandas as pd
import matplotlib.pyplot as plt

def total_revenue():
    #extract the each data files as pandas data frame
    df_a=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\playsport_ab_test\data\data_daily_activity.csv')
    df_p=pd.read_csv(r'C:\Users\ilkay_senturk\git\home\playsport_ab_test\data\data_in_app_purchases.csv')

    #Join the players data with in app purchases
    df=pd.merge(df_a,df_p ,on=['userId','date'],how='left')

    #Calculate total purchases grouped by test group
    df=df.groupby('abTestGroup')['cost'].sum()
    return (df)

df=total_revenue()
print(df)

#Show as graph
df.plot.bar()
plt.show()
