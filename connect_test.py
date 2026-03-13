import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Projects4?!@",
    database="task_planner"
)

print("Connection successful!")

cursor = db.cursor()
cursor.execute("SELECT * FROM tasks")

for row in cursor.fetchall():
    print(row)