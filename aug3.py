"""
Q1)
for i in range(1,11):
    if i==5:
        continue
    print(i)

Q2)    
a=[2,12,23,21,45,34,56]

# print({i:i**2 for i in range(1,6)})
print({i:i**3 for i in range(1,16)if i%2!=0})
print({i:i**2 for i in range(1,6) if i%2==0}) 

print({i:i**2 for i  in range(1,10) if i%2==0 else i:i**3 })

Q) swap key and value.
a={'a':'ram','Age':'b','Addres':"Pune"}
# print({v:k for k,v in a.items() })
# print({v:len(v) for v in a.values() })

# print({f:len(f) for f in a.values() })

#Q) WAP to crate a dictionary of values and index pair.
# l=["google","apple","python","orange"]
l=["google","apple","python","orange"]
print({k:v for v,k in enumerate(l)}) 


#Q) WAP to print first caracter if word is even and if odd print whole
l=["google","apple","python","orange"]
print({i:i if len(i)%2==0 else i[::-1] for i in l}) """




#Q) WAP tp check length of words and create a dict having word and word pair if it 
#is 

