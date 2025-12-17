# Project 66: Student Grade Management System

students = {}
def add_students():
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    students[name] = grade
    print("Student added successfully")

def update_grade():
    name = input("Enter student name: ")
    if name in students:
        grade = input("Enter grade: ")
        students[name] = grade
        print("Grade updated successfully")
    else:
        print("Student not found")

def get_grade():
    name = input("Enter student name: ")
    if name in students:
        print(students[name])
    else:
        print("Student not found")

def display_all():
    for key, value in students.items():
        print(f"{key}: {value}")
while True:
    print("\n1. Add students\n2. Update grade\n3. Get grade\n4. Display all\n5. Exit")
    choice = input("Enter you choice: ")
    if choice == "1":
        add_students()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        get_grade()
    elif choice == "4":
        display_all()
    elif choice == "5":
        break
    else:
        print("Invalid choice")

print(students)