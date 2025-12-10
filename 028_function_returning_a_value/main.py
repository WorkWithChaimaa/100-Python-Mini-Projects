# Exercise 28: Function Returning a Value

# 1. Define the function square(num) that returns the square of the input number
def square(num):
    """Calculates and returns the square of a number."""
    return num ** 2

# 2. Call the function inside an f-string to print the result
# The function call 'square(5)' is replaced by its returned value (25) before printing.
print(f"The square of 5 is {square(5)}")
