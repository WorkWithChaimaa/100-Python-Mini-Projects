# Exercise 24: Multiplication Table

# 1. Take integer input (N) with error handling
try:
    input_number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# 2. Print the multiplication table up to 10
# 'i' represents the factor (1 to 10)
for i in range(1, 11):
    # Calculate the product
    product = input_number * i

    # Print the result in the format: N x i = product
    print(f"{input_number} x {i} = {product}")