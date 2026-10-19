"""Q1)
num=int(input('Enter the number: '))
if 0<=num<=25:
    print('The range is from 0 to 25.')
elif 26<=num<=50:
    print('The range is from 26 to 50.')
elif 51<=num<=100:
    print('The range is from 51 to 100.')
else:
    print('The number is out of range.') """

#Q2) write the program to check entered brand is present in bar.

""" brand=input('Enter the brand name: ')
if "beer" in brand:
    print('your first selection is present')
elif "teacher" in brand:
    print ('your second selection is present')
elif "old monk" in brand:
    print ('your third selection is present')
elif "bro code" in brand:
    print ('your fourth selection is present')
else:
    print ('Close the bar and die.') """

#Q3) write a program to check at which quadotent the value are present.

""" n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))
if n1>=0 and n2>=0:
    print('The numbers are in first quadrant.')
elif n1>=0 and n2<0:
    print('The numbers are in second quadrant.')
elif n1<0 and n2>=0:
    print('The numbers are in third quadrant.')
elif n1<0 and n2<0:
    print('The numbers are in fourth quadrant.')
else:
    print('The numbers does not belong to any quadrant.') """

#Q4 WAP to check greatest of three number.

""" a=int(input('Enter 1st the number:'))
b=int(input('Enter 2nd the number:'))
c=int(input('Enter 3rd the number:'))

if a>b and a>c:
    print(a, 'is greatest of three.')
elif b>a and b>c:
    print(b, 'is greatest of three.')
elif c>a and c>b:
    print(c, 'is greatest of three.')
else:
    print('Invalid input.') """

#q5 find lowset of three number.

""" a=int(input('Enter 1st the number:'))
b=int(input('Enter 2nd the number:'))
c=int(input('Enter 3rd the number:'))

if a<b and a<c:
    print(a, 'is lowest of three.')
elif b<a and b<c:
    print(b, 'is lowest of three.')
elif c<a and c<b:
    print(c, 'is lowest of three.')
else:
    print('Invalid input.') """

#Q6) Write program to check wether a enter character type.

""" a=input('Enter the charater:')
if a.isupper():
    print(a, 'character is uppercase.')
elif a.islower():
    print(a, 'character is lowercase.')
elif a.isdigit():
    print(a, 'character is digit.')
else:
    print(a, 'character is special case.') """

#Q7 WAP to check divisibility by 3 and 5
"""a=int(input('Enter the number: '))
if a%3==0 and a%5==0:
    print('Fizz Buzz.')
elif a%3==0 and a%5!=0:
    print('Fizz Fizz.')
elif a%3!=0 and a%5==0:
    print('Buzz')
else:
    print('No Buzz and Fuzz') """

# WAP if input is string return its length, else if input is list pop elements, else if input 
# is tuple reverse else invalid input.

""" a=input("Ennter the values: ")
if isinstance(a, str):
    print(len(a))
elif isinstance(a,list):
    a.pop()
    print("Empty")
elif isinstance(a,tuple):
    rev=a[::-1]
    print(rev)
else:
    print("Invaid Input.") """

#WAP to give a hike to an employee based on his experience, u should ask employee date of joining  exp 0 to 2 years no hike and 3 to 5 
#years 5000rs hike, and 6 to 8 years 7000rs and 9 to n years 1000rs


""" jy=int(input('Enter year of joining: '))
s=int(input('Enter salary: '))
cy=2026
if cy-jy<=2:
    print('No hike in salary.')
elif cy-jy>=3 and cy-jy<=5:
    print('Hike is salary your salary is', s+5000,'rs.')
elif cy-jy>=6 and cy-jy<=8:
    print('Hike is salary your salary is', s+7000,'rs.')
elif cy-jy>=9:
    print('Hike is salary your salary is', s+10000,'rs.')
else:
    ('Invalid Input') """

#WAP to check height of the student and make the stand in order.

h=float(input("enter student height: "))
if 5.0<=h<=5.4:
    print('Student height is less.')
elif 5.5<=h<=5.9:
    print('Student height is average.')
elif 6.0<=h:
    print('Student height is extra ordinery.')
else:
    print('very small height.')




# WAP to give discount to customer based on total price (p1+p2+p3) 1000 to 3000 price discount 500 
# and price 3001 to 5000 discount 1000 more than 5001 price 1200 discount and less than 1000 no discount. 

""" p=int(input('Enter total spending: '))
if p<1000:
    print('No discount.')
elif 1000>=p<=3000:
    print('You got a discount of 500rs, final price is ',p-500,'rs.')
elif 3001>=p<=5000:
    print('You got a discount of 1000rs, final price is ',p-1000,'rs.')
elif 5001<p:
    print('You got a discount of 1200rs, final price is ',p-1200,'rs.')
else:
    print('better luck next time.') """

#WAP to check signal light color=[red,yellow,green]

"""color=input("Enter the signal color: ")
if color=="red":
    print("Stop at signal.")
elif color=="yellow":
    print("Start your car.")
elif color=="green":
    print("lets go.")
else:
    print('Invalid signal.') """

#