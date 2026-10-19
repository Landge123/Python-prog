'''
 Employee:
    Name="ABC"
    age=23
    def Information(self):
        print(f'My employee name is {Name}')
        print(f'Employee current age is {age}')

e=Employee()
'''

#way 1 
#how to access class varaible into the instance method
#By using  object -----> self
'''
class Employee:
    Name="ABC"
    age=23
    def Information(self):
        print(f'My employee name is {self.Name}')
        print(f'Employee current age is {self.age}')

e=Employee()
e.Information()
'''

#(Not mandetory)
class Employee:
    Name="ABC"
    age=23
    def Information(self):
        print(f'My employee name is {e.Name}')
        print(f'Employee current age is {e.age}')

e=Employee()
e.Information()

#way 2
#how to access class varaible into the instance method
#By using  Classname -----> Employee

'''
class Employee:
    Name="ABC"
    age=23
    def Information(self):
        print(f'My employee name is {Employee.Name}')
        print(f'Employee current age is {Employee.age}')

e=Employee()
e.Information()
'''

'''
class Amazon:
    product_name="Iphone"
    color="white" 
    total_product=3
    add="Pune"

    def Product_Info(self):
        print(f'My product name is {self.product_name}\n'
              f'total product is {self.total_product}\n'
              f'Product color is {self.color}')

    def Address(self):
        print(f'Current address is {self.add}')

a=Amazon()
a.Product_Info()
print()
a.Address()
'''

#Class variable modification using address 

"""
class Amazon:
    product_name="Iphone"
    color="white" 
    total_product=3
    add="Pune"

    def Product_Info(self):
        print(f'My product name is {self.product_name}\n'
              f'total product is {self.total_product}\n'
              f'Product color is {self.color}')

    def Address(self):
        print(f'Current address is {self.add}')

a=Amazon()
a.total_product=30 #object.variable_name=value
a.product_name="laptop"
a.add="Deccan"
a.Product_Info()
print()
a.Address()
"""

#Class variable modification using class_name

class Amazon:
    product_name="Iphone"
    color="white" 
    total_product=3
    add="Pune"

    def Product_Info(self):
        print(f'My product name is {self.product_name}\n'
              f'total product is {self.total_product}\n'
              f'Product color is {self.color}')

    def Address(self):
        print(f'Current address is {self.add}')

a=Amazon()
Amazon.product_name="Mobile" #class_name.variable name=new_value
Amazon.total_product=300
Amazon.color="Black"
a.Product_Info()
print()
a.Address()