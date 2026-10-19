"""
default parameter:
   def method_name(kn1=0,kn2=0,kn3=0):
       statement 

   method_name(argument)


def demo(a,b,c):
    print(a,b,c)

#demo() #TypeError: demo() missing 3 required positional arguments: 'a', 'b', and 'c'

demo(1,2,3)
"""

"""
class T:
    def spam(self,a):
        print(a)

    def spam(self,a,b):
        print(a,b)

    def spam(self,a,b,c):
        print(a,b,c)

t=T()
#t.spam(1) # TypeError: T.spam() missing 2 required positional arguments: 'b' and 'c'
#t.spam(1,2) # TypeError: T.spam() missing 1 required positional argument: 'c'
t.spam(1,2,3)
"""

"""
class T:
    def spam(self,a):
        print(a)

    def spam(self,a,b):             
        print(a,b)

    def spam(self,a=0,b=0,c=0):
        print(a,b,c)

t=T()
# t.spam()
# t.spam(1)
# t.spam(1,2)
t.spam(1,2,3)
"""

"""
#constructor overloading

class T:
    def __init__(self,a):
        print(a)

    def __init__(self,a,b):             
        print(a,b)

    def __init__(self,a=0,b=0,c=0):
        print(a,b,c)

t=T()


"""

