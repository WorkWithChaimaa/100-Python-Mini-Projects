# Exercise 20: Print Even Numbers up to N (Using the 'continue' Statement)

# 1. Get user input with error handling
try:
    N = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# 2. Loop through all numbers from 1 to N
for number in range(1, N + 1):

    # Check if the number is ODD (remainder is not 0)
    if number % 2 != 0:
        # If it's ODD, skip the rest of the loop block and move to the next number
        continue

    # If the code reaches this line, the number must be EVEN, so print it
    print(number, end=" ")