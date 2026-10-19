#Q1) WAP to print sum of N natural numbers.
# num=int(input('Enter the natural number: '))
# sum=0
# i=1
# while i<=num:
#     sum=sum+i
#     i+=1
# print(sum)

#Q2) WAP to print product of N natural numbers.
# num=int(input('Enter the natural number: '))
# mul=1
# i=1
# while i<=num:
#     mul=mul*i
#     i+=1
# print(mul)

#program to print multiple of 5 and 7 in between 1 to 100.

# i=1
# lt=[]
# while i<=100:
#      if i%5==0 or i%7==0:
#         lt.append(i)
#      i+=1
# # print(lt)

# Q)
# i=0
# while i<6:
#     i+=1
#     if i==3:
#      continue
#     print(i)

# Q) print odd numbers   
# a = 10
# while a<=20:
#     print(a)
#     a+=2

# q)Print powers of 2
# n=128
# i = 2
# while i<=n:
#     print(i)
#     i=i*2
#Q) program to loop of number to print from 10 to 100 while adding 10. 
# i = 10
# while i<=300:
#     print(i)
#     i+=10

# Q) print the following series 105,98,91......
# i = 105
# while i>0:
#     print(i)
#     i-=7

# st=input('Enter the string: ')
# i=0
# while i<len(st):
#     print(st[i],end=" ")
#     i+=1

# st=input('Enter the string: ')
# i=0
# out=''
# while i<len(st):
#    # if st[i].isupper:
#      if 65<=ord(st[i])<=90:
#         out+=st[i]
#      i+=1
# print(out)

# st=input('Enter the value: ')
# i=0
# out1=''
# out2=''
# out3=''
# out4=''
# while i<len(st):
#     if 65<=ord(st[i])<=90:
#         out1+=st[i]
#     elif 97<=ord(st[i])<=122:
#        out2+=st[i] 
#     elif 48<=ord(st[i])<=57:
#        out3+=st[i]
#     else:
#        out4+=st[i]
#     i+=1
        
# print('Characters are uppercase.',out1)
# print('Characters are uppercase.',out2)
# print('Characters is digits.',out3)
# print('Character is speacial characters.',out4)

# Q2)
# a = ['Paru', 'Shiva', 'Urmila', 'Parmila', 'Sheela', 'Uma', 'Suma', 'Komaa', 'Oma', 'On']
# i = 0
# out1 = []  
# out2 = []

# while i < len(a):
#     if len(a[i]) % 2 == 0: 
#         out1.append(a[i]) 
#     else:
#         out2.append(a[i])
#     i += 1

# print('Even number names: ', out1)
# print('Odd number names: ', out2)

#Q3)WAP to marge 2 different lists into dictionary.
# h1=['a','b','c','d']
# h2=[4,5,6,7]
# out={}
# i=0
# while i<len(h1):
#     out[h1[i]]=h2[i]
#     i+=1
# print(out)

#Q4) Write a program to drop a duplicate values.
# a=[10,20,30,40,30,20,10]
# out=[]
# i=0
# while i<len(a):
#     if a[i] not in out:
#         out.append(a[i])
#     i+=1
# print(out)

