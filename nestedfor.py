"""
#Q1) print below pattern
* 
* * 
* * * 
* * * * 

for i in range(1,5,1):
    for j in range(i):
        print('*',end=" ")
    print()

#2) print below pattern
* * * * 
* * * 
* * 
* 

for i in range(4,0,-1):
    for j in range(i):
        print('*', end=" ")
    print()

#3)  print below pattern

        * 
      * * 
    * * * 
  * * * * 
* * * * * 

for i in range(1,6,1):
    for j in range(5-i):
        print(' ', end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

#4) print below pattern
* * * * * 
  * * * * 
    * * * 
      * * 
        * 

for i in range(5,0,-1):
    for j in range(5-i):
        print(' ', end=" ")
    for j in range(i):
        print("*",end=" ")
    print()


#5) print below pattern

                * 
              * * * 
            * * * * * 
          * * * * * * * 
        * * * * * * * * * 

for i in range(1,5,1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in  range(2*i-1): 
        print("*",end=" ")
    print()

#6) print below pattern


        * * * * * * * * * 
          * * * * * * * 
            * * * * * 
              * * * 
                * 


for i in range(5,0,-1):
    for j in range(5-i):
        print("-",end=" ")
    for j in  range(2*i-1):
        print("*",end=" ")
    print()


for i in range(1,6,1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in  range(2*i-1): 
        print("*",end=" ")
    print()
for i in range(4,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in  range(2*i-1):
        print("*",end=" ")
    print()



for i in range(1,6,1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in  range(2*i-1): 
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in  range(2*i-1):
        print(j,end=" ")
    print()

#Date 2 Sep
Q1) 1.Increasing Numbers
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

for i in range(1,6,1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


Q2) Repeated Numbers
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

for i in range(1,6,1):
    for j in range(i):
        print(i,end=" ")
    print()
 
Q3.Reverse Numbers
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

Q4.Increasing Alphabets
A
A B
A B C
A B C D
A B C D E

for i in range(1,6,1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
 
Q5. Repeated Alphabets
A
B B
C C C
D D D D
E E E E E

for i in range(0,6,1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

3.Continuous Numbers
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15


num=1
for i in range(1,6,1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
   

Q.Reverse Alphabets
A B C D E
A B C D
A B C
A B
A


for i in range(6,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()


num=2
for i in range(1,6,1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=2
    print()


#Q. Print only binary numbers


# for i in range(1,6,1):
#     for j in range(1,i+1):
#         print((i+j)%2,end=" ")
#     print()

for i in range(1,6,1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
"""

# for i in range(1,6,1):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in  range(2*i-1): 
#         print("*",end=" ")
#     print()
for i in range(4,0,-1):
    for j in range(5-i):
        if (i+j)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()