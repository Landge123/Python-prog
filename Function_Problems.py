#Q1) WAp to print 0 to 30 odd number and store in list.
"""
def number():
    x=[]
    for i in range(0,31):
        if i%2==1:
            x.append(i)
        print(i,end=" ")
number()

def number():
    x=[]
    for i in range(0,31):
        if i%2==1:
            x.append(i)
        return x
q=number()
print(q)
"""

#Q2) WAP to store given string in dictanray with its ascii number.
"""
def convert():

   y='Good Luck'

   d={}

   for i in y:
    d[i]=ord[i]
    print(d)

convert()
"""
# y='Good Luck'
# def data():

#     e={}
#     for i in y:

"""
w=["Python","Java","SQl","PowerBI","Excel"]

def Position():

    for i in enumerate(w):
        print(i)
Position()

w=["Python","Java","SQl","PowerBI","Excel"]

def Position():

    for i,j in enumerate(w):
        print(i,j)
Position()


w=["Python","Java","SQl","PowerBI","Excel"]

def Position():

    for i in range(0,5):
        print(i,w[i])
Position()


w=["Python","Java","SQl","PowerBI","Excel"]
def Position():
    for i in w:
        print(len(i))
Position()
"""
#Q4) WAP to find the sum of individual values in list.
"""
s=[1,4,"Hello",5+4j,True,False,2.3,[1,2,3]]

sum=0
def cal():
    for i in s:
        if type(s)==(int,complex,bool,float):
            sum=sum+i
            
print(sum)

cal()


s=[1,4,"Hello",5+4j,True,False,2.3,[1,2,3]]

sum=0
def cal():
    for i in s:
        if isinstance(i(int,float,bool,complex)):
            global sum
            sum=sum+i
    print(sum)
cal()
"""

#Q6) Sum of 1 to 10 number.
"""
total=0
def additon():   
    for i in range(1,11):
        total=total+i
        print(total)
additon()
"""
#Q7) 
"""
a=["walmart","kickout","punchout","lovely","Thought"]

def show():
    length={}
    for i in a:
        a[i]=len(i)
    print(a)
show()

"""

#Q8) if word is odd length reverse it and if even keep as it is.

#a=["walmart","kickout","punchout","lovely","Thought"]
"""
def reversed():
    d={}
    for i in d:
        if len(i)%2==1:
            print(i[::-1])
        else:
            print(i)

reversed(["walmart","kickout","punchout","lovely","Thought"])

"""

#Q9) Check positive, negative & zero
"""
a=int(input('Enter the number: '))
def check():
    if a>0:
        print(a,'is positve number.')
    elif a<0:
        print(a,' is negative number.')
    else:
        print(a,' is zero value')

check()
"""

# y=43217

# def last():
#     print(y%10)

# last()


"""
s="Genrator"
def store(s):
    a={}
    for i in s:
        a.update({i:ord(i)})
        yield a
w= store(s)
print(next(w))

#Q) WAP to perform all calculation
a) Gen
a=10
b=20

def cal(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a%b

w=cal(a,b)
print(next(w))
print(next(w))
print(next(w))
print(next(w))
#print(next(w))


#b) Fun
# a=10
# b=20

def cal(a,b):
    return a+b,a-b,a*b,a%b
w=cal(10,20)
print(w)

# WAP to generate only values which are divide by 5 using genrator

l=[34,44,60,56,67,90,25,40]

def div(l):
    out=[]
    for i in l:
        if i%5==0:
            out.append(i)
w=div(l)
print(w)




l=[34,44,60,56,67,90,25,40]

def div(l):
    l=[]
    for i in l:
        if l(i)%5==0:

        




# WAP to return a iterator which having square root off values present in the list using function with return and as with generator

l=[25,35,49,81,9,16]

import math

def sqrt_iter(data):
    return iter([math.sqrt(x) for x in data])

result = sqrt_iter(l)

for val in result:
    print(val)




import math

l = [25, 35, 49, 81, 9, 16]

def sqrt_gen(data):
    for x in data:
        yield math.sqrt(x)

result = sqrt_gen(l)

for val in result:
    print(val)

"""

#wap to generate a list if it is individual data type, reverse it else keep it as it is


def reversed(a):
    d=[]
    for i in d:
        if len(i)%2==1:
            print(i[::-1])
        else:
            print(i)
    return
t=reversed(["walmart","kickout","punchout","lovely","Thought"])

print(t)