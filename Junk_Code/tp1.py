import re
def find_max(num1,num2,num3):
    list=[num1,num2,num3]
    out=max(list)
    print(out)

find_max(11,2,4)


def max_of_two(x,y):
    if x>y:
        return x
    else:
        return y
def final_max(x,y,z):
    return(max_of_two(z,max_of_two(x,y)))

p=final_max(1,99,3)

print(p)

def find_sum(x,y,z):
    list=[x,y,z]
    sum_out=sum(list)
    return sum_out

sum_out=find_sum(10,33,21)
print(sum_out)


def sum(numbers):
    total=0
    for i in numbers:
        total=i+total
    return total

print(sum((2,3,4)))


def mul_all(numbers):
    total=1
    for i in numbers:
        total=i*total
    return total

print(mul_all((8, 2, 3, -1, 7)))


def rev_sort(x):
    concat=''
    for i in reversed(x):
        concat= concat + i
    print(concat)

rev_sort('1234abcd')


def fact(x):
    y=1
    for i in reversed(range(x+1)):
        if i not in [0,1]:
            y=i*y
    return y

print(fact(4))


def range_test(n):
    if n in range(1,6):
        print('yes')
    else:
        print('no')
range_test(0)

def case_counter(string):
    uc=0
    lc=0
    for i in string:
        if i.islower():
            lc+=1
        elif i.isupper():
            uc+=1
    print('Number of lower case is',str(lc))
    print('Number of upper case is',str(uc))

case_counter('The quick Brow Fox')



def unique(x):
    list=[]
    for i in x:
        if i not in list:
            list.append(i)
    print(list)


unique('12333345')



def even(x):
    list=(x)
    output=[]
    for i in list:
        if i ==0:
            return False
        elif (i % 2 ==0):
            output.append(i)
        else:
            pass
    return output



out=even([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(out)


#'job1,job2,job3'
def sep_comma(s_input):
    input=s_input
    out=input.count(',')
    input=re.split(',',input)
    my_list=input
    out=list(my_list)
    print(out)


sep_comma('job1,job2,job3')
