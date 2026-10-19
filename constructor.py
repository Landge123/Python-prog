'''
#Constructor:

i) Special members in the class.
ii) __init__ -----> in python we defined constructor
iii) In constructor object creation is mendetory.
iv) We can create n numbers of constructor in single class, but it will only access thee leatest one.
v) When every we create object it directly creates a constructor, it take self as defalut parameter
vi) Types:
1) Default constructor
2) Parameterized constructor
'''

"""
class Happy:
    def __init__(self):
        print("Welcome to all")


k=Happy()
Happy.__init__(k)  #TypeError: Happy.__init__() missing 1 required positional argument: 'self'
"""

"""
class A:
    def __init__(self):
        print(self)

a=A()
print(a)   
"""
"""
class B:
    def __init__(self):
        print("First method")

    def __init__(self):
        print("Second method")

b=B()
"""
'''
class Data:
    def __init__(self):
        print("Frist day of class")

    def show(self):
        print("class completed")

d=Data()
d.show()


#calling constructor and method through class name
Data.__init__(d)
Data.show(d)
'''


"""
class Test:
    def __init__(self):
        print("Test class")
        self.Display()
        self.Show()

    def Display(self):
        print("Display Method")

    def Show(self):
        print("Final Data")

t=Test()
"""
'''
class Room8:
    def __init__(self):
        self.name="Sachin"
        self.age=24
        self.add="Deccan"
        print(f'Student name is {self.name}\n'
              f'Student age is {self.age}\n'
              f'Current address is {self.add}')

r=Room8()
print()
r1=Room8()
print()
r2=Room8()
'''
"""
class Bank:
    def __init__(self):
        self.bankname="SBI"
        self.accnum=12345678
        self.IFSC="SBIN0079"
        self.Holder="Kiran"
        self.add="Deccan"
        print(f'Current bank name is {self.bankname}\n'
              f'Account number is {self.accnum}\n'
              f'bank IFSC code is {self.IFSC}\n'
              f'Holder name is {self.Holder}\n'
              f'Holder address is {self.add}')

b=Bank()
print()
b1=Bank()
print()
b2=Bank()
print("only instance varaible data")
print(b.bankname)
print(b.accnum)
print(b.IFSC)
print(b.Holder)
print(b.add)

"""

"""
class School:
    def __init__(self):
        self.Grade="A"
        self.Marks=75
        self.Total_marks=600

    def Student_data(self):
        print(f'Student subject grade is {self.Grade}\n'
              f'Student marks are {self.Marks}\n'
              f'Total marks is {self.Total_marks}')
        

s=School()
s.Student_data()
"""

# Parameterized Constructor:
'''
class Class_name:
    def __init__(self,value1,value2,........):
        self.new_var=value1

object=Class_name()         
'''

"""
class SBI:
    def __init__(self,name,bal,accnum):
        self.name=name
        self.bal=bal
        self.accnum=accnum
        print(f'Holder name is {self.name}\n'
              f'Total balance is {self.bal}\n'
              f'account number is {self.accnum}')

s=SBI("RAvi",30000,1234765434)
print()
s1=SBI("Omkar",13000,654987434)
print()
s2=SBI("Pravin",34000,98765467)
print()
"""

"""
class SBI:
    def __init__(self,name,bal,accnum):
        self.name=name
        self.bal=bal
        self.accnum=accnum

    def Holder_information(self):
        print(f'Holder name is {self.name}\n'
              f'Total balance is {self.bal}\n'
              f'account number is {self.accnum}')

s1=SBI("Omkar",13000,654987434)
s1.Holder_information()
print()
s2=SBI("Pravin",354000,8345677434)
s2.Holder_information()
"""

# Instance varaible modification
"""
b.Deposit(5000) 
b.Withdraw(2000)
class Bank:
    def __init__(self):
        self.bal=0.0

    def Deposit(self,amount):
        print(f'Before deposit total amount is {self.bal}\n')

        self.bal+=amount
        print(f'After deposit total amount is {self.bal}')

    def Withdraw(self,amount):
        self.bal-=amount
        print(f'After widraw total amount {self.bal}')

b=Bank()
'''
#Instance varaible modification by using object
b.bal=1000
# print(b.bal)
b.Deposit(5000)
b.Withdraw(2000)
'''

#Instance varaible modification by using classname
Bank.bal=5000    #due to instance method/varaible modification does not work with the help of class
print(b.bal)   #5000
"""

"""
class Car:
    def __init__(self,name,price,color,*args):
        self.name=name
        self.price=price
        self.color=color
        self.a=args


        print(f'car name is {self.name}\n'
              f'car price is {self.price}\n'
              f'car color is {self.color}\n'
              f'Extra inormation {self.a}')

c=Car("BMW",10000000,"Gray","Show","pune")       

#c=Car("BMW",10000000,"Gray",showroom="Pune") #TypeError: Car.__init__() got an unexpected keyword argument 'showroom'
"""

