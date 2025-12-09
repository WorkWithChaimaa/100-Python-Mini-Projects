# Exercise 18: Check if a Year is a Leap Year

# 1. Get user input and convert it to an integer
try:
    user_input = int(input("Enter a year: "))
except ValueError:
    print("Invalid input. Please enter a whole number year.")
    exit()

# 2. Apply the Leap Year Logic:
# (Divisible by 4 AND Not divisible by 100) OR (Divisible by 400)
if user_input % 4 == 0 and user_input % 100 != 0 or user_input % 400 == 0:
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is not a leap year.")