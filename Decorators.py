#Addding extra functionality without chaning the main code or source code
#It is also part of a function
#login
#First class: pyhton function delecerated 
#Meta Programming: Taking one part of thr program and modifying in another part of the program 
#Decorator function
"""
def outer(func):
    def inner(*args,**kwargs):
        statement ---> before execution of the program 
        func(*args,**kwargs)
        statement ---> After execution of the program
    return inner
"""
#@outer ---->connection part for both functions.

#Main function
"""
def main_function():
    statement

main_function()
"""

#1)Outer function it will accept only one argument which is func or main function
#2)@Outer function is internally present like [Outer(main_function)]
#3)After the Outer function invoking the inner function
#4)inner function
#5)return inner
#6)main_function()collecting values
#7) statement will get call.
#8) func(*args,**kwargs) will get callled

#inner function will accpet vaiaible positional argument.
#@outer function will call outer(main function).
#All values will be present in main function()

#EX
"""
def outer(Add):
    def inner(x,y):
        print('Addition operation started')
        Add(x,y)
        print('Addition operation completed')

    return inner

@outer

def Add(x,y):
    print(x+y)

Add(4,5)    
"""

#Work flow 
"""
1) def outer(Add):
2) @outer
3) def Add(x,y):
4) def inner(x,y):
5) return inner ---.x,y
6) Add(4,5)
7) print('Addition operation started')
8) Add(x,y)
9) print('Addition operation completed')
"""

#EX 
"""
import time
def Outer(func):
    def inner():
        # time.sleep(3)  ------------To dely execution for perticular time.
        # print(func.__name__)       ---------- To print function name.
        print('Welcome To All')
        # time.sleep(2)
        func()
        # time.sleep(5)
        print('Class completed')
    return inner

@Outer
def Greet():
    print("Good Morning All")   

Greet()

@Outer
def Demo():
    print('First method')

Demo()
"""

#Multiple decorator with multiple main function
"""
def outer(func):
    def inner(x,y):
        print("Operation Started")
        func(x,y)
        print("Operation completed")
    return inner

def outer1(func):
    def inner1(x,y):
        print("Operation Started--------**********")
        func(x,y)
        print("Operation completed--------$$$$$$$$$")
    return inner1

@outer

def Demo(x,y):
    print(x+y)
Demo(5,6) 

@outer

def Demo(x,y):
    print(x+y)
Demo(4,6) 
"""

# Multiple decoratorswith single maain function
"""
def outer(func):
    def inner(x,y):
        print("Operation Started")
        func(x,y)
        print("Operation completed")
    return inner

def outer1(func):
    def inner1(x,y):
        print("Operation Started--------**********")
        func(x,y)
        print("Operation completed--------$$$$$$$$$")
    return inner1

@outer
@outer1
def Demo(x,y):
    print(x+y)
Demo(5,6) 
"""
#Date: 8/10/26
"""
def outer(func):
    def inner(x):
        print(func.__name__)
        if x%2==0:
            print('The Given Number Is Even')
        else:
            print('The Given Number Is Odd')
        func(x)
        print('Operation Done.')
       
    

    return inner

@outer

def Check(x):
    print(x)
Check(10) 
Check(12)
"""

"""
def Outer(func):
    count=0
    def inner():
        nonlocal count
        print(func.__name__)
        count=count+1
        print('Function total count is: ',count)
        func()
        print('Operation completed')

    return inner
@Outer
def Demo():
   ... 

Demo()
Demo()
Demo()
"""

"""
def outer(func):
    def inner(x,y):
        print("Operation Started")
        func(x,y)
        print("Operation completed")
        print()
    return inner

@outer

def Demo(x,y):
    print(x+y)
Demo(5,6) 

@outer
def Demo1(x,y):

    print(x-y)
Demo(10,5)

@outer
def Demo2(x,y):
   
    print(x*y)
Demo2(3,6)
"""

"""def Outer_most(Parameter):
    def Outer(x):
        def inner(*args,**kwargs):
            #statemnt
            func(*args,**kwargs)
            #Stament ---> AR*
        return inner
    return Outer_most

@Outer_most
    """
'''
def Outer_most(msg):
    def Outer(func):
        def inner(*a):
            print(msg)
            func(*a)
           
        return inner
    return Outer


@Outer_most('Addition of number is ')
def Add(x,y):
    print(x+y)

@Outer_most('Subtraction of number is')
def Sub(x,y):
    print(x-y)

@Outer_most('Sivivsion of number is ')
def Div(x,y):
    print(x//y)

Add(12,13)
Sub(30,25)
Div(95,5)

'''
"""
import time
def Outer_most(msg):
    def Outer(func):
        def inner(*a):
            print(msg)
            func(*a)
           
        return inner
    return Outer

@Outer_most(2)

def Add(x,y):
    print(x+y)

@Outer_most(3)

def Sub(x,y):
    print(x-y)

@Outer_most(5)

def Div(x,y):
    print(x//y)

Add(2,3)
Sub(10,5)
Div(25,5)
"""
#WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME, DELAY FOR 3 SECONDS AND DISPLAY EMAIL ADDRESS ,
#DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER


"""
import time

def Outer_most(s):
    def outer(func):
        def inner(*args):
            time.sleep(s)

            return func(*args)
        
        return inner
    return outer
    
@Outer_most(3)
def Company_name(name):
    print(f'Name of the company is {name}')
Company_name("TY")

@Outer_most(3)
def Email(email):
    print(f'Company email address id {email}')
Email("ty123@gmail.com")

@Outer_most(3)
def Mobile(num):
    print(f'Company mobile is {num}')
Mobile(9172302539)

Company_name()
Email()
Mobile()
"""


#write a decorator function to print the type of datatype before performing the action
"""
def Outer(func):
    def inner(*args):
        for i in args:
            print(type(i))
            func(*args)
    return inner

@Outer
def Data(*args):
    print(args)

Data(1,"omkar")
"""


"""import time

def Outer(func):
    def inner(*args):
        start=time.time()
        func(*args)
        end=time.time()
        print(end-start)
    return inner
@Outer

def Check():
    print("its working")
Check()"""

import time

def Outer(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return inner

@Outer

def Check():
    print("its working")
Check()

#Regular expression
#Data type question
#gerators (methods in genrator) and function 
#Program treacing
#
