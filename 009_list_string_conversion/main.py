# Exercise 9: Convert List to a String and Back

# 1. Declare the initial list of words
word_list = ["python", "is", "programming"]

# --- Part 1: Convert List to a String ---

# Use the string join() method to combine the list elements.
# The string before the .join() is the SEPARATOR used between elements.
# We use ", " as the separator to match the expected output format.
string_result = ", ".join(word_list)
# Print the result
# Expected Output: List to String: Python, is, amazing
print(f"List to String: {string_result}")

# --- Part 2: Convert the String back into a List ---

# Use the string split() method to break the string into a list of words.
# We must use the exact separator we joined with (", ") so Python knows where to split.
list_result = string_result.split(", ")

# Print the result
# Expected Output: String to List: ['Python', 'is', 'amazing']
print(f"String to List: {list_result}")
