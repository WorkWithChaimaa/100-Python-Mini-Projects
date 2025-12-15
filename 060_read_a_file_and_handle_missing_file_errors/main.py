# Exercise 60: Read a File and Handle Missing File Errors

file = input("Enter file name: ")
try:
    with open(file, "r") as file:
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print(f"Error: {file} not found.")