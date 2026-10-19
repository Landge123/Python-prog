"""
a=[5,9,7,6,12,14,192,22]
for i in a:
    if i>10:
        break
    print(i,end=' ') 

q='Good Morning'
for i in q:
    if i=='r':
        break
    print(i,end=' ')

for i in range(1,25):
    if i>13:
        break
    print(i,end=' ')  

a='Praveen Kumar'
for i in a:
    if i in 'aeiouAEIOU':
        continue
    print(i,end=' ') 
d=[-120,7,8,-100,90,20,-420]
for i in d:
    if i<0:
        continue
    print(i,end=' ')  

#MAP FUNCTION
a=[1,5,9,10,30]
print(list(map(lambda x:x**2,a))) 

e=['Shivani','Pratik','Shruti','Omkar']
print(list(map(lambda x:x[0],e)))

#wap to return list of name and length pair.
#namel=["laptop","mouse","board","house","week"]

namel=["laptop","mouse","board","house","week"]
print(list(map(lambda x:(x,len(x)),namel))) 

#WAP to print sum of indices from both list
l1=[2,3,4,5,6]
l2=[3,4,5,8,9]

print(list(map(lambda x,y:x+y,l1,l2)))  

#WAP to return if the key is individual returns its value else return its type

d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}

print(list(map(lambda x:d[x] if type(x) in [int,float,complex,bool,] else type(x),d))) 

#WAP to return a list having even values
l=[4,3,5,6,7,8,10]
print(list(filter(lambda x:x%2==0,l)))

#WAP to return s list having only flowers
l=["sun flowers","banana tree","lily flowers","lotus flowers","mariglod flowers"]
print(list(filter(lambda x:'flowers' in x,l))) 

#WAP to return a listhaving elements which are starting from consonants
l=["hello","guys","please","respond","to","insta","computer"]
print(list(filter(lambda x:x[0] not in "aeiouAEIOU",l)))

#wap to build a list with only even length strings using filter

k=["apple","google","walmart","fb","insta","act","zomato"]
print(list(filter(lambda x:len(x)%2==0,k))) 

#5.WAP to return only positive values in the list using filter

m=[-5,-6,9,-34,90,-28,78,100,89,45,-65] 
print(list(filter(lambda x:x>=0,m))) """


