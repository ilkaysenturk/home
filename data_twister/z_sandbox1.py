import log
import read_csv

df=read_csv.read_csv("oscar_age_female.csv")

data_types=dict(df.dtypes)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

test_dict=dict(df.sum(numeric_only=True))
total_rows=df.shape[0]
total_cols=df.shape[1]
columns=df.columns
#print(car['bran'])


print(total_rows)
print(total_cols)
print(data_types)
#print(test_dict)
