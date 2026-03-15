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
    print("3. Delete Task")
    print("4. Exit")

    choice = (input("Enter your choice: "))
    if not choice.isdigit():
        print("Please enter a valid number.")
        continue

    choice = int(choice)

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
        cursor.execute("SELECT * FROM tasks ORDER BY priority ASC, deadline ASC")
        tasks = cursor.fetchall()

        for task in tasks:
            print("ID:", task[0])
            print("Title:", task[1])
            print("Description:", task[2])
            print("Priority:", task[3])
            print("Deadline:", task[4])
            print("Status:", task[5])
            print("---------------------")

    elif choice == 3:
        task_id = int(input("Enter task ID to delete: "))
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        db.commit()
        print("Task deleted successfully!")

    elif choice == 4:
        print("Exiting program...")
        break