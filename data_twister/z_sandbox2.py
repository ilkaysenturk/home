import pandas as pd
data = {
   'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
   'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
              'Manchester', 'Cairo', 'Osaka'],
     'age': [41, 28, 33, 34, 38, 31, 37],
     'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

row_labels = [101, 102, 103, 104, 105, 106, 107]

column=data['name']
print(column)

#print(row_labels)
df=pd.DataFrame(data=data, index=row_labels)


#data=df[['age']>33,df['name']]
#out=dict(df.max())
data= df[(df['age']>33)&(df['py-score']>79)]
#data=df['age'].isin([33,34,31])
#data=df.loc[df['age'].isin([41,28,33]),:]
print(data)
