# import sqlite3
# conn=sqlite3.connect('python.db')
# cur=conn.cursor()
# cur.execute("""CREATE TABLE stud(id int,name varchar(20),Phone int, Address varchar(20))""")
# cur.execute("""INSERT INTO stud VALUES(101,'NAMAN',9172302539,'Pune')""")
# cur.execute("""INSERT INTO stud VALUES(102,'PRAVEEN',9172302540,'Deccan')""")
# cur.execute("""INSERT INTO stud VALUES(103,'MINA'  ,9172302541,'Banner')""")
# res=cur.execute("""SELECT * FROM stud""")
# print(res.fetchall())
# conn.commit()
# conn.close()


# import mysql.connector

# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="5100"
# )
# var=conn.cursor()

# var.execute('USE DATABASE mysql.db')
# var.execute("""CREATE TABLE IF NOT EXISTS DETAILS(id int,name varchar(20))""")


# var.execute(
#     "INSERT INTO details (id, name) VALUES (%s, %s)",
#     (101, "NAMAN")
# )

# var.execute(
#     "INSERT INTO details (id, name) VALUES (%s, %s)",
#     (102, "PRAVEEN")
# )

# var.execute(
#     "INSERT INTO details (id, name) VALUES (%s, %s)",
#     (103, "MINA")
# )


# res=var.execute("""SELECT * FROM  DETAILS""")

# print(res.fetchall())
# conn.commit()
# var.close()
# conn.close()


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5100",
    database="mysql"
)

var = conn.cursor()

var.execute("""
    CREATE TABLE IF NOT EXISTS details (
        id INT,
        name VARCHAR(20)
    )
""")

var.execute(
    "INSERT INTO details (id, name) VALUES (%s, %s)",
    (101, "NAMAN")
)

var.execute(
    "INSERT INTO details (id, name) VALUES (%s, %s)",
    (102, "PRAVEEN")
)

var.execute(
    "INSERT INTO details (id, name) VALUES (%s, %s)",
    (103, "MINA")
)

var.execute("SELECT * FROM details")
print(var.fetchall())

conn.commit()
var.close()
conn.close()