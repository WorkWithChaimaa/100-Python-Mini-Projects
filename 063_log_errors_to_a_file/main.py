# Exercise 63: Log Errors to a File
log_file = "error_log.txt"
try:
    numerator = float(input("Enter a numerator: "))
    denominator = float(input("Enter a denominator: "))
    division = numerator / denominator
except ZeroDivisionError:
    error = "Error: Division by zero is not allowed.\n"
    with open(log_file, "a") as file:
        file.write(error)
    print("Error logged to file.")

except ValueError:
    print("Invalid input, please enter integers only.")
