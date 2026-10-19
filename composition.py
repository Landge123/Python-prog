# Composition(Has a relationship)

'''
class Test:
    def spam(self):
        print('Spam method')

class Data:
    def demo(self):
        t=Test()
        print('Demo method')
        t.spam()

d=Data()
d.demo()

'''

'''
#()

class Company:
    def Info(self,name,sal,loc):
        self.name=name
        self.sal=sal
        self.loc=loc
        print(f'company name is {self.name}\n'
              f'Salary is {self.sal}\n'
              f'Company location is {self.loc}')


class Student:
    def Stud_data(self,Marks,Grade):
        c=Company()
        c.Info("Omkar",45000,"Pune")
        self.Marks=Marks
        self.Grade=Grade
        print(f'Student marks are {self.Marks}\n'
              f'Student grande is {self.Grade}')

s=Student()
s.Stud_data(600,"S")
'''


"""
#(USing 2 instance varaible)
class Company:
    def Info(self,name,sal,loc):
        self.name=name
        self.sal=sal
        self.loc=loc
        print(f'company name is {self.name}\n'
              f'Salary is {self.sal}\n'
              f'Company location is {self.loc}')


class Student:
    def Stud_data(self,Marks,Grade):
        self.c=Company()
        self.c.Info("Omkar",45000,"Pune")
        self.Marks=Marks
        self.Grade=Grade
        print(f'Student marks are {self.Marks}\n'
              f'Student grande is {self.Grade}')

s=Student()
s.Stud_data(600,"S")

"""

#Using methods

'''
class Hii:
    def __init__(self,name):
        self.name=name
        print(f'name is {self.name}')

class Happy:
    def __init__(self,age):
        self.age=age
        self.T=Hii("Omkar")
        print(f'Current age is {self.age}')

h=Happy(23)
'''

class Amazon:
    def __init__(self,Product,Price):

        self.p=Product
        self.Price=Price


    def Data(self):    
        print(f'Product name is {self.p}\n'
              f'Price of product is {self.Price}')

class Flipkart:
    def __init__(self,total_product,color):
        self.a=Amazon("Sumsung",50000)
        self.a.Data([])
        self.total_product=total_product
        self.color=color


    def show(self):
        print(f'Total number of product are {self.total_product}\n'
              f'Color of product is {self.color}')

f=Flipkart(30,'Sky blue')
f.show()
        
