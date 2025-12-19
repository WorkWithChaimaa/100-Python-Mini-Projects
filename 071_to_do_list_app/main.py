# Project 71: To-Do List App

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    task  = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed")
    else:
        print("Task not found")

def view_task():
    print("\n------To-Do List------")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

while True:
    print("\n1. Add task\n2. Remove task\n3. View task\n4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")