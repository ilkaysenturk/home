list=[1,5,6,7,9,14,25]

prev_i=0
for i in list:
    if i<prev_i+1:
        print(i)
    else:
        m=i
        while prev_i<m:
            t=prev_i+1
            print(t)
            prev_i=t
    prev_i=i
    #print(prev_i)
