"""
#Function: 
# -Set of statement or block of code it will execute when we call the function name. 
# -without execute when we call the fuction name. 
# - Without calling the function name it will won't execute it will show blank space.

#Types of function:
#1) Predefine Function
#2)  User Define Function

                               #User Defined Function
#                                         |
#                                         |
#                                 _______________
#                                |               |
#           Without using return keyword     with using return keyword

# Sytax:
#  def Function_name(Parameters):
#      Statement ---|__ block of code/set of statement
#      Statement ---|


#  Function_name(argumment)

#def-----> keyword
#Function_name------> Name given to function it can be any name.
#parameter-----> Varable deceleration(can be optional)
#: ------> code Starting point.
#def Function_name(Parameters):-------> Function deceleration.
# argument-----> varabile value.(can be optional) 
#   Function_name(argumment)--------> function calling.
# 

def Greet():
    print('Good Morning!!!')

Greet()
#print(Greet())
#Greet
#print(Greet)

#Inside the function if we use print() function while calling again no need to use,
#print() function if we use it will display out+None.

#-If we call function without parenthisis() it give blank as error, it will act like a normal word.
#-But the word will point to whole function address.

def even(a):
    if a%2==0:
        print(a," is even number.")
    else:
        print(a, " is odd number.")
even(10)
even(11)


def even_odd():
    a=int(input('enter the number: '))
    if a%2==0:
        print(a," is even number.")
    else:
        print(a, " is odd number.")
even_odd()

def palindrome():
    a=input('Enter the string.')
    if a[::-1]==a:
        print('String is palindrome.')
    else:
        print('String is not palindrome.')
palindrome()

def palindrome(a):
    if a[::-1]==a:
        print('String is palindrome.')
    else:
        print('String is not palindrome.')
palindrome('Hii')
palindrome('MOM')
palindrome('HoH')

d=[1,2,3,4,5,6,7]
def even_odd(d):
    for i in d:
        if i%2==1:
           print('Odd number in list: ',i)

even_odd(d)


s=["Back","Welcome","Hi","markout","deal","done"]

def even_length(s):
    for i in s:
        if len(i)%2==0:
            print('Words with even length: ',i)
even_length(s)
"""

        