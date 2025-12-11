# Exercise 31: Function Using Local Variable

def local_variable():
    # 1. 'message' is a LOCAL variable. It is created when the function runs.
    message = "Lkhbira Rocks"
    print(f"Inside function: {message}")

# Call the function. This runs the code inside and prints the first line.
local_variable()

# 2. Try accessing the variable OUTSIDE the function.
# Python throws an error because the variable 'message' was destroyed
# as soon as the function finished running.
print(message)