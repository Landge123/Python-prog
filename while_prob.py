#Q1)WAP to extract palindromes string present in side the given list.

# words=["radar", "hello", "madam", "world", "racecar", "noon"]
# palindromes = []
# i=0
# while i<len(words):
#     if words[i]==words[i][::-1]:
#         palindromes.append(words[i])
#     i+=1
# print("Palindromes:", palindromes)

#Q2)WAP to find the sum of individual digits present inside a given int number.

# number = 12345

# digit_sum = 0
# temp_num = abs(number)

# while temp_num > 0:
#     last_digit = temp_num % 10
#     digit_sum += last_digit
#     temp_num = temp_num // 10

# print(f"The sum of individual digits of {number} is: {digit_sum}")


#Q3) FETCH INTEGER VALUES FROM LIST:
'''l=[12,'nikhi',34,56]
i=0
while i<len(l):
    if type(l[i])==int:
        print(l[i])
    i+=1'''

#Q4) I/P=['PYTHON','IS','EASY'],o/p
'''l=['Python','is','easy']
i=0
d=""
while i<len(l):
    d=d+str(len(l[i]))
    i+=1
print(d)'''

#Q5) 
# s=input('Enter a string: ')
# i=0
# sp=0
# while i<len(s):
#     if s[i].isalnum()==False:
#         sp=sp+ord(s[i])
#     i+=1
# print(sp)

#a=['python','is','easy']

#Q) WAP to print prime number.

# num=int(input('Enter the number: '))
# i=1
# out=[]
# while i<=num:
#     if num%i==0:
#         out.append(i)
#     i+=1
# if len(out)==2:
#     print('Entered number is prime number',num)
# else:
#     print('Entered number is not a prime number.')

#Q) WAP tp find the factorial for 28.

# num=28
# i=1
# out=[]
# while i<=num:
#     if num%i==0:
#         out.append(i)
#     i+=1
# if len(out)==2:
#     print('Factorials of ',num, 'are', out)
# else:
#     print('The factorial of 28 are: ', out)

#Q) WAP to print a perfect number.
# num=int(input('Enter the number: '))
# i=1
# out=0
# while i<num:
#     if num%i==0:
#         out=out+i
#     i+=1
# if out==num:
#     print('Number is perfect.')
# else:
#     print('Else number is not perfect')

#Q)Write a program to print a amstrong number.

# num=int(input('Enter the number: '))
# length=len(str(num))
# dum=num
# rev=0
# while num>0:
#     l_d=num%10
#     rev=rev+l_d**length
#     num=num//10
#     length-=1
# if rev==dum:
#     print('diserium number')
# else:
#     print('Not a diserium number.')

#Q) Find the HCF of 2 numbers.

# n1=8
# n2=12
# i=1
# hcf=0
# while i<=n1 and i<=n2:
#     if n1%i==0 and n2%i==0:
#         hcf=i
#     i+=1
# print('HCF for the given number is ',hcf) 

#Q) WAP to print all alphbates .
# i=65
# while i<=90:
#     print(chr(i),end=" ")
#     i+=1

#Q) WAP TO REVERSE A NUMBER.
# num=int(input('Enter a number: '))
# org_num=num
# rev_num=0
# while num >0:
#     rev=num%10
#     rev_num=(rev_num*10)+rev
#     num=num//10
# print(rev_num)


#Q) WAP TO CHECK WHETHER A NUMBER IS PALINDROME OR NOT .

# num=int(input('Enter the number.'))
# temp = num
# rev_num=0
# while temp >0:
#     rev=temp%10
#     rev_num=(rev_num*10)+rev
#     temp=temp//10
# if num==rev_num:
#    print("Palindromes:", num)
# else:
#     print('Not a palindrome.')

# Q) WAP TO CHECK THE LENGTH OF THE STRING WITHOUT USING LEN() FUNCTION.

# s=input('Enter the string: ')
# temp_string = s
# i = 0
# while temp_string:
#     i += 1
#     temp_string = temp_string[1:]

# print(i)

#Q) WAP TO REVERSE A STRING WITHOUT SPLICING

# s=input('Enter the string: ')
# i=0
# for character in s:
#     i += 1

# reversed_string = ""
# index = i - 1  

# while index >= 0:
#     reversed_string += s[index]  
#     index -= 1                             
# print(reversed_string)

#Q)  WAP TO PRINT THE FOLLOWING OUTPUT...
#I/P--'abcd' --:o/p{'a':97,'b':98.... 

# string = 'abcd'
# output_dict = {}

# slength = 0
# for character in string:
#     slength += 1
# i = 0
# while i < slength:
#     character = string[i]       
#     output_dict[character] = ord(character) 
#     i += 1                            
# print(output_dict)

#WAP to print the square of entered number and square of before numbers.

# num=int(input('Enter the number: '))
# i=1
# while i<=num:
#     print(i*i,end=' ')
#     i+=1

