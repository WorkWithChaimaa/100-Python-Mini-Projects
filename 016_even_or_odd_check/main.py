# Exercise 16: Check if a Number is Even or Odd

# 1. Get input from the user and convert it directly to an integer
number = int(input("Enter a number: "))

# 2. Use the if-else structure with the modulus operator (%)
# If the remainder of division by 2 is 0, the number is even.
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    # If the remainder is not 0 (it will be 1 for positive odd numbers), it is odd.
    print(f"{number} is an odd number.")