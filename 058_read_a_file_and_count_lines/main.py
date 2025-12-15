## Exercise 58: Read a File and Count Lines

# The two methods to solve this exercise are presented below.
# Only the code NOT enclosed in triple quotes ("""...""") is active.

# -----------------------------------------------------------
# METHOD 1: Line-by-Line Iteration (Best for Very Large Files)
# -----------------------------------------------------------
"""
# Get the file name from the user
file_name = input("Enter file name for Method 1: ")
line_count = 0

try:
    # Open the file and iterate through it line by line
    with open(file_name, "r") as file:
        for line in file:
            line_count += 1

    print("\n--- Method 1 Result ---")
    print(f"Total lines: {line_count}")

except FileNotFoundError:
    print(f"\n--- Method 1 Error ---")
    print("File not found.")
"""

# -----------------------------------------------------------
# METHOD 2: Using len(file.readlines()) (Most Concise) - ACTIVE
# -----------------------------------------------------------

# Get the file name from the user
file_name = input("Enter file name for Method 2: ")

try:
    # Open the file
    with open(file_name, "r") as file:
        # Read all lines into a list and immediately get the length (count)
        total_lines = len(file.readlines())

        print("\n--- Method 2 Result ---")
        print(f"Total lines: {total_lines}")

except FileNotFoundError:
    print(f"\n--- Method 2 Error ---")
    print("File not found.")