#WAP to print the square of entered number and square of before numbers.

# num=int(input('Enter the number: '))
# i=1
# while i<=num:
#     print(i*i*i,end=' ')
#     i+=1

# a="COME23 regul@rly2 FOR c!@ss donkey!4#"
# upper=0
# lower=0
# digit=0
# white=0
# special=0


# for i in a:
#     if i.isupper():
#         upper+=1     
#     elif i.islower():
#         lower+=1  
#     elif i.isdigit():
#         digit+=1 
#     elif i.isspace():
#         white+=1
#     else:
#         special+=1
# print('count of upper char is ',upper)
# print('count of lower char is ',lower)
# print('count of numbers is ',digit)
# print('count of white space is ',white)
# print('count of special char is ',special)

# wAP for sum of n natural numbers.

# n=int(input("Enter the number: "))
# add=0
# i=1
# while i<=n:
#     add+=i
#     i+=1
# print(add)

# wAP for multipication of n natural numbers or factorial number.

# n=int(input("Enter the number: "))
# mul=1
# i=1
# while i<=n:
#     mul*=i
#     i+=1
# print(mul)

# WAP to print character from given string.

# s=input("enter the string: ")
# i=0
# while i<len(s):
#     print(s[i],end=" ")
#     i+=1

#WAP to fetch only lowercase from a string.

# s=input("Enter the string: ")
# i=0
# out=" "
# while i<len(s):
#     if 'a'<=s[i]<='z':
#         out+=s[i]
#     i+=1
# print(out)

                     #OR

# s = input("Enter the string: ")
# i = 0

# while i < len(s):
#     if 'a' <= s[i] <= 'z':
#         print(s[i], end=" ")
#     i += 1


# Q) WAP to seprate even and odd numbers

# l=eval(input("Enter the list: "))
# even=[]
# odd=[]
# i=0
# while i<len(l):
#     if l[i]%2==0:
#         even.append(l[i])
#     else:
#         odd.append(l[i])
#     i+=1
# print("Even numbers: ",even,end=" ")
# print()
# print("Odd numbers:",odd,end=" ")
        
#Q WAP to fatch special character from string.

# s=input('Enter a string: ')
# i=0
# out=''
# while i<len(s):
#     if not s[i].isalnum():
#          out+=s[i] 
#     i+=1      
# print(out)

                      # OR

# s = input("Enter the string: ")
# i = 0

# while i < len(s):
#     if not ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9'):
#         print(s[i], end=" ")
#     i += 1

                             #OR

# s = input("Enter the string: ")
# i = 0

# while i < len(s):
#     if not s[i].isalnum():
#         print(s[i], end=" ")
#     i += 1


#Q) WAP to seprate even and odd numbers from tuple

# l=eval(input("Enter the tuple: "))
# even=()
# odd=()
# i=0
# while i<len(l):
#     if l[i]%2==0:
#         even+=(l[i],)
#     else:
#         odd+=(l[i],)
#     i+=1
# print("Even numbers: ",even,end=" ")
# print()
# print("Odd numbers:",odd,end=" ")


# s = input('Enter the string: ')
# upper = ''
# lower = ''
# num = ''
# space = ''
# special = ''

# i = 0
# while i < len(s):
#     if s[i].isupper():
#         upper += s[i]
#     elif s[i].islower():
#         lower += s[i]
#     elif s[i].isdigit():
#         num += s[i]
#     elif s[i].isspace():
#         space += s[i]
#     else:
#         special += s[i]
#     i += 1

# print("The upper char: ", upper)
# print("The lower char: ", lower)
# print("The numbers: ", num)
# print("The spaces: ", space)
# print("The special characters: ", special)

# Q) Reverse the string [without slicing and buildin function]

# s=input("Enter the string: ")
# rev=' '
# i=0

# while i<len(s):
#     rev=s[i]+rev
#     i+=1
# print(rev)

# s=input('Enter the strimg: ')
# i=0
# rev=''
# while i<len(s):
#     rev=s[i]+rev
#     i+=1
# if rev==s:
#     print('String is palindrom')
# else:
#     print('String is not a palindrom')

# WAP to fatch last digit 
# num=int(input('Enter a number: '))
# rev_num=0
# while num >0:
#     last_digit=num%10
#     rev_num=(rev_num*10)+last_digit
#     num=num//10
# print(rev_num)


# num=int(input('Enter the number:'))
# temp = num
# rev_num=0
# while temp >0:
#     rev=temp%10
#     rev_num=(rev_num*10)+rev
#     temp=temp//10
# if num==rev_num:
#    print("Palindromes:", num)
# else:
#     print('Not a palindrome.')


l=[10,45.18,'hello',20,50,4j+5,'bye',40]
i=0
sum=0
while i<len(l):
    if type(l[i])==int:
        sum=sum+l[i]
    i+=1
print(sum)