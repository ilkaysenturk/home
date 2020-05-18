import first
import os
import pandas

i=0
while i< 10:
    i += 1
    print(i)
else:
    print("loop is complete")
#print(out)
#os.mkdir(test)


def my_function(*kids):
    print("hello "+kids[0])

my_function("ilkay","senturk","hasan")
