#Encapsulation
'''
1) The idea of encapsulation is to bind the data members and methods into a single unit.
2) Helps in better maintainability, readability and usability as we do not need to explicitly 
pass data members to member methods.
3) Helps maintain data integrity by allowing validation and control over the values assigned to variables.
4) It helps in achieving abstraction. 
5) A class can hide the implementation part and discloses only the functionalities required by other 
classes which allows later changes to representations or implementations without impacting the codes that uses this class.

'''
'''
1) Public Access Specifier:

- Before the varaible or before the method we didn't menyion any underscore that type
of varaible/method we can call it as a public access specifiers.
- Public members are variables or methods that can be accessed from anywhere inside the class, 
outside the class or from other modules. By default, all members in Python are public. 
They are defined without any underscore prefix (e.g., self.name).


class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible


'''
'''
2) Protected Access Specifier(semi-public/private):

- Protected members are variables or methods that are intended to be accessed only within the class 
and its subclasses. They are not strictly private but should be treated as internal. In Python, 
protected members are defined with a single underscore prefix (e.g., self._name).

-EX:
class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass


'''

'''
3) Private Access Specifier:
- Private members are variables or methods that cannot be accessed directly from outside the class. 
They are used to restrict access and protect internal data. In Python, private members are defined 
with a double underscore prefix (e.g., self.__salary).

- Python uses name mangling, where the interpreter internally renames the variable (for eg, __salary 
becomes _ClassName__salary). This discourages direct access from outside the class, although it does 
not create strict privacy like other languages.

EX:

class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly


'''

# _______________________________EXAMPLES_____________________________#


"""
class Student:
    fees=1000
    def data(self):
        print(f'Total student fees are {self.fees}')

s=Student()
s.data()
"""

'''
class Student:
    def __init__(self,name,fees):
        self.name=name
        self.fees=fees

        print(f'Student name is {self.name}\n'
            f'Total student fees are {self.fees}')

s=Student("Omkar",1000)
'''
'''
class Operation:
    _name="ABC"
    def _Demo(self):
        print(f'Student name is {self._name}')

o=Operation()
print(o._name)  # no need to call outside according to the rules of pepet
o._Demo()
'''
'''
class Bank:
    _pin=1234

    def Pin(self):
        print(f'Bank pin code information is {self._pin}')

    def _Modification(self,New_pin):
        self._pin=New_pin
        print(f'New modified pin number {self._pin}')


b=Bank()
# b.Pin()
# b._Modification(1000)


#before modification
print(b._pin)
#after modification
b._pin=4321
print(b._pin)
'''

'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getter(self):
        return self.name, self.age

    def setter(self,name,age):
        self.name=name
        self.age=age


s=Student("Omkar",23)
#Before modiciation
print(s.getter())
#Aftermodification
print(s.setter(name="Pravin",age=27))
print(s.getter())
'''
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self._age=age

    def Getter(self,name,age):
        print(self.name)
        print(self._age)

    def Setter(self,name,age):
        self.name=name
        self._age=age

    def Deleter(self,name,age):
        del self.name
        del self._age


s=Student("OMkar",23) 
# s.Getter()
s.Setter("Pravin",27)
s.Getter() 
s.Deleter()'''


"""
class Amazon:
    def __init__(self,color,add):
        self.col=color
        self._ad=add

    def Getter(self):
        return(getattr(self,"col","Color data deleted"),
               getattr(self,"_ad","Address data is deleted"))

    def Setter(self,color,add):
        self.col=color
        self._ad=add

    def Deleter(self):
        del self.col


a=Amazon("Red","Pune")
print(a.Getter())
a.Setter("Blue","Mumbai")
print(a.Getter())
a.Deleter()
print(a.Getter())
"""


#Private access specifier
'''
class Data:
    __pin=1111
    def show(self):
        print(f'Person atm pin number is {self.__pin}')

d=Data()
d.show()
# print(Data.__dict__)
'''


'''
class Test:
    __a=100
    def display(self):
        print(f'Varaible data is {self.__a}')

t=Test()
#accessing private varaible outside by using object
print(t._Test__a)

#Accessing private variable outside by using classname
print(Test._Test__a)
'''
'''
class Bank:
    def __init__(self,TE,Mname,Working_hours,dept):
        self.TE=TE
        self.Mname=Mname
        self._Whours=Working_hours
        self.__dept=dept


    def Getter(self):
        return(getattr(self,"TE","empolyee_data"),
               getattr(self,"Mname","name_data"),
               getattr(self,"_Whours","Working_data"),
               getattr(self,"__Bank__dept","dept_data"))

    def Setter(self,TE,Mname,Working_hours,dept):
        self.TE=TE
        self.Mname=Mname
        self._Whours=Working_hours
        self.__dept=dept

    def Deletter(self):
        del self.Mname
        del self.__dept

k=Bank("Omkar","Python",9,"Development")
print(k.Getter())
k.Deletter()
print(k.Getter())
'''


"""
class Student:
    def __init__(self,name):
        self.name=name

    @property     #------------> Getter
    def data(self):
            return(setattr(self,'name','name_deleted'))

    @data.setter
    def data(self,name):
         self.name=name

    @data.delattr
    def data(self):
         del self.name

s=Student()
print(s.data)
s.data

s=Student('xyz')
print(s.data)
s.data='ABC'
print(s.data)
del s.data
print(s.data)
"""      
