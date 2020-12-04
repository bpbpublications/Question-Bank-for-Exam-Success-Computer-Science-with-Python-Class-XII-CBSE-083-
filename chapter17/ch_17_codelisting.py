Very Short Questions and Answers
# 15. How to use keyword arguments with the function connect()?
# Ans. The following code demonstrates the use of keyword arguments with the execute function:

import mysql.connector as connection
dbconfig = {
'user': 'root',
'password': '',
'database': 'pythondb',
'host': '127.0.0.1',
'raise_on_warnings': True
}
conn = connection.connect(**dbconfig)
if(conn.is_connected()==True):
    print("Successfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database")
conn.close()
Output:
Successfully connected to Mysql...!

# 17. Write a program that retrieves the version of MySQL.
# Ans. 
import mysql.connector as con
mycon= con.connect(host="localhost",
user="root",
passwd="",
database='pythondb')
if(mycon.is_connected()==True):
    print("Successfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database")
cursor=mycon.cursor()
cursor.execute("select version()")
data= cursor.fetchone()
if data:
    print('version retrieved:', data)
else:
    print('version not retrieved')
cursor.close()

19. Write a program that delete row(s) from a table.
Ans. 
import mysql.connector as con
mycon=con.connect(host="localhost",\
user="root",\
password="",\
database='pythondb')
if(mycon.is_connected()==True):
    print("successfully connected to Mysql...!")
else:
    print("There is a problem connecting to database")
cursor=mycon.cursor()
query="delete from users where user_id > 10"
cursor.execute(query)
print("Affetced rows: "+ str(cursor.rowcount))
mycon.commit()
cursor.close()

21. Write a program that update row(s) in the table.
Ans. import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="",database='pythondb')
if(mycon.is_connected()==True):
print("successfully connected to Mysql...!")
else:
print("There is a problem in connecting to database")
cursor=mycon.cursor()
query="update users set First_Name='Rajesh' where user_id= 2"
cursor.execute(query)
print("Affetced rows: "+ str(cursor.rowcount))
mycon.commit()
cursor.close()
mycon.close()

Short Questions and Answers
5. Write a Python program that iterates a result set.
Ans. 
import mysql.connector
conn = mysql.connector.connect(user='root', \
password='',\
host='127.0.0.1',\
database='pythondb1')
# Using cursor as an iterator
cursor.execute("SELECT * from books")
for result_row in cursor:
    print(result_row)
    
# Using fetchone with a while loop
cursor.execute("SELECT * from books")
    #Fetch the row first
result_row = cursor.fetchone()

while result_row is not None:
    print(result_row)
    result_row = cursor.fetchone()
    
conn.close()

6. Write a program to insert a record(s) in the below table.

+-----------+------------+----+----+--------+---------+
Field       |Type        |Null|Key |Default |Extra    |
+-----------+------------+----+----+--------+---------+
User_ID     |  int(11)   | No |PRI |NULL    |         |
+-----------+------------+----+----+--------+---------+
First_Name  | varchar(30)| No |    |        |         |
+-----------+------------+----+----+--------+---------+
Last_Name   | varchar(30)| No |    |        |         |
+-----------+------------+----+----+--------+---------+
Address     | varchar(70)| No |    |        |         |
+-----------+------------+----+----+--------+---------+
phone       | varchar(10)| No |    |        |         |
+-----------+------------+----+----+--------+---------+
email       | varchar(10)| No |    |NULL    |         |
+-----------+------------+----+----+--------+---------+

Ans. 
import mysql.connector as con
mycon=con.connect(host="localhost",\
user="root",\passwd="",
\database='pythondb')
if(mycon.is_connected()==True):
    print("successfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database")
cursor=mycon.cursor()
query="INSERT INTO users(First_Name,Last_Name,Address,PhoneNo,Email)\
VALUES('{}','{}','{}','{}','{}')".format('Satyam','Kumar',\
'23 E-Pkt Sadar bazar','7676767676','sk@test.com')
cursor.execute(query)
print("Affetced rows: "+ str(cursor.rowcount))
cursor.close()

# 7. Write a program to count the number of rows in a table.
# Ans. Method 1: Retrieve the result using query:
select count(*) from users;
import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="",database='pythondb')
if(mycon.is_connected()==True):
    print("successfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database")
