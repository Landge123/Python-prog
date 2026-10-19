# Multilevel Inheritance:

"""
Syntax:

class grandparent:
    statement.....

class Parent(grandparent):
    statement.....

class Child(Father):
    statement.....

object=child()
"""


'''
class Grandpa:
    def villa(self):
        print("20 acers villa")

class Father(Grandpa):
    def Property(self):
        print("4bhk flat")

class Child(Father):
    def Study(self):
        print("python class.")

c=Child()
c.villa()
c.Property()
c.Study()
'''

'''
class Grandpa:
    def villa(self):
        print("20 acers villa")


class Father(Grandpa):
    
    def villa(self):
        super().villa()
        print("4bhk flat")

class Child(Father):
    
    def villa(self):
        super().villa()
        print("python class.")

c=Child()
c.villa()
'''


'''
class Grandpa:
    def __init__(self):
        print("20 acers villa")

class Father(Grandpa):
    
    def __init__(self):
        super().__init__()
        print("4bhk flat")

class Child(Father):
    
    def __init__(self):
        super().__init__()
        print("python class.")

c=Child()

'''

#Method Chaning
#Constructor Chaning



"""
class Psipder:
    def __init__(self,Total_Stud,Total_girls,Total_boys):
        self.Tot_St=Total_Stud
        self.Tot_Gr=Total_girls
        self.tot_by=Total_boys

    def Inforamtion(self):
        print(f'Total number of student in class {self.Tot_St}\n'
              f'Total numbers of girls in class {self.Tot_Gr}\n'
              f'Total numbers of boys in class {self.tot_by}')
        
        

class Subject(Psipder):
    def __init__(self,Total_Stud,Total_girls,Total_boys,Subject_name,Total_class):
        super().__init__(Total_Stud,Total_girls,Total_boys)
        self.Tot_cl=Total_class
        self.Sub=Subject_name


    def Data(self):
        print(f'Subject name is {self.Sub}\n'
              f'Total classes are {self.Tot_cl}')

class Result(Subject):
    def __init__(self, Total_Stud, Total_girls, Total_boys, Subject_name,
                  Total_class,Total_marks,Grade):
        super().__init__(Total_Stud, Total_girls, Total_boys, Subject_name,
                          Total_class)
        self.Tot_mr=Total_marks
        self.Gr=Grade

    def final(self):
        print(f'Totals marks are {self.Tot_mr}\n'
              f'Final grades are {self.Gr}')


r=Result(1200,600,600,"Python",10,98,"A")
r.Inforamtion()
r.Data()
r.final()
"""


"""
class A:
    def one(self):
        print("*")

class B:
    def one(self):
        print("$")

class C(A,B):
    def one(self):
        print("@+#")


c=C()
c.one()
"""
'''
class X:
    def __init__(self):
        print("X class data")

class Y:
    def __init__(self):
        print("Y class data")

class  Z(X,Y):
    def __init__(self):
        super().__init__()
        Y.__init__(self)
        print("X and Y class information ")

a=Z()
'''



'''
class Person:
    def Details(self,name,age,loc):
        self.name=name
        self.age=age
        self.loc=loc

    def Data(self):
        print(f'Person Name is {self.name}\n'
              f'Person location age {self.loc}\n'
              f'Current location age {self.loc}')

class Teacher:
    def Display(self,name,sub,total_hour_taken_class):
        self.name=name
        self.sub=sub
        self.time=total_hour_taken_class

    def Data(self):
        
        print(f'Teacher Name is {self.name}\n'
              f'Subject name is {self.sub}\n'
              f'Total hours of class {self.time}')

class Empoyee(Person,Teacher):
    def information(self,sal,eid,role):
        self.sal=sal
        self.eid=eid
        self.role=role


    def Data(self):
        super().Data()
        Teacher.Data(self)
        print(f'Total saraly od employee is {self.sal}\n'
              f'Employee id is {self.eid}\n'
              f'Employee role is {self.role}')


e=Empoyee()
e.Details("Omkar",23,"Pune")
e.Display("XYz","Excel",2)
e.information(30000,"E12","Developer")
e.Data()
'''

"""
class Showroom1:
    def Bike_info(self,name,type):
        self.name=name
        self.type=type

    def show(self):
        print(f"Bike name is {self.name}\n"
              f"Bike type is {self.type}")


class Car_showroom:
    def Car_info(self,name,type):
        self.name=name
        self.type=type

    def show(self):
        print(f"Car name is {self.name}\n"
              f"Car type is {self.type}")

class Both_Info(Showroom1,Car_showroom):
    def Info(self,color,model,type):
        self.color=color
        self.model=model
        self.type=type


    def show(self):
        super().show()
        Showroom1().show()
        print(f"Both car and bike color is {self.color}\n"
              f"car and bike model is {self.model}\n"
              f"Car and bike type is {self.type}")


b=Both_Info()
b.Info("Blue","BMW","Sport")
b.Bike_info("BMW","Sport")
b.Car_info("Audio","SUV")
b.show()
"""

'''

class BikeShowroom:
    def bike_info(self, name, bike_type):
        self.bike_name = name
        self.bike_type = bike_type

    def show_bike(self):
        print(f"Bike name is {self.bike_name}\n"
              f"Bike type is {self.bike_type}")


class CarShowroom:
    def car_info(self, name, car_type):
        self.car_name = name
        self.car_type = car_type

    def show_car(self):
        print(f"Car name is {self.car_name}\n"
              f"Car type is {self.car_type}")


class BothInfo(BikeShowroom, CarShowroom):
    def info(self, color, model):
        self.color = color
        self.model = model

    def show(self):
        self.show_bike()
        self.show_car()
        print(f"Both car and bike color is {self.color}\n"
              f"Car and bike model is {self.model}")


b = BothInfo()
b.info("Blue", "BMW")
b.bike_info("BMW", "Sport")
b.car_info("Audi", "SUV")
b.show()
'''


'''
class BikeShowroom:
    def __init__(self, bike_name, bike_type):
        self.bike_name = bike_name
        self.bike_type = bike_type

    def show_bike(self):
        print(f"Bike name is {self.bike_name}\n"
              f"Bike type is {self.bike_type}")


class CarShowroom:
    def __init__(self, car_name, car_type):
        self.car_name = car_name
        self.car_type = car_type

    def show_car(self):
        print(f"Car name is {self.car_name}\n"
              f"Car type is {self.car_type}")


class BothInfo(BikeShowroom, CarShowroom):
    def __init__(self, bike_name,bike_type,car_name,car_type,color,model):
        super().__init__(bike_name,bike_type)
        CarShowroom.__init__(self,car_name,car_type)
        self.color=color
        self.model=model
        print(f"Both car and bike color is {self.color}\n"
              f"car and bike model is {self.model}")


b=BothInfo("Ninja","Sport","BMW","perfomance","red","E12")
b.show_car()
b.show_bike()
'''

class Student:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(f'Student name is {self.name}')

class Gamer:
    def __init__(self,game_name,level):
         self.game_name=game_name
         self.level=level

    def show(self):
        print(f"Game name is {self.game_name}\n"
              f"Game level is {self.level}")


class Pro_gamer(Student,Gamer):
    def __init__(self, name,game_name,level,stat):
        # super().__init__()
        # super().__init__()
        Student.__init__(self,name)
        Gamer.__init__(self,game_name,level)
        self.stat=stat

    def final(self):
        print(f'Final game status is {self.stat}')


p=Pro_gamer("Omkar","BGMI",80,"Ace")
p.final()
p.display()
p.show()
        