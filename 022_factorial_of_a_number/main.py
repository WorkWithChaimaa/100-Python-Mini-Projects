# Exercise 22: Factorial of a Number

# 1. Get user input with error handling
while True :
    try:
        input_number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. please enter a whole number.")

# 2. Guard Clauses for negative and zero input
if input_number < 0:
    print("The factorial isn't defined for negative numbers.")
    exit()
elif input_number == 0:
    print("The factorial of 0 is 1.")
    exit()

# 3. Initialize the accumulator for multiplication
# Must be 1, because anything multiplied by 1 is itself.
factorial_result = 1

# 4. Loop through the numbers from 1 up to (and including) input_number
for i in range(1, input_number + 1):
     # Accumulate the product: factorial_result = factorial_result * i
     factorial_result *= i

# 5. Print the final result
print(f"Factorial of {input_number} is {factorial_result}")