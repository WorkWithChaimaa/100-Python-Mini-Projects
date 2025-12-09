# Exercise 19: Print Numbers from 1 to N

# 1. Take an integer input N, with error handling
try:
    N_input = input("Enter a number: ")
    N = int(N_input)

except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# 2. Use a 'for' loop and range(1, N + 1)
# range(1, N + 1) generates numbers from 1 up to and including N.
# The end=" " argument ensures the numbers are printed on the same line, separated by a space.
for number in range(1, N + 1):
    print(number, end=" ")