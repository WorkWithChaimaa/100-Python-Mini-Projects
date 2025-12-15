# Exercise 62: Validate User Input as an Integer

while True:
    try:
        number = input("Enter a number: ")
        number = int(number)
        print(f"You entered: {number}")
        break

    except ValueError:
        print("Invalid input. Please enter an integer.")