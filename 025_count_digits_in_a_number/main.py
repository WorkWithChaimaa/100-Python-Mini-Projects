# Exercise 25: Count Digits in a Number

# --- STEP 1: Get the Number
while True:
    try:
        input_number = int(input("Enter a number: "))
        break # Exit the loop if input is a valid integer
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# --- STEP 2: Handle Edge Cases and Initialize ---

# Copy the original number before we start modifying input_number
original_number = input_number

# Initialize the counter
count = 0

# Handle the case where the input is 0 (it has 1 digit)
if input_number == 0:
    count = 1
    print(f"The number {original_number} has {count} digit(s).")
    exit()

# Use the absolute (positive) value for the math loop
input_number = abs(input_number)

# --- STEP 3 & 4: The Counting Loop ---

# The loop runs as long as the number has digits left
while input_number > 0:

    # Action A: Count the digit we are about to remove
    count += 1

    # Action B: Shrink the number by removing the last digit
    input_number //= 10

# --- STEP 5: Print the Result ---
print(f"The number {original_number} has {count} digits.")