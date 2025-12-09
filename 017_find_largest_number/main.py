# Exercise 17: Find the Largest Number (Using Pythonic max() function)

# 1. Take three numbers as input on a single line.
# map(int, ...) converts the space-separated strings from split() into integers.
try:
    num1, num2, num3 = map(int, input("Enter three numbers: ").split())

    # 2. Find the largest number using the built-in max() function
    largest = max(num1, num2, num3)

    # 3. Print the result
    print(f"The largest number is {largest}.")

except ValueError:
    print("Invalid input. Please enter exactly three whole numbers separated by spaces.")
