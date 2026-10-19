# a='rohit'
# for i in a:
    #print(i)
    #print(str(i))
    #print(list(i))
    #print(dict(i))

# a=('rohit',1,2,3,'Ravi')
# for i in a:
#     print(i)

# a=['rohit','Ravi','Ravan','Rudra','Rajesh']
# for i in a:
#     print(i)

#Q) To print each element on new line.
# a={'rohit':1,"Pravin":2,"Ram":3}
# for i in a:
#     print(i,a[i])

# a=(1,2,3,4,5,6)
# for i in a:
#     print(i)

# a={1,2,3,4,5,6}
# for i in a:
#     print(i)

#WAP to calculate and print the numbers of items in list.
# a=eval(input('Enter the data: '))
# count=0
# for i in a:
#     count+=1
#     print(count)

#WAP to reverse a string.
# a=input('Enter the string: ')
# rev=''
# for i in a:
#     rev=i+rev
# print(rev)

#Q) WAP to remove duplicate values from list.
# a=eval(input('Enter the values: '))
# out=[]
# for i in a:
#     if i not in out:
#         out.append(i)
# print(out)
#Q) WAP to print even and odd numbers.
# even=[]
# odd=[]
# for i in range(1,21):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd)
# print(even)

#Q) WAP to print owels and consonanats from given input.
# a='PRATISHA'
# owl=[]
# con=[]
# for i in a:
#     if i in 'AEIOUaeiou':
#         owl.append(i)
#     else:
#         con.append(i)
# print(owl,' are owels in given input.')
# print(con,' are not owels.')

#WAP to print indivdual values and grouped values.
# a=[1,9+45J,'MEENA',['SUMA','KAMALA'],True,9.5,('YUNO','ASTA')]
    # ind=[]
    # grp=[]
    # for i in a:
    #     if type(i) in (int,float,complex,bool):
    #         ind.append(i)
    #     else:
    #         grp.append(i)
    # print(ind,' Individual datatype.')
    # print(grp,' Group datatype.')

#Q) WAP to print individual values
# a=[1,9+45J,'MEENA',['SUMA','KAMALA'],True,9.5,('YUNO','ASTA')]
# out=0
# for i in a:
#     if type(i) in (int,float,complex,bool):
#         out+=1
# print(out)

#Q) WAP to print the count of uppercase, lowercase, numbers, whitespace and special characters 
# from given input.

# a="COME23 regul@rly2 FOR c!@ss donkey!4#"
# upper=0
# lower=0
# white=0
# special=0


# for i in a:
#     if a.isupper():
#         upper+=1     
#     elif a.islower():
#         lower+=1   
#     elif a.isspace():
#         white+=1
#     else:
#         special+=1
# print('count of upper char is ',upper)
# print('count of lower char is ',lower)
# print('count of white space is ',white)
# print('count of special char is ',special)

#Q) WAP to print ascii value of input.

# s = input('Enter a character: ')
# if len(s) == 0:
#     print('No input provided.')
# else:
#     print(ord(s))

# a=input('Enter the characters: ')
# for i in a:
#     print(ord(i))

# u=['rani','ring','ramya','suresh','tarak','dingi','hir','durgesh']
# d={}
# for i in u:
#     if len(i)%2==0:
#         d[i]=i
#     else:
#         d[i]=i[::-1]
# print(d)

# a={'name': 'mina', 'sachin': 10, 45: 'rohit', 'hima': 'hema', 'dhoni': 7, 'sangakara': 40}
# d={}
# for i in a:
#     if type(i)==str and type(a[i])==int:
#         d[i]=a[i]
# print(d)

# c={'name':45,'abc':7.7,'xyz':9.6,'run':4.5,'kho':10.50,'opps':1.5}
# mul=1
# for i in c:
#     if type(c[i]) == float:
#         mul=mul*c[i]
# print(mul)

