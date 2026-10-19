#Way 2 Modifiction through object
"""
class Bank: 
    Holder="ABC"
    bal=1000

    def Data(self):
        print(f'Holder name is {self.Holder}')
        print(f'Account balance is {self.bal}')

b=Bank()
'''
#Modification through object
b.Holder="XYZ"
b.bal=2000
'''
'''
#Modification through classname
Bank.Holder="Abhi"
Bank.bal=1000
'''
b.Data()
"""

#Way 2 Modifiction through class
"""
class Bank: 
    Holder="ABC"
    bal=1000

    def Data(self):
        print(f'Holder name is {Bank.Holder}')
        print(f'Account balance is {Bank.bal}')

b=Bank()
'''
#Modification throught object
b.Holder="PQR"
b.bal=9000

'''
#
#Modification through class
Bank.Holder="JOY"
Bank.bal=5000
b.Data()
"""
'''
class Fipkart:
    total_item=12
    add="Pune"
    def Data(self):
        print(f'Total item count is {self.total_item}')
    
    def Info(self):
        print(f'Customer current address is {self.add}')

f=Fipkart()
f.Data()
f.Info()
'''

"""
class Flipkart:
    total_item=12
    add="Pune"
    def Data(self):
        print(f'Total item count is {self.total_item}')
        self.Info()
    
    def Info(self):
        print(f'Customer current address is {self.add}')

f=Flipkart()
# f.Data()
#Flipkart.Data()  # Flipkart.Data() missing 1 required positional argument: 'self'
Flipkart.Data(f)
"""

'''
class Flipkart:
    total_item=12
    add="Pune"
    def Data(self):
        print(f'Total item count is {self.total_item}')
        
    
    def Info(self):
        print(f'Customer current address is {self.add}')
        self.Data()

f=Flipkart()
# f.Info()
#Flipkart.Info() Flipkart.Info() missing 1 required positional argument: 'self'
Flipkart.Info(f)
'''
'''
class Student:
    def Info(self):
        name="Ravi"
        age=23
        sub="Python"

        print(f'Student name is {name}\n'
              f'Student age is {age}\n'
              f'Subject name is {sub}')

s=Student()
s.Info()
#print(s.name) #'Student' object has no attribute 'name'
#print(s.age)  #'Student' object has no attribute 'age'
'''
'''
class Student:
    def Info(self):
        self.name="Ravi"
        self.age=23
        self.sub="Python"

        print(f'Student name is {self.name}\n'
              f'Student age is {self.age}\n'
              f'Subject name is {self.sub}')

s=Student()
s.Info()
print(s.name)
'''
"""
class Mock:
    def study(self,name,subject,rating):
        # self.name=name
        # self.subject=subject
        # self.rating=rating

        self.n=name
        self.s=subject
        self.r=rating
        print(f'Student name is {name}\n'
              f'Subject name is {subject}\n'
              f'Mock rating is {rating}')

m=Mock()
m.study(name="Omkar",subject="python",rating="*")
print()
m.study(name="Rohit",subject="java",rating="*")
print()
m.study(name="ganesh",subject="SQL",rating="*")
print()
m.study("Krishna","PowerBI","*")
"""
