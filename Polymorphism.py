"""class Info:
    def Data(self,x):
        print(x)

    def Data(self,x,y):
        print(x,y)

    def Data(self,x=0,y=0,z=0):
        print(x,y,z)

    def Data():

        

i=Info()
i.Data()

"""
class Data:
    def demo(self,**kwargs):
        print(kwargs)

d=Data()
d.demo()
d.demo(x=1)
d.demo(x=1,y="hii")
d.demo(x=1,y="hii",z=[1,2,3])
