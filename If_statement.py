#Wap to check wether he/she is eligible to vote or not.

"""age=int(input('Enter the age: '))
if age>=18:
    print('He/She is eligible to vote...')"""

#Wap to check whether the software lanaguage is present inside a list or not.


"""a=input('Enter the language: ')
b=['C++','Java','Python','SQL','Manual','apttitude']
if a in b:
    print('Language is present in list')"""

#WAP to check wether the renter charecter is alphbet or not

"""c=input("Enter your character: ")
if ('a'<= c <='z') or ('A'<= c <='Z'):
    print('Enter char is alphbet.')"""

#WAP to check wether the number is negative or not.

"""a=int(input('Enter your number: '))
if a<0:
    print('Negative number')"""

#WAP to check wether the entered number is divisible by both 2 and 6, if the condition is true then convert the number into complex number.

"""a=int(input('Enter the number: '))
if (a%2== 0) and (a%6==0):
    print(complex(a)) """


"""a=input("Enter your value: ")
if isinstance(a, str):
  print('This is a string.')"""

#19 wap to check whether a given value is dividible by 5 and7,if the value is 
# divisible then display the square of the values (take user input )

"""a=int(input("Enter your value: "))
if(a%5==0) and (a%7==0):
  print(a*a)"""

22# Wap to checked whether value is charecter or not, if it is  store it in dict in key value pair of ascci values.

"""ch=input('Enter the charater: ')
out={}
if('a'<=ch<='z') or ('A'<=ch<='Z'):
    out[ch]=ascii(ch)
    print(out)"""

#23wap to check whether a character is in uppercase or not, if uppercase, convert it to lowercase and store the value inside the divtionary(character as key and value ascii as value) take the user input.
out={}
a=input('Enter the character: ')

if a.isupper():
    low=a.lower()
    out[low]=ascii(low)
    print(out)