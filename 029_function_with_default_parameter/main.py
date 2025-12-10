# Exercise 29: Function with Default Parameter

# 1. Define the function greet(name) with a default value of "Student"
def greet(name="Student"):
    """
    Greets the user.
    If no name is provided when called, it uses the default "Student".
    """
    print(f"Hello, {name}!")

# 2. Call the function WITHOUT a parameter (Uses the default value)
greet()

# 3. Call the function WITH a parameter (Overrides the default value)
greet("Amine")