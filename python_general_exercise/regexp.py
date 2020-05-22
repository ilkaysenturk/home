import re

txt = "The rain in Spain"

x=re.search("^The.*Spain$",txt).span()
t=re.search("\s",txt)
m=re.findall("por",txt)
p=re.split("\s",txt,1)
q=re.sub("\s","_",txt)
w=re.search(r"" )
print(x)
print(m)
print(t)
print(p)

if (x):
    print("yes we have a match")
else:
    print("we don't have a match")
print(q)
