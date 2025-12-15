# Exercise 61: Handle Division by Zero in a Calculator

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    result = float(num1) / float(num2)
    print(f"The division is: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter only numbers.")