# Exercise 65: Automatically Close a File Using a Context Manager

file_name = "notes.txt"
with open("notes.txt", "r") as file:
    print(file.read())