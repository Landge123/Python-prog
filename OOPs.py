#how to create empty class
#syntax: class Class_Name:
'''
class Evening:

e=Evening()
e1=Evening
print(e)
print(e1)
'''
"""
Class:
1) variable        
a) Class varaible: Any varabile which is present inside a class.
b) Instance varabile
c) Local varabile
2) Method
3) Constructor"""

"""class Student:
    Name="Rohit"
    R_NO=32
    Branch="Cs"
s=Student()"""
#print(Name)  #NameError: name 'Name' is not defined.

'''
Accessing class varaible outside by using className
'''
"""print(Student.Name)
print(Student.R_NO)
pyint(s.Name)
print(Student.Branch)

print(f'Student name is {Student.Name}')
print(f'Student roll no is {Student.R_NO}')
print(f'Student branch is {Student.Branch}')u
print()
print(f'Student name is {s.Name}')
print(f'Student roll no is {s.R_NO}')
print(f'Student branch is {s.Branch}')
"""
"""
print(Student.__dict__) # data will be printed in dict format
print()
print(s.__dict__)  # Empty dict will be printed
"""

"""
class Hii:
    x=100
    y=200
h=Hii()
h1=Hii()
Hii()
"""
"""
print(id(Hii))
print(id(h))
print(id(h1))
print()
print(h.x)
print(Hii.x)
print(Hii.y)
print(id(Hii.x))
print(id(Hii.y))"""

'''
If we done any modifiction in main class it will affected for both object
syntax: Class_Name.Var_Name=Value
'''
'''class Hii:
    x=100
    y=200
h=Hii()
h1=Hii()

Hii.x=300
print(h.x)
print("Before modifiction")
print(Hii.x)
print(h.x)
print(h1.x)
print()
print("After modifiction")
Hii.x="SQL"
print(Hii.x)
print(h.x)
print(h1.x)
'''







"""print("Before modifiction")
print(Hii.x)
print(h.x)
print(h1.x)

print("After modifiction")

Hii.x=700

print(Hii.x)


print(h.x)
print(h1.x)"""

'''IF we done any modification in object, it will not affect the main class or other object, 
it is limited for particular object only. '''

"""print("Before modifiction")
print(Hii.x)
print(h.x)
print(h1.x)
print()
print("After modifiction")

h.x="Python"
print(h.x)     #Python
print(h1.x)    #100
print(Hii.x)   #100"""

'''
Again if we done any modification in main class it will affected for main class it will affect 
for other object but it will won't affect for previous modiification object because when we do  
separate modication it will create seperate memory means we loss the connection.
syntax:-----> ClassName.Var_name=value
'''
"""print("Before modifiction")
print(Hii.x)
print(h.x)
print(h1.x)
print()
print("After modifiction")
"""
'''Hii.x="SQL"
print(Hii.x)
print(h.x)
print(h1.x)'''

# Docstring: It is description of the class.

'''
class Employee:
    name="ABC"
    EID="A123"
    Sal=45000
    role="Analysis"

e=Employee()
# print(Employee.__doc__)
help(Employee)
'''
# Method: A function inside a class.

#Function: A block of code it will execute when we call the function name.

'''
Class A:   ---------------> Class creation
  def spam(self):

a=A()     -----------------> Objection creration
'''
'''
# Types of methods:
1) Instant method
2) Class method
3) Static method
'''


# Instance Method: Instance method is nothing but an object.

'''
1) It only works for a object data
2) A method it will accept first argument of an object address then we can call it 
as an instance method.
3) syntax:
class Class_Name:   -------------> class creation

  def method(self):  ------------> instance method
  statment

object=Class_Name()  ------------>Object creation
'''
#Two ways to access
'''
1) By using object
syntax:
object.method_name()

2) By using class
syntax:
Class_Name.method_name(object)

#Note: Object calling is mendetory then class.
'''
#Example:

"""
class Evening:
    def demo(self):
        print("Welcome to all")

e=Evening()
#by calling object
#e.demo()  #object.method.name()

#by calling class name
#Evening.demo() # TypeError: Evening.demo() missing 1 required positional argument: 'self'

Evening.demo(e) 

#e.demo(e) # TypeError: Evening.demo() takes 1 positional argument but 2 were given
""" 
"""
class Evening:
    def demo(self):
        print(self)

e=Evening()
print(e)  # <__main__.Evening object at 0x000001B7F017C440>
e.demo()  # <__main__.Evening object at 0x000001B7F017C440>
"""
'''
class Evening:
    def demo(x):
        print(x)

e=Evening()
print(e)  # <__main__.Evening object at 0x0000017EA71F82F0>
e.demo()  # <__main__.Evening object at 0x0000017EA71F82F0>
'''

# 2) Instance Varaible:

# syntax: self.new_var=value
"""
class Student:
    def Information(self):
        self.name="XYZ"
        self.age=21
        self.Rno=101
        self.clg="ABC"
        print(f'Student Name is {self.name}\n'
              f'Student age is {self.age}\n'
              f'Student Roll_No is {self.Rno}\n'
              f'Student college name is {self.clg}\n'

              )

s=Student()
s.Information()
s1=Student()
s1.Information()
"""
'''
class Bank:
    def AccountInfo(self,Holder_Name,Acc_No,Bank_Name,Balance,IFSC):
        self.HN=Holder_Name
        self.AN=Acc_No
        self.BN=Bank_Name
        self.BL=Balance
        self.IC=IFSC
        print(f'Account holder name is {self.HN}\n'
              f'Account number is {self.AN}\n'
              f'Bank name is {self.BN}\n'
              f'Account balance is {self.BL}\n'
              f'Account IFSC coode is {self.IC}\n'
              )

b=Bank()
b.AccountInfo("Omkar",123,"BOM",1000,"ASC12")
print()'''
# b.AccountInfo()



"""class Student:
    school = "ABC College"              # class variable

    def __init__(self, name):
        self.name = name                # instance variable


s1 = Student("Omkar")
s2 = Student("Riya")

# print(s1.school)            # ABC College
# print(s2.school)            # ABC College
# print(Student.school)       # ABC College  (same value through the class)

# print(s1.__dict__)          # {'name': 'Omkar'}  <- 'school' is not stored in the object


print(s1)


"""