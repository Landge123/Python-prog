# i=1
# while i<=5:
#     print(i)
#     i+=1

# i=1
# while i<=5:
#     print(i,end=' ')
#     i+=1

# i=1
# while i<=5:
#     print('vad pav')
#     i+=1

#WAP to print first 10 natural numbers.
# i=1
# while i<=10:
#     print(i)
#     i+=1

#WAP to print first 10 natural numbers in reversed.
# i=10
# while i>=1:
#     print(i)
#     i-=1

#WAP to print tables.
# num=int(input('Enter the number to print table: '))
# i=1
# while i<=10:
#     print(num,'*',i,' =',num*i)
#     i+=1

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
"""

# Q20) WAP to fetch all the string values in a list only if it consists of middle char in it.


s=input('Enter the string: ')
i=0
out=[]

while i<len(s):
    if type(s)==str and len(s[i])%2==1:
        out.append(s[i])
    i+=1
print(out)