cursor=mycon.cursor()
#Retrieves row count from query
query="SELECT count(*) from users"
cursor.execute(query)
row=cursor.fetchone()
print("The number of rows " + str(list(row)) )
cursor.close()
mycon.close()

import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="",database='pythondb')
if(mycon.is_connected()==True):
    print("succesfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database ")
cursor = mycon.cursor()
query="SELECT * from users"
cursor.execute(query)

row=cursor.fetchone()
while row is not None:
    row=cursor.fetchone()
    
print("The number of rows", end='')
print(cursor.rowcount)
cursor.close()
mycon.close()

8. Write a program to insert multiple rows in a table using a single query.
Ans. import mysql.connector as con
mycon=con.connect(host="localhost",
user="root",
passwd="",
database='pythondb')
if(mycon.is_connected()==True):
    print("successfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database")
cursor = mycon.cursor()
query="INSERT INTO users(First_Name,Last_Name,Address,PhoneNo,Email)\
VALUES \
('Narayan','Mishra','Shivaji Nagar', '9807654321', 'narayan@test.com'),\
('Prateek','Sharma','Bapu Nagar','9999765432','prateek@test.com'),\
('Dinesh','vijaykumar','Shastri Nagar','9899654321','dinesh@test.com'),\
('Manish','Verma','9807654321','T Nagar','narayan@test.com');"
cursor.execute(query)
mycon.commit()
print("Affected rows: "+str(cursor.rowcount))
cursor.close()
mycon.close()

# 9. Write a program that fetches (n) rows from the database and displays them one by one.
# Ans. 
import mysql.connector as con
mycon=con.connect(host="localhost",\
user="root",\
passwd="",
database='pythondb')
if(mycon.is_connected()==True):
    print("successfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database")
cursor=mycon.cursor()
query="SELECT * from users"
cursor.execute(query)
data=cursor.fetchmany(4)

for row in data:
    print(row)
    
mycon.close()

# 10. Write a program that fetches all the rows from a table in a database and displays them one by one.
# Ans. 
import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="",database='pythondb')
if(mycon.is_connected()==True):
    print("successfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database")
cursor=mycon.cursor()
query="SELECT * from users"
cursor.execute(query)
data=cursor.fetchall()
for row in data:
    print(row)

mycon.close()


# 11. Write a program that demonstrates the use of commit and rollback.
# Ans. 
import mysql.connector as connection
# Open database connection
dbconn = mysql.connector.connect(user='root', \
password='',\
host='localhost',\
database='pythondb')
# Create a cursor using cursor() method
cursor = dbconn.cursor()
#The SQL query to INSERT records in a table.
sql = "query=SELECT * FROM USERS "
try:
    # Execute the SQL command using execute
    cursor.execute(sql)
    # Commit the changes in database
    dbconn.commit()
except:
    # Rollback in case of an error
    dbconn.rollback()
# disconnect from server
dbconn.close()
mycon.close()

14. Write a program to connect to a MySQL database and fetch all records where the grade is ‘A’ from the students table.
Ans. 
import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="",database='pythondb')
if(mycon.is_connected()==True):
    print("successfully connected to Mysql...!")
else:
    print("There is a problem in connecting to database")
cursor=mycon.cursor()
query="SELECT * from students where grade='A' "
cursor.execute(query)
data=cursor.fetchall()
for row in data:
    print(row)
    
mycon.commit()

15. Write a function that updates row(s) using a parameterization query.
Ans. A parameterized query allows providing parameters that can be inserted into the query at the time of execution. The following example demonstrates the use of parameterizing a query:
import mysql.connector as con
def updatephone(id,PhoneNo):
    # Open database connection
    dbconn = con.connect(user='root',password='',host='localhost',database='pythondb')
    # Create a cursor using cursor() method
    cursor = dbconn.cursor()
    # SQL query to INSERT a records in a table.
    sql = 'update users set phoneno= %s where user_id = %s'
    dtuple = (PhoneNo,id)
    try:
        # Execute the SQL command using execute
        cursor.execute(sql,dtuple)
        print('Affected rows: '+str(cursor.rowcount))
        # Commit the changes in database
        dbconn.commit()
    except:
        # Rollback in case of an error
        dbconn.rollback()
        
    # disconnect from server
    dbconn.close()
    updatephone(1,'1234567891')
    cursor.close()
    mycon.close()
