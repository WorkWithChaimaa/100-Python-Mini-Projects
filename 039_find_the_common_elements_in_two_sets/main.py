# Exercise 39: Find Common Elements in Two Sets

# 1. Define the two input sets
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"David", "Alice", "Eve", "Frank"}

# 2. Find the intersection (common students)
# The .intersection() method returns a new set containing elements present in both.
common_students = python_students.intersection(java_students)

# 3. Print the result
print(common_students)