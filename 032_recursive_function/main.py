# Exercise 32: Function Using Recursion (Factorial)

def factorial(n):
    """
    Computes the factorial of a non-negative integer 'n' recursively.
    """
    # 1. Base Case (Stop Condition)
    # The recursion stops when n is 0 or 1, returning 1.
    if n == 0 or n == 1:
        return 1

    # 2. Recursive Step
    # The function calls itself with a smaller number (n - 1)
    # and multiplies the result by the current n.
    else:
        return n * factorial(n - 1)


# Call the function and print the result
print(f"Factorial of 5 is {factorial(5)}")