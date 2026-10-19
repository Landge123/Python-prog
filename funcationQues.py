#Q1) WAP to check positive num. 
# def positive(a):
#     if a>=0:
#         print("Positive Number.")
# print(positive(4))

#Q2) WAP to check negative num.
# def negative(a):
#     if a<0:
#         return True
# print(negative(-4))

#Q3) WAP check.
# def Zero(a):
#     if a==0:
#         return True
#     else:
#         return False
# print(Zero(0))
# print(Zero(1))
# print(Zero(-1))

#Q4) WAP to check vote eligibility of voting.

# def Vote(a):
#     if a>=18:
#         return print("Eligible")
#     else:
#         return print("Not")
# Vote(17)
        

#Q5) WAP to check driving eligibility of voting.

# def drive(a):
#     if a>=18:
#         return print("Eligible")
#     else:
#         return print("Not")
# drive(17)

#Q6) WAP for student passing.

# def passed(a):
#     if a>=36:
#         return print("Pass")
#     else:
#         return print("Fail")
# passed(17)
        
#Q7) WAP Salary eligible 10000

# def salary(a):
#     if a>=10000:
#         return print("Eligible for salary")
#     else:
#         return print("Not eligible for salary")
# salary(5000)
       
#Q8) WAP for adult person

# def adult(a):
#     if a>=18:
#         return print("Adult")
#     else:
#         return print("child")
# adult(17)

#Q9) WAP to check temprature.

# def temp(a):
#     if a>=36:
#         return print("Hot")
#     else:
#         return print("cold")
# temp(37)

#Q10) WAP to check ATM balance.
  
# def atm(a):
#     if a>=0:
#         return print("Balance is not zero")
#     else:
#         return print("zero balance")
# atm(17)

#Q11&12) WAP to check even and odd

# def check(a):
#     if a%2==0:
#         return print("Even")
#     else:
#         return print("Odd")
# check(9)

#Q13) div 5

# a=int(input("enter the number: "))
# def div(a):
#     if a%5==0:
#         return print("div by 5")
#     else:
#         return print("not div by 5")
# div(a)

#Q14) Div 10

# a=int(input("enter the number: "))
# def div(a):
#     if a%10==0:
#         return print("div by 10")
#     else:
#         return print("not div by 10")
# div(a)

#Q15) div 3

# a=int(input("enter the number: "))
# def div(a):
#     if a%3==0:
#         return print("div by 3")
#     else:
#         return print("not div by 3")
# div(a) 

#Q16) Mul 7

# a=int(input("enter the number: "))
# def mul(a):
#     if a%7==0:
#         return print("multiple of 7")
#     else:
#         return print("not mul of 7")
# mul(a)

# #Q17) check for leaf year

# a=int(input('Enter the year: '))
# def leap(a):
#     if a%4==0 and a%100!==0 or a % 400 == 0:
#         return print("leap year")
#     else:
#         return print("Not leap")
# leap(a)

#Q18 
# a=int(input("enter the number: "))
# def cube(a):
#     if a**3>500:
#         return print("greater")
#     else:
#         return print("smaller")
# cube(a)

#Q19
# a=int(input("enter the number: "))
# def sq(a):
#     if a**2>100:
#         return print("greater")
#     else:
#         return print("smaller")
# sq(a)


#Q20 ends with zero
# a=int(input("enter the number"))
# def z(a):
#     if str(a[-1])==0:
#         return print("ends with 0")
# z(a)

# #Q21) Check empty string.
# a=input("enter the value: ")
# def check(a):
#     if len(a)==0:
#         return print("string is empty")
# check(a)

#Q22 name start with a 

# a=input("enter the string")
# def z(a):
#     if a[0] in 'Aa':
#         return print("starts with a")
# z(a)

#Q23 name ends with n 

# a=input("enter the string")
# def z(a):
#     if a[-1] in 'Nn':
#         return print("ends with n")
# z(a)


# #Q24 Check len gret than 5.
# a=input("enter the value: ")
# def check(a):
#     if len(a)>5:
#         return print("length is greater than 5")
# check(a)


#Q25 check uppercase

# a=input("enter the string: ")
# def up(a):
#     if a.isupper():
#         return print("uppercase")
# up(a)

# #Q26
# a=input("enter the string: ")
# def up(a):
#     if a.isalpha():
#         return print("alphabet")
# up(a)

# #Q27
# a=input("enter the string: ")
# def up(a):
#     if a.isnum():
#         return print("num")
# up(a)

# #Q28
# a=input("enter the string: ")
# def up(a):
#     if a.isalnum():
#         return print("alphanumeeric")
# up(a)

# #Q29
# a=input("enter the string: ")
# def up(a):
#     if a.isalnum():
#         return print("alphanumeeric")
# up(a)

# #Q30
# a=input("enter the string: ")
# def up(a):
#     if a.isspace():
#         return print("space is present")
# up(a)


# # #Q31) Check empty string.
# a=eval(input("enter the list "))
# def check(a):
#     if len(a)==0:
#         return print("list is empty")
# check(a)

# #Q32) Check empty string.
# a=eval(input("enter the list "))
# def check(a):
#     if len(a)>5:
#         return print("length is greater than 5")
# check(a)

#Q33
# num=int(input("enter the number"))
# a=eval(input("enter the list "))
# def check(a):
#     if num in a:
#         return print("num is present")
# check(a)

# #Q34 num largest than 100

# a=int(input("enter the number: "))
# def sq(a):
#     if a>100:
#         return print("greater")
#     else:
#         return print("smaller")
# sq(a)


# #Q35 smaller than 0 

# a=int(input("enter the number: "))
# def sq(a):
#     if a<0:
#         return print("smaller")
#     else:
#         return print("greater")
# sq(a)


# #Q36
# a=int(input("enter the 1 number: "))
# b=int(input("enter the 1 number: "))
# def sq(a,b):
#     if (a+b)>100:
#         return print("grater")
#     else:
#         return print("smaller")
# sq(a)

# #Q37 sort given list
# a=eval(input("enter the list"))
# def sort1(a):
#     return print(a.sort())
# sort1(a)


#Q38  age >80  sal>30000

age=int(input("enter the age"))
     