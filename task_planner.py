import mysql.connector

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nID | Title | Priority | Deadline | Status")
    print("-------------------------------------------")

    for task in tasks:
        print(task[0], "|", task[1], "|", task[3], "|", task[4], "|", task[5])

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
    print("3. View Pending Tasks")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Edit Task")
    print("7. Search Task")
    print("8. Exit")

    choice = (input("Enter your choice: "))
    if not choice.isdigit():
        print("Please enter a valid number.")
        continue

    choice = int(choice)

    if choice == 1:
        title = input("Enter task title: ")
        if title.strip() == "":
            print("Title cannot be empty!")
            continue
        description = input("Enter description: ")
        priority = input("Enter priority (1-3): ")

        if not priority.isdigit():
            print("Invalid priority. Use 1 (High), 2 (Medium), 3 (Low).")
            continue

        priority = int(priority)
        deadline = input("Enter deadline (YYYY-MM-DD): ")

        query = "INSERT INTO tasks (title, description, priority, deadline, status) VALUES (%s,%s,%s,%s,%s)"
        values = (title, description, priority, deadline, "Pending")

        cursor.execute(query, values)
        db.commit()
        print("Task added successfully!")

    elif choice == 2:
        cursor.execute("SELECT * FROM tasks ORDER BY priority ASC, deadline ASC")
        tasks = cursor.fetchall()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nID | Title | Priority | Deadline | Status")
            print("-------------------------------------------")

        for task in tasks:
            status = task[5]
            if status == "completed":
                status = "\u2714 COMPLETED"
            print(task[0], "|", task[1], "|", task[3], "|", task[4], "|", status)
                
    elif choice == 3:
        cursor.execute("SELECT * FROM tasks WHERE status = 'pending'")
        tasks = cursor.fetchall()
        display_tasks(tasks)
                    

    elif choice == 4:
        task_id = int(input("Enter task ID to delete: "))
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        db.commit()
        print("Task deleted successfully!")

    elif choice == 5:
        task_id = int(input("Enter task ID to mark as completed: "))
        cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = %s", (task_id,))
        db.commit()
        print("Task marked as completed!")

    elif choice == 6:
        task_id = int(input("Enter task ID to edit: "))
        
        new_title = input("Enter new title: ")
        new_description = input("Enter new description: ")
        new_priority = int(input("Enter new priority: "))
        new_deadline = input("Enter new deadline (YYYY-MM-DD): ")

        cursor.execute(
            "UPDATE tasks SET title=%s, description=%s, priority=%s, deadline=%s WHERE id=%s",
            (new_title, new_description, new_priority, new_deadline, task_id)
        )

        db.commit()
        print("Task updated successfully!")

    elif choice == 7:
        keyword = input("Enter keyword to search: ")
        cursor.execute("SELECT * FROM tasks WHERE title LIKE %s", ("%" + keyword + "%",))
        tasks = cursor.fetchall()

        if not tasks:
            print("No matching tasks found.")
        else:
            for task in tasks:
                status = task[5]

                if status == "completed":
                    status = "\u2714 COMPLETED"

                print(task[0], "|", task[1], "|", task[3], "|", task[4], "|", status)
    elif choice == 8:
        print("Exiting program...")
        break