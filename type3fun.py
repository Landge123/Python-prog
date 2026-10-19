#TYPE 3 FANCTION
#Q1)
# def conso():
#     a=input("Enter string: ")
#     out=''
#     for i in a:
#         if i not in 'aeiouAEIOU':
#             out=out +i
#     return out
# print(conso())

#Q2)
# def con():
#     a = ['Hello', 92, 32, 'Mina', 'Mayuri', 'Mokshi']

#     out = []

#     for i in a:
#         if type(i) == str:
#             out.append(i)

#     var = '*'.join(out)
#     return var

# print(con())

#Q3)
# def fun():
#     a = ['Python.py', 'File2.csv', 'File.txt', 'File2.csv']

#     out = []
#     for i in a:
#         dum = i.split('.')
#         out.append(dum[-1])
#     return out

# print(fun())

#Q4)

# def inc():
#     a1='101110111'
#     a2='000011011'
#     count=0

#     for i in range(0,len(a1)):
#         if a1[i]==a2[i]:
#           count+=1
#     return count
# print(inc())

#TYPE 4 FUNCTION

# def mul(a,b,c):
#     return a*b*c
# result=mul(3,4,5)
# print(result)
            
#featch all the uppercase character from given string.


# def st():
#     a=input("Enter the string: ")
#     for i in a:
#         if i.isupper():
#             print(a,end="")
#     print()
# st()


# def add(a,b):
#     return a+b
# result=add(3,5)
# print(result)


# def sub(a,b):
#     return a-b
# result=sub(3,5)
# print(result)

def cal(num1,num2,operator):
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2:
    elif operator=='/':
        return num1/num2:
    else:
        print("Invalid operator")
    

