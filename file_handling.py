import os
print(os.getcwd())
os.chdir(r"C:\Users\landg\OneDrive\Desktop - Copy\Desktop\unique\PythonClass")
#os.chdir("C:\\Users\\landg\\Desktop\\unique")
print()

# os.makedir("Second")

#os.makedirs("A\B\C\D\E")

# print(os.listdir())  

# os.rename("Firstclass","PythonClass")

#os.popen(r"C:\Users\landg\OneDrive\Desktop - Copy\Desktop\unique\omkar.txt.txt")

# os.rmdir("First")
# os.remove("Omkar.txt")
#file=open("martker.txt","x")

# file=open("martker.txt")  #---default it will be in reading mode.
#os.popen("martker.txt")


# print(file.name)
# print(file.mode)


# file=open("martker.txt","w")
# print(file.mode)
# print(file.readable())
# print(file.writable())
# file.close()
# print(file.closed)

# file=open("martker.txt","r") 

# os.popen("martker.txt")
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# print(file.read(3))

# file1=open("Pen.txt","w")


# file1.write("Hello guys welcome to the class")
# file1.write("Python program")

# file1.writelines(["Python\n","Java\n","SQL\n","SQL\n","PowerBI\n"])


# os.popen("Pen.txt") 


# file2=open("walmart.txt","a")
# file2.write("Evening")
# file2.write("Good luck")
# file2.write("Java\n")
# file2.write("sql\n")
# file2.write("PowerBI\n")
# file2.write("ML\n")

# os.popen("walmart.txt")

# file=open("martker.txt","r") 
# print(file.read())
# print(file.tell())
# print(file.seek(4))
# print(file.tell())
# print(file.readline())
# print(file.seek(1))


# file=open("martker.txt","r+") 
# print(file.read())
# file.write("***************")
# print(file.read())
# # os.popen("martker.txt")

# print(file.tell())
# print(file.seek(0))


# file=open("martker.txt","w+") 
# file.write("@@@@@@@@@@@@@@@@@@@@")


# # print(file.tell())
# print(file.seek(0))
# print(file.read())

file=open("martker.txt","a+") 
file.write("\n%%%%%%%%%%%%%%%%%%")


# print(file.tell())
print(file.seek(0))
print(file.read())