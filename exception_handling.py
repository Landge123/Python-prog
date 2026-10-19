#Exception:
#Unwanted and unexcepted happen suddenly while execution of the program
#i) Runtime error

#Error: Before execution of the program
#i) Syntax error
#Types of error in python:
#1) Predefined error.
#2) User defined error.


#Exception handling:
# we will use try catch block while be used to handle runtime error 


"""try :
    statement (error line)
except:
    statement (Resolve block or handling block)"""


"""a=[1,2,3,4,5]
try:
    print[1]
except:
    print("error handling")"""

"""a="evening"
try:
    print("error handling")
except:
    print("error done")
"""


"""try:
    file=open("python.txt","r")
    print(file.readline())
except:
    print("File handling Done")"""

"""
#Types of exception block:
#1) Default except block 
syntax: 
try:
    statement
except:
    statement

when we don't know what kind of error it will occur that time 
we can go for the ddfault exception block

#2) Specific except block:
syntax:
try:
    statement 

except (exception name):
    statement

when we konw what kind of error it will occur that time we can go for 
spicific except block

#3) Multiple except block:
Syntax:
try:
    statement

except exception name:
    statement

except exception name:
    statement

except exception name:
    statement  

            OR

try:
   statemenet

except (exception1,exception2,exception3........):
    statement

#4) Generic except block
syntax:
try: 
    statement

except Exception as msg:
     statment
     print(MSS)

"""

'''try:
    file=open("python.txt","r")
    print(file.readline())
except TypeError:
    print("Block 1")

except ZeroDivisionError:
    print("Block2")

except PermissionError:
    print("Block3")

except ValueError:
    print("Block4")
'''

'''try:
    file=open("python.txt","r")
    print(file.readline())
except (ValueError,ZeroDivisionError,TypeError):
    print("error Done")'''