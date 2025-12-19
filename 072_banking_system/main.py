# Project 72: Banking System

balance = 0

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print(f"deposited ${amount:.2f}. New balance is ${balance:.2f}")

def withdraw():
    global balance
    amount = float(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print(f"withdrew ${amount:.2f}. New balance is ${balance:.2f}")
    else:
        print("Insufficient funds.")

while True:
    print("Welcome to the banking system.")
    print("Please enter your tasks:")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")
    task = input("Enter your task: ")
    if task == "1":
        deposit()
    elif task == "2":
        withdraw()
    elif task == "3":
        print(f"Current balance: ${balance:.2f}")
    elif task == "4":
        break
    else:
        print("Invalid input!")


