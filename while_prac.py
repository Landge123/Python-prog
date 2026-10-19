
""" Q1) Print first 10 natural numbers using while loop

i=1
while i<=10:
    print(i)
    i+=1

#Q2) Display numbers from -10 to -1 using for loop 

i=-10
while i<=-1:
    print(i)
    i+=1

#Q3) Display a message “Done” after successful execution of for loop     
   
i=1
while i<=10:
    print(i)
    i+=1
print('Successful')  

#Q4) Calculate the sum of all numbers from 1 to N. 
n=int(input('Enter the number: '))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum) 


#Q4) Calculate the sum of even numbers.

n=int(input('Enter the number: '))
sum=0
i=1
while i<=n :
    if i%2==0:
      sum+=i
    i+=1
print(sum) 

#Q5) Write a peogram to print the table of given input.

n=int(input('Enter the number: '))
i=1
while i<=10:
    print(i*n)
    i+=1  """

#Q6) WAP to print all even numbers than falls between two numbers.

n1=int(input('Enter the 1st number: '))
n2=int(input('Enter the 2nd number: ')) 
if n1>n2:
    while(n2<=n1):
      if n2%2==0:
        print(n2)
      n2+=1
else:
    while(n1<=n2):
      if n1%2==0:
        print(n1)
      n1+=1
         

        




