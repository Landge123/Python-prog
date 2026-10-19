# import threading
'''
print(threading.current_thread().name)     #---updated method should not use capital one.
print(threading.current_thread().ident)
print(threading.current_thread().is_alive())
'''

'''
print(threading.current_thread().name)
threading.current_thread().name="Python"
print(threading.current_thread().name)
'''

'''
#(older version so not to use)
print(threading.current_thread().getName)
threading.current_thread().setName="java"
print(threading.current_thread().getName)
'''

"""
#ways to create new thread

1) without using any class
2) with extending threat class
3) witthout extending threat class
"""

"""
import threading
from threading import *
def show():
    for i in range(5):
        print("Child threat class ")
x=Thread(target=show)
x.start()
x.join()
for i in range(5):
    print("main thread")
"""


"""
import time
import threading
from threading import *
def Display():
    print(current_thread().name," started")
    time.sleep(3)
    print(current_thread().name," Stoped")
print("Total active thread is",active_count())


t1=Thread(target=Display,name=" Child1")
t2=Thread(target=Display,name=" Child2")
t3=Thread(target=Display,name="    Child3")


t1.start()
t2.start()
t3.start()


print("Total active threads is: ",active_count())
print()
time.sleep(3)
print("Total active threads is: ",active_count())
"""

"""
import time
import threading
from threading import *
def Display():
    print(current_thread().name," started")
    time.sleep(3)
    print(current_thread().name," Stoped")
print("Total active thread is",active_count())

   
t1=Thread(target=Display,name=" Child1")
t2=Thread(target=Display,name=" Child2")
t3=Thread(target=Display,name="    Child3")


t1.start()
t2.start()
t3.start()


print("Total active threads is: ",active_count())
print()
time.sleep(3)
print("Total active threads is: ",active_count())
"""

"""
import thread
from threading import *

def job():
    print("Job Process is Loading")

t=Thread(target=job)
t.setDaemon(True)
print(t.daemon)
"""

"""
from threading import*
import time
l=Lock()

def Greet(name):
    l.acquire()
    for i in range(2):
        
        print("Good Morning ",name)
        time.sleep(2)
        print(name)

t=Thread(target=Greet,args=("Virat"))
t1=Thread(target=Greet,args=("Yuvraj"))
t2=Thread(target=Greet,args=("Dhoni"))

t.start()
t1.start()
t2.start()
"""

"""
from threading import*

l=Lock()
l.acquire()
print('Thread working')
l.acquire()
print('Thread 2 also working')
l.release()
"""

"""
from threading import*

l=RLock()
l.acquire()
print('Thread working')
l.acquire()
print('Thread 2 also working')
l.release()

"""
'''
from threading import*

def Greet(name):

  '''  
from threading import*
import time
s=Semaphore()
def Greet(name):
    s.acquire()
    for i in range(4):

        print("Good morning",end=" ")
        time.sleep(2)
        print(name)
        s.release()

t1=Thread(target=Greet,args=("Virat",))
t2=Thread(target=Greet,args=("Shreyas",))
t3=Thread(target=Greet,args=("Hardik",))
t4=Thread(target=Greet,args=("Sachin",))
t5=Thread(target=Greet,args=("Rohit",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

