# Exercise 67: Expense Tracker

expenses = {}
def add_expense():
    category = input("Enter category (Food, Transport, etc.): ")
    amount = float(input("Enter amount: "))
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
        ''' we can use another method : expenses[category] = expenses.get(category, 0) + amount'''

    print("Expense added.")

def view_by_category():
    for category, total in expenses.items():
        print(f"{category}: ${total:.2f}")

def save_to_file():
    with open("expenses.txt", "w") as file:
        for category, total in expenses.items():
            file.write(f"{category}: ${total:.2f}\n")
    print("Expenses saved to a file.")

while True:
    print("\n1. Add Expense\n2. View Expenses by Category\n3. Save & Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_by_category()
    elif choice == "3":
        save_to_file()
        break
    else:
        print("Invalid choice.")




