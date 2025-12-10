# Exercise 30: Function Using Global Variable

# 1. Declare the global variable 'academy'
academy = "Lkhibra"

# 2. Define a function that reads the value of the global variable
def print_academy():
    """
    Reads and prints the value of the global variable 'academy'.
    No 'global' keyword is needed because we are only reading, not changing, the variable.
    """
    print(f"The best academy is {academy}!")

# 3. Call the function to execute the print statement
print_academy()