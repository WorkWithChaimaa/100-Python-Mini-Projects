# Exercise 4: Check the Type of Variable

# 1. Declare variables with their specific data types and values:
age = 21                          # Integer (int)
course_rating = 4.9               # Float (float)
course_name = "Python Programming"  # String (str)

# 2. Use the built-in type() function to display the data type of each variable.
# The type() function returns the class object, which is automatically formatted as
# <class 'type'> when printed inside an f-string.

# Output for the integer variable (age):
print(f"{age} is of type {type(age)}")

# Output for the float variable (course_rating):
print(f"{course_rating} is of type {type(course_rating)}")

# Output for the string variable (course_name):
print(f"{course_name} is of type {type(course_name)}")