"""#Q5) WAP to fatch all the string values inside a list

d=['hii',5j+9,10,'Hello',True,False,'Mina',6j+9,False,78.9]
i=0
out=[]
while i<len(d):
    if type (d[i])==str:
        out.append(d[i])
    i+=1
print(out)

#Q6) WAP to fatch all the string & complex values inside a list

d=['hii',5j+9,10,'Hello',True,False,'Mina',6j+9,False,78.9]
i=0
out=[]
while i<len(d):
    if type (d[i]) in (complex,str):
        out.append(d[i])
    i+=1
print(out)


Q7)WAP to extract palindromes string present in side the given list.  

words=["radar", "hello", "madam", "world", "racecar", "noon"]
palindromes = []
i=0
while i<len(words):
    if words[i]==words[i][::-1]:
        palindromes.append(words[i])
    i+=1
print("Palindromes:", palindromes)
#Q8) based on index position if both values are same increase the value of one using while loop

a = '1011011'
b = '0022000'
i = 0
count=0

while i < len(b):
    if a[i] == b[i]:
        count+= 1
    i += 1
print(count) 

#Q9) print the length of string without using length funcation.

a='Pineapple'
count=0

while a[count:]!="":
    count+=1
print(count)

#                or  
a='Pineapple'
count=0
i=0
while i<len(a):
    count+=1
    i+=1
print(count)

Q10) replace whitespceses with star


a='Hi how are you'
i=0
out=''
while i<len(a):
    if a[i]==' ':
        out=out+'*'
    else:
        out=out+a[i]
    i+=1
print(out)


#Q11) WAP to fetch all the  integer values in even index position only 

a=[10,45.5,6.5,1,2,47,90,6.2,4j+9,30]
i=0
out=[]

while i<len(a):
    if i%2==0 and type(a[i]) is int:
        out.append(a[i])
    i+=1
print(out)

#Q12) WAP to check the number of occrance of specified character in a given string.

#a='Keep it up keerti'
a=input("Enter the charcter: ")
b=input('Enter the charcter to check: ')

i=0
count=0

while i<len(a):
    if a[i] == b:
        count += 1
    i += 1

print(count) 
a=eval(input('Enter the list: '))
i=0
out=[]

while i<len(a):
    if a[i] not in out:
        out.append(a[i])
    i+=1
print(out)
 

#Q 13) WAP to find the sum of the cube digits present in a given string.

a='827641'
i=0
out=0

while i<len(a):
    if a[i].isdigit():
        out += int(a[i]) ** 3
    i += 1

print(out)  

#Q14) WAP to extract the integers present in a list only if it is present a odd index. 

a=[10,45.5,6.5,1,2,47,90,6.2,4j+9,30]
i=0
out=[]

while i<len(a):
    if i%2==1 and type(a[i]) is int:
        out.append(a[i])
    i+=1
print(out)

#Q15) WAP to extract factors of the given number.

a=int(input('Enter the number: '))
i=1

while i<a:
    if a%i==0:
        print(i,end=" ")
    i+=1

#Q16) WAP to check weather the number is perfect number or not.


num=int(input('Enter the number: '))
i=1
out=0
while i<num:
    if num%i==0:
        out=out+i
    i+=1
if out==num:
    print('Number is perfect.')
else:
    print('number is not perfect')  

#Q17) WAP to toggle a string.

s=input('Enter the string to toggle: ')
i=0
out=''

while i<len(s):
    if s[i].isupper():
        out += s[i].lower()
    elif s[i].islower():
        out += s[i].upper()
    else:
        out += s[i]
    i += 1

print(out) 

#Q 18) WAP fabonacci series

n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 0

while i < n:
    print(a, end=" ")

    a = 0
    a = b
    b = a+b

    i = i + 1

#Q19) WAP to fetch all ovels from string.

s=input('Enter the string: ')
i=0
out=''

while i<len(s):
    if s[i] in 'aeioue':
        out=out+s[i]
    i+=1
print(out) 
 


#Q21) WAP to consider a homogenous tuple of integers and divide it 2 output in  to even and odd


t=eval(input('Enter the tuple: '))
i=0
out1=[]
out2=[]

while i<len(t):
    if t[i]%2==0:
        out1.append(t[i])
    else:
        out2.append(t[i])
    i=i+1

print('Even numbers: ',out1)
print('Odd numbers: ',out2)


# Q20) WAP to fetch all the string values in a list only if it consists of middle char in it.


s=input('Enter the string: ')
i=0
out=[]

while i<len(s):
    if type(s)==str and len(s[i])%2==1:
        out.append(s[i])
    i+=1
print(out)



num=int(input('Enter the number: '))
i=1
out=0

while i<=num:
    if num%i==0:
        out+=1
    i+=1
if out==2:
    print(num,' is a prime number.')
else:
    print(num,' is not a prime number.')


# Q) armstrong number
num=int(input('Enter the number: '))
temp=num
s=str(num)
p=len(s)
add=0

while num>0:
    last_digit=num%10
    add=add+last_digit**p
    num=num//10
if add==temp:
    print(temp,' is a armstrong number.')
else:
    print(temp, 'not armstrong.')

# Q) Diesirum number.

num=int(input('Enter the number: '))
temp=num
s=str(num)
p=len(s)
add=0

while num>0:
    last_digit=num%10
    add=add+last_digit**p
    num=num//10
    p-=1
if add==temp:
    print(temp,' is a diasrium number.')
else:
    print(temp, 'not diasdrium.')

#Q) Strong number.


from math import factorial

a = int(input('Enter the number: '))
temp = a
add = 0
while a > 0:
    l_d = a % 10
    add += factorial(l_d)
    a //= 10

if add == temp:
    print('strong number')
else:
    print("not a strong number.")
    
#Q) SPT Number.

num=int(input('Enter the number.'))
ad=0
mul=1

while num>0:
    l_d=num%10
    ad=ad+l_d
    mul=mul*l_d
    num=num//10
if ad==mul:
    print('Spy number.')
else:
    print('Not a spy number').

#Q) Xyleom number.

num = int(input('Enter the number: '))
mid_sum = 0
l_d = num % 10
num = num // 10

while num > 9:
    d = num % 10
    mid_sum = mid_sum + d
    num = num // 10

f_d = num

if f_d + l_d == mid_sum:
    print('Xyleom number.')
else:
    print('Not a Xyleom number.')

#Q21) WAP to consider a homogenous tuple of integers and divide it 2 output in  to even and odd

t=eval(input('Enter the tuple: '))
i=0
out1=[]
out2=[]

while i<len(t):
    if t[i]%2==0:
        out1.append(t[i])
    else:
        out2.append(t[i])
    i=i+1

print('Even numbers: ',out1)
print('Odd numbers: ',out2)
    


#Q22) Wap 
i=101
out=[]
while i in range(101,500,1):
    if i%13==0 and i%3!=0:
        out.append(i)
    i+=1
print(out)


#Q23) 
    
#Q24)

words=["radar", "hello", "madam", "world", "racecar", "noon"]
palindromes = []
i=0
while i<len(words):
    if words[i]==words[i][::-1]:
        palindromes.append(words[i])
    i+=1
print("Palindromes:", palindromes)
  
#Q25) 
s=input('Enter the string: ')
upper=[]
lower=[]
num=[]
special=[]
i=0
while i<len(s):
    if s[i].isupper():
        upper.append(s[i])
    if s[i].islower():
        lower.append(s[i])
    if s[i].isdigit():
        num.append(s[i])
    else:
        special.append(s[i])
    i+=1
print(lower)
print(upper)
print(num)
print(special)


s=input('Enter the string: ')
out=''
i=0

while i<len(s):
    if s[i].isupper():
        out+=s[i].lower()
    else:
       out+=s[i].upper()
    i+=1
print(out)

#Q27)
s=input('Enter the value: ')
i=0
out=[]

while i<len(s):
    if s[i].islower() and ord(s[i])%2==0:
        out.append(s[i])
    i+=1


print(out)


s=input('Enter the string: ')
i=0
out={}
b=s.split()

while i<len(b):
    if len(b[i])%2==0:
        mid= len(b[i])//2
        out[b[i]]=b[i][mid-1:mid+1]
    else:
        mid= len(b[i])//2
        out[b[i]]=b[i][mid]

    i+=1
print(out)



#Q29)

s=input('Enter the string: ')
i=1
wordlen=0
sp=s.split()


while i<len(sp):
    curword=len(sp[i])

    if curword>wordlen:
        wordlen=curword

    i+=1
print(wordlen)


#Q30) 
words=["radar", "hello", "madam", "world", "racecar", "noon"]
palindromes = []
i=0
while i<len(words):
    if words[i]==words[i][::-1]:
        palindromes.append(words[i])
    i+=1
print("Palindromes:", palindromes)

# while i<len(words):
#     if words[i]==words[i][::-1]:
#         print(palindromes, 'is a palindromes.')
#     else:
#         print(palindromes, 'not a palindromes.')
#     i+=1

#Q31)a='Python is easy'
#    output: '624'

a='Python is easy'.split()
i=0
out=""

while i <len(a):
    out=out+str(len(a[i]))
    i+=1
print(out,end="")


#Q33)Exract all the vowels from the string & print its next character.

s=input('Enter the string: ')
i=0
out=[]

while i<len(s):
    if s[i] in 'aeiouAEIOU':
        out.append(chr(ord(s)+1))
    i+=1
print(out)


#Q34) input: '14976328'
#      out:'46281973'

a='14976328'
i=0
out1=""
out2=""

while i<len(a):
    if int(a[i])%2==0:
        out1+=a[i]
    else:
        out2+=a[i]

    i+=1
print(out1+out2)



#Q35) input='Hii hello every one'
#     output='iih olleh yreve eno'

s='Hii hello every one'
i=0
rev=''
out=''

while i<len(s):
    if s[i] !=' ':
        rev=s[i]+rev
    else:
        rev=out+rev+' '
        re=''
    i+=1
out+=rev
print(out)


#Q36) A=['a','b','c','d']
#   B: [1,2,3,4]
# output={'a':1,'b':2,'c':3,'d':4}
 
A=['a','b','c','d']
B=[1,2,3,4]
i=0
out={}

while i<len(A) and i<len(B):
    out[A[i]]=B[i]
    i+=1
print(out)


#Q37) A=[1,18,36,45,9,12,113]
# output: [1,3,1,4,2,3]

A=[1,18,36,45,9,12,113]
i=0
out=[]

while i<len(A):

    out.append(A[i]%5)
    i+=1

print(out)



#Q38) a='abc143'
# out=92

a='abc143'
i=0
out=0

while i<len(a):
    if a[i].isdigit():
        out+=(int(a[i])**3)
    i+=1
print(out)

  """

num=12
sq=num*num
temp=num
is_auto=True

while temp>0:
    if temp%10!=sq%10:
        is_auto=False
        break

    temp=temp//10
    sq=sq//10

if is_auto:
    print(num,'is automorphic')
else:
    print(num,'not automorphic')



    


    







    








