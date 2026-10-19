#Q) WAP to print reverse of given int values.
"""a=['hii',78,96,123,False,421]
rev=[]
i=0
for i in a:
    if type(i)==int:
        r=str(i)
        rev.append(r[::-1])
print(rev) 

#a=[100,200,60,40]
#output[300,200,340,360]

a=[100,200,60,40]
out=[]
for i in a:
   sum=0
   for j in a:
     sum+=j
     out.append(sum-i)
print(out) 

#z='i hate you'
#{'i':1,'hate':2,'you':2}

z='i hate you'

out={}
w=z.split()
for i in w:
    count=0
    for j in i:
      if j in 'AEIOUaeiou':
         count+=1
    out[i]=count       
print(out) """

a='kabab is love'
out={}
for i in a.split():
    count=0
    for j in i:
        if j in 'AEIOUaeiou':
          count+=1
out[i]=[i[::-1],count,i[::2]]    
print(out)
        
    

    




    

     
