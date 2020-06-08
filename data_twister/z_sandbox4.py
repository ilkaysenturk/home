import pandas as pd
import numpy as np
data=[3.000938,11.370722,14.612143,8.990256,13.925283,12.056875,14.118931,8.247458,5.526727]

s=pd.Series(data)
l=[]
min_out=s.min()
pct_out=s.quantile(q=0.25)
std_out=s.std()

l.append(min_out)
l.append(std_out)
l.append(pct_out)

#mean=s.mean()
#std=s.std()

print(l)
