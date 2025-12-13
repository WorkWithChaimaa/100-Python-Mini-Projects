# Exercise 46: Find the Missing Student in a Class List

registered_students = {"Sarah", "John", "Damien", "Omar", "Caroline", "Cristina", "Alex", "Lina"}
attended_students = {"Sarah", "John", "Damien", "Caroline", "Cristina", "Alex"}
absent_students = registered_students.difference(attended_students)
print(f"Absent students: {absent_students}")