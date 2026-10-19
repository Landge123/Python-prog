
"""
#Class Methods:
#- only worl for class data only

#syntax:

'''
class Class_name:
    @class metho
    def method_name(cls):     # cls alway poinnt to classname
          statement
          ......
          ......

object=Class_name()    #------optional
'''
way 1:
object.method_name()

way 2:   (optinal)
Class_name.method_name()

cls will always point to the main class

"""


"""
#instance method
#- it only for object data

#syntax:
class Class_name:
    def method_name(self):    ----|___Instance method
        statement             ----|

object=Class_name

way1 :
object.method_name()

way2 :
Class_name.method_name(object)

self is a special parameter (we can also use any character in place of self)
cls is a special parameter   (we can also use any character in place of cls)
we can use cls in the place od self


"""



'''
class Evening:
    @classmethod
    def Demo(cls):
        print("demo method")

Evening.Demo()
'''

'''class Evening:
    @classmethod
    def Demo(cls):
        print("demo method")

e=Evening()
e.Demo()
Evening.Demo()
#Evening.Demo(e) # TypeError: Evening.Demo() takes 1 positional argument but 2 were given'''

"""
class Evening:
    @classmethod
    def Demo(cls):
        print(cls)

e=Evening()
print(e)   # <__main__.Evening object at 0x000001D1B3D281A0>  -----pointing to main class object
e.Demo()   # <class '__main__.Evening'>   -----pointing to main class
"""
'''
class Evening:
    @classmethod
    def Demo(d):
        print(d)

e=Evening()

print(e)   
e.Demo()
Evening.Demo() 
'''

#1) modification using class_method

"""
class School:
    sub="SQL"
    @classmethod
    def display(cls):
        print(f'subject name is {cls.sub}')


    @classmethod
    def show(cls,new_sub):
        cls.sub=new_sub
        print(f'Modification name is {cls.sub}')

School.display()
School.show("Python")
"""
#2) Direct modification
"""
class School:
    sub="SQL"
    @classmethod
    def display(cls):
        print(f'subject name is {cls.sub}')

School.sub="Python"
School.display()
"""

#3) Modifiction using

"""
class School:
    sub="SQL"
    @classmethod
    def display(cls):
        print(f'subject name is {cls.sub}')

        @classmethod
        
"""

"""
class Election:
    date="10-09-2026"
    @classmethod
    def Area1(cls):
        print(f'Election date is {cls.date}')


Election.Area1()
#modification using classname
Election.date="15-09-2026"
Election.Area1()

"""
"""
class Joy:
    sub="SQL"
    @classmethod
    def data(cls):
        print(f'subject Name is {cls.sub}')
        cls.sub="Python"
        print(f'subject Name is {cls.sub}')

Joy.data()
"""

"""
class Amazon:
    add="Pune_office"
    @classmethod
    def off1(cls):
        print(f'address one is {cls.add}')

    @classmethod
    def off2(cls):
        print(f'address two is {cls.add}')

    @classmethod
    def off3(cls):
        print(f'address three is {cls.add}')

a=Amazon()
#calling throught object
a.off1()
a.off2()
a.off3()
print()
#calling through classname
Amazon.off1()
Amazon.off2()
Amazon.off3()
"""
"""
class Amazon:
    add="Pune_office"
    @classmethod
    def off1(cls):
        print(f'address one is {cls.add}')

    @classmethod
    def off2(cls):
        w=cls()
        w.add="deccan_office"
        print(f'address two is {w.add}')

    @classmethod
    def off3(cls):
        print(f'address three is {cls.add}')

a=Amazon()
# a.add="Deccan_office"

a.off1()
a.off2()
a.off3()
"""

"""
class Showroom:
    car_name="BMW"
    total_amount="1cr"
    color="red"

    def car_data(self):
        print(f'Car name is {self.car_name}\n'
              f'car color is {self.color}')

    @classmethod
    def car_amount(cls):
        print(f'Total car amount is {cls.total_amount}')

s=Showroom()
s.car_data()
Showroom.car_amount()
            
s=Showroom()
s.car_name="Lambo"
s.color="Black"
s.car_data="50lac

"""
                                 