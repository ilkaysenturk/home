import pandas as pd
import numpy as np
import re

data=[1,8,7,5,6,5,3,4,7,1]
s=pd.Series(data)
prev_element=0
lat_element=0
result=[]
x=len(s)-1

for i in range(len(s)):
    if i==0:
        prev_element=0
    else:
        prev_element=i-1
        prev_element=s[prev_element]
    if i==x:
        lat_element=0
    else:
        lat_element=i+1
        lat_element=s[lat_element]
    element=s[i]
    #print(element,prev_element,lat_element)
    if int(element)>int(prev_element):
        if int(element)>int(lat_element):
            result.append(i)
print(result)
out=pd.Series(result)
print(out)









#(lambda c: sum([Counter(c.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
