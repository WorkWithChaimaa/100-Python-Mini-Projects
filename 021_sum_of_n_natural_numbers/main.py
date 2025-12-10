# Exercise 21: Sum of First N Natural Numbers

# 1. Take an integer input N, with error handling
try:
    input_number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# 2. Initialize the accumulator
total_sum = 0

# 3. Use the 'for' loop to iterate and accumulate the sum
for num in range(1, input_number + 1):
    total_sum += num

# 4. Print the final result in the required format
print(f"Sum of first {input_number} numbers: {total_sum}")