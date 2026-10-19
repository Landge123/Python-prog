"""

"""






""" st=input('Enter the string: ')
if len(st)%2==1:
   if st[len(st)//2].isupper():
      print("Middle character is uppercase.")
   else:
      print("Middle charcter is not uppercase.")
else:
   print('No middle characteer.') 


        
a=int(input('Enter 1st num:'))   
b=int(input('Enter 2nd num:'))   
c=int(input('Enter 3rd num:'))   
d=int(input('Enter 4rt num:'))   

if a>b:
    if a>c:
        if a>d:
            print(a,' is greatest.')
        else:
            print(d,' is greatest.')
    else:
         if c>d:
           print(c, 'is greatest.')
         else:
             print(d, 'is greatest.')
else:
    if b>c:
       
          if b>d:
            print(b, ' is greatest.') 
          else:
            print(d,' is greatest.') 
    else:
        if c>d:
            print(c, 'is greatest.')
        else:
            print(d, 'is greatest.')  


l=eval(input("Enter your list: "))
if type(l)==list:
    print('1--> Pop')
    print('2--> Append')
    print('3-->Clear')

    option=int(input('Select your option:'))
    if option==1:
        l.pop()
        print(l)
    elif option==2:
        val=input('Enter the value to pop: ')
        l.append(val)
        print(l)
    elif option==3:
        l.clear()
        print(l)
    else:
        print('invalid option.')
else:
    print('Input is not a list.') 

Q) WAP to print the given string only if the first character is vowel & last character is consonant
str=input('Enter the  string: ')
if str[0] in ('AEIOUaeiou'):
    if str[-1] not in ('AEIOUaeiou'):
        print(str)
    else:
        print('last character is not vowel.')
else:
    print('First character is not a vowel.')  
 
WAP to take input from user for payment , product and price and give discount of 10 percent.

pay_mode=input('Enter the mode of payment: ')
product=int(input('Enter the  numbewr of product: '))
price=int(input('Enter the price: '))
if pay_mode=='online':
    if product>=3:
        if price>=500:
            total=product*price
            discount=total*0.1
            final_am=total-(total*0.1)
            print('Final amount is -->', total)
            print('The discount is -->',final_am)
        else:
            print('Price is not  greater than 500.')
    else:
        print('Products are less than 3.')
else:
    print('Payment mode is not online.') 

WAP to check the mobile is available on website like amazon or flipkart.
app=input('Enter the app name: ')
category=input('Enter the category: ')
sub_cat=input('Enter the sub category: ')
if app in ('amazon,flipkart'):
    if category=='Electronics':
        if sub_cat == 'mobile':
         print('You have selected Mobile.')
        else:
           print('You have selected laptop.')
    else:
       print('You have not selected electronic category.')
else:
   print('You have selected wrong website.') """ 
      

       
    