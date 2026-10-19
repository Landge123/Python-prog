""" q1) 
a=int(input('Enter your number: '))
if a%2==0:
  print('Square of number is',a*a) 


q2)
ch=(input('Enter the character: '))
if ch in 'aeiouAEIOU':
   print("Character is vowel")


 q3)
ch=input('Enter the character: ')
if ch.isupper:
    print(ord(ch))

q4)
num=int(input('Enter the number: '))
if num%9==0 or num%6==0:
    print('The cube of number is ',num*num*num)


q5)
num=int(input('Enter the number: '))
if 100<=num<=999:
    print('Three digit number ',num)

q6)
num=int(input('Enter the number: '))
if num%10==5:
    print('The last digit is 5.')


q7)
num=input('Enter the number: ')
if type(num)==float:
    print('Entered number is float.')


q8)
a=eval(input('Enter the value: '))
if type(a) in (int,float,str,bool):
    print('Single value datatype.')


q9)
num=input('Enter the value: ')
if num.isdigit():
    print('The  value is digit.')


q10)
num=int(input('Enter the number: '))
if num%3==0:
    print('The number is muliple of 3.')


q11)
a=eval(input('Enter the value: '))
if type(a) in (list,tuple,dict):
    print('Mutable data type.')
else:
    print('immutable data types.')

q12)
num=input('Enter the value: ')
if num.isdigit():
    print('The  value is digit.')
else:
    print('Not a digit.')  

q13)
ch=input('Enter the character: ')
if ch.isalnum:
    print('Is a special character.')
else:
    print('not a special character.') 

q14)
list=input('enter the list: ')
n=len(list)
if n//2!=0:
    print('List has middle value.')
else:
    print('Does not have middle value.') 

q15)
num=int(input('Enter the number:'))
if num%2==0:
    print('The number is even.')
else:
    print('The number is odd.') 

q16)
a=eval(input('Enter the value: '))
if type(a) in (list,tuple,dict):
    print('Mutable data type.')
else:

q17)
a=input('Enter the 1st value: ')
b=input('Enter the 2nd value: ')
print('Id id a is',id(a))
print('Id id a is',id(b))
if a is b:
    print('Pointing same memeory.')
else:
    print('Not pointing same memeory.') 
    
    
q18)
t=(1,2)
homo=type(t[0])==type(t[1])
if homo:
    print('Tuple is homogeneous.')
else:
    print('Not homogenous.')  """

s=input('Enter the string: ')
