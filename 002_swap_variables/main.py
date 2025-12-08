# Exercise 2: Swap Two Variables Without a Third Variable

# 1. Initialize variables with their starting values
students_morning = 15
students_evening = 25

# Print the values BEFORE the swap to confirm their initial state
print(f"Before Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")

# 2. Perform the swap using Python's 'tuple packing and unpacking'
# The values on the right side (students_evening, students_morning) are evaluated first.
# This creates a temporary tuple (25, 15).
# The values in this tuple are then simultaneously assigned to the variables on the left.
students_morning, students_evening = students_evening, students_morning

# 3. Print the values AFTER the swap to verify the operation
print(f"After Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")