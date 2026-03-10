import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # agar password set nahi hai
    database="python_db"
)

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS class_info (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# cursor.execute("SELECT * FROM users")
# cursor.execute("INSERT INTO users VALUES  (3, 'Alice', 30, 999)")
# cursor.execute("UPDATE users set name='raghav' WHERE id=3 ")
# cursor.execute("DELETE FROM users WHERE name='Akash'")
conn.commit()

# for row in cursor.fetchall():
#     print(row)

conn.close()



############################# DB code ###################################
# import sqlite3
# # Connect to the database (or create it if it doesn't exist)
# conn = sqlite3.connect('demodb.sqlite3')
# # Create a cursor object to interact with the database
# cursor = conn.cursor()
# # Create a new table called 'users'
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# # Insert a new user into the table
# cursor.execute("INSERT INTO users VALUES  (2, 'Alice', 30)")
# # Commit the changes to the database
# conn.commit()
# # Query the database to retrieve all users
# #cursor.execute("SELECT * FROM users")
# # Fetch all results from the executed query
# #users = cursor.fetchall()
# # Print the retrieved users
# #for user in users:
# #print(user)
# # Close the connection to the database
# conn.close()
# ---------------------------------------------------------------------------
# OperationalError                          Traceback (most recent call last)
# Cell In[6], line 9
#       7 cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
#       8 # Insert a new user into the table
# ----> 9 cursor.execute("INSERT INTO users VALUES  (2, 'Alice', 30)")
#      10 # Commit the changes to the database
#      11 conn.commit()

# OperationalError: database is locked
# import sqlite3
# conn=sqlite3.connect('testdb.sqlite3')
# cur=conn.cursor()
# qry='''
# CREATE TABLE Employee (
# EmpID INTEGER PRIMARY KEY AUTOINCREMENT,
# FIRST_NAME TEXT (20),
# LAST_NAME TEXT(20),
# AGE INTEGER,
# SEX TEXT(1),
# INCOME FLOAT
# );
# '''
# try:
#    cur.execute(qry)
#    print ('Table created successfully')
# except:
#    print ('error in creating table')
# conn.close()