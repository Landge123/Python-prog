#Inheritance: Is a relationship
#Accuring the properties from one class to another class

'''
#Types of inheritance
a) Single Level
b) Multi Level
c) Multiple
d) Herchical
e) Hybrid
'''

"""
# a) Single Level Inheritance:
i) Their will be only two classes 
ii) Any changes/modififction in parent class will after the child class
iii) Changes in child class will not affect the parent class.                                                                                                                     

                     Parent Class
              (super class, base class)
                         |
                         |
                         |
                     Child class
               (sub class, derived class)

"""
'''
#iv) Syntax:

class Parent:
    statement

class Child(Parent):
    statement

Object=child()    
'''

#ex:
"""
class Parent:
    def villa(self):
        print("Dad's villa")

class Child(Parent):
    def Bike(self):
        print("Dad's Gift")

c=Child()
c.villa()
c.Bike()
 """
'''
class Student:
    sub="python"
    def study(self): 
        print("Mock completed")

class Teacher(Student):
    Rating="*"
    def sub_data(self):
        print("still pending")

t=Teacher()
# print(dir(Student))  
# print(dir(Teacher()))
# t.study()
# t.sub_data()
print(t.study)
print(t.sub_data)
'''

#ways to access parent class data in to  child class
#1) super: suoer.method_name()


'''
class A:
    def show(self):
        print('First class')

class B(A):
    def show(self):
        super().show()
        print('Second class')

b=B()
b.show()
'''

#2) with the help of class name
# syntax:
# 
"""
class A:
    def show(self):
        print('First class')

class B(A):
    def show(self):
        A.show(self)
        print('Second class')

b=B()
b.show()
"""
'''
class A:
    def __init__(self):
        print("First class")

class B(A):
    def __init__(self):
        A.__init__(self)
        print("Second class")

b=B()'''

'''
class A:
    def __init__(self):
        print("First class")

class B(A):
    def __init__(self):
        super().__init__()
        print("Second class")

b=B()
'''
'''
class Employee:
    def Data(self,name,eid):
        self.name=name
        self.eid=eid

        print(f'Empoyee name is {self.name}\n'
              f'Employee id is {self.eid}')

class Information(Employee):

    def Role_Info(self,yoe,sal,role):
        self.yoe=yoe
        self.sal=sal
        self.role=role
        print(f'Year of experence {self.yoe}\n'
              f'Employee salary is {self.sal}\n'
              f'Employee role is {self.role}')

# e=Employee()   
i=Information()
i.Data("Omkar","EI123")
i.Role_Info(4,100000,"Developer")
'''
"""
class Bank:
    def __init__(self,Branch,Loc,total_emp):
        self.Branch=Branch
        self.Loc=Loc
        self.total_emp=total_emp

        print(f'Branch is {self.Branch}\n'
              f'Bank location is {self.Loc}\n'
              f'Total number of emp in bank are {self.total_emp}')

class Account_Info(Bank):
    def __init__(self, Holder_name, Acc_no, Bal):
        super().__init__("Deccan","Pune",35)
        #Bank.__init__(self,"Deccan","Pune",35)
        self.Holder_name=Holder_name
        self.Acc_no=Acc_no
        self.Bal=Bal

        print(f'Acccount holder name is {self.Holder_name}\n'
              f'Account number is {self.Acc_no}\n'
              f'Account balance is {self.Bal}')

        
# b=Bank("ICICI","Deccan",35)
ai=Account_Info("Omkar","An0123",2500)

"""

"""
class Bank:
    def morning(self,Branch,Loc,total_emp):
        self.Branch=Branch
        self.Loc=Loc
        self.total_emp=total_emp

        print(f'Branch is {self.Branch}\n'
              f'Bank location is {self.Loc}\n'
              f'Total number of emp in bank are {self.total_emp}')

class Account_Info(Bank):
    def morning(self, Holder_name, Acc_no, Bal):
        # super().morning("Deccan","Pune",45)
        Bank().morning("Deccan","Pune",45)
        self.Holder_name=Holder_name
        self.Acc_no=Acc_no
        self.Bal=Bal

        print(f'Acccount holder name is {self.Holder_name}\n'
              f'Account number is {self.Acc_no}\n'
              f'Account balance is {self.Bal}')

    
ai=Account_Info()
ai.morning("Omkar",439234567,12234)

"""


'''
class Product:
    def __init__(self,Productname,Brandname,Price):
        self.PName=Productname
        self.BName=Brandname
        self.Price=Price

    def Data(self):
        print(f'Product Name is {self.PName}\n'
              f'Brand name is {self.BName}\n'
              f'Price of product is {self.Price}')

class Product_data(Product):
    def __init__(self, Productname, Brandname, Price,Total_product,Location):
        super().__init__(Productname,Brandname,Price)
        self.TotalP=Total_product
        self.Loc=Location

    def Data(self):
        super().Data()
        print(f'Total number of products are {self.TotalP}\n'
              f'The location is {self.Loc}')


e=Product_data("Laptop","HP",45000,5,"Pune")
e.Data()
'''

class Hospital:
    def __init__(self,Hname,Dname,Pname):
        self.Hname=Hname
        self.Dname=Dname
        self.Pname=Pname

    def Hos_Data(self):
        print(f'Hospital name is {self.Hname}\n'
              f'Doctor name is {self.Dname}\n'
              f'Patitent name is {self.Pname}')

class Hospital_bill(Hospital):
    def __init__(self, Hname, Dname, Pname,Icu_bill,Normal_bill,Total_bill):
        super().__init__(Hname, Dname, Pname)
        
        self.Icu_bill=Icu_bill
        self.Normal_bill=Normal_bill
        self.Total_bill=Total_bill

    def Hos_Data(self):
        super().Hos_Data()
        print(f'ICU bad bill is {self.Icu_bill}\n'
              f'Noraml bed bill is {self.Normal_bill}\n'
              f'Total bill is {self.Total_bill}')

h=Hospital_bill("Sanjivani","Ravi","Omkar",45000,20000,65000)
h.Hos_Data()
        



