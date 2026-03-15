import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_Password",
    database="task_planner"
)

cursor = db.cursor()
while True:

    print("SMART DAILY TASK PLANNER")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter task title: ")
        description = input("Enter description: ")
        priority = int(input("Enter priority (1-High, 2-Medium, 3-Low): "))
        deadline = input("Enter deadline (YYYY-MM-DD): ")

        query = "INSERT INTO tasks (title, description, priority, deadline, status) VALUES (%s,%s,%s,%s,%s)"
        values = (title, description, priority, deadline, "Pending")

        cursor.execute(query, values)
        db.commit()
        print("Task added successfully!")

    elif choice == 2:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        for task in tasks:
            print(task)

    elif choice == 3:
        print("Exiting program...")
        break