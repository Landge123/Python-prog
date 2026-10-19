
# without using file handling

"""import pickle
dumps()
new_var=pickle.dumps(iterable)

loads()
new_var=pickle.loads(previous_varible)
"""
'''
dump()-------> python_object--------->ByteStream
dumps()-------> python_object--------->ByteStream
load()-------> BytesStream----------->Python_Object
loads()-------> BytesStream----------->Python_Object 
'''
"""
1) dump()---using file handling
with open("file.extension","mode") as file_object:
     new_var=pickle.dump(iterable,file_object)

2) load()---using file handling   
with open("file.extension","mode") as file_object1:
     new_var=pickle.load(file_object1)
"""

"""import pickle

s=[100,"Python","PowerBI","Walmart"]

x=pickle.dumps(s)
print(x)

y=pickle.loads(x)
print(y)
"""

# with using file handling

import os 
import pickle
print(os.getcwd())
os.chdir(r"C:\Users\landg\OneDrive\Desktop - Copy\Desktop\unique\PythonClass")
print(os.getcwd())

#without coteext manager
"""x=open("xyz.txt","w")
x.close()
print(x.closed)
"""

#with context manager

"""with open("xyz.txt","w") as file:
    print(file.closed)
print(file.closed)
"""

#using pickle

with open("day.pkl","wb") as file:
    e=pickle.dump(["abc","Hii","hello","xzy"],file)

# os.popen("day.pkl")

print()
with open("day.pkl","rb") as file1:
    w=pickle.load(file1)
print(w)










#imp
# 1) diff seriallization and deserallization
# 2) 
