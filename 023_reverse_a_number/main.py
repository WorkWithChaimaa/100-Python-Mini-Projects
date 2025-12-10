# Exercise 23: Reverse a Number

# 1. Take integer input with robust error handling
while True:
    try:
        input_number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Try again.")

# --- Preparation for Reversal ---

# 2. Check if the number is negative and detach the sign
is_negative = input_number < 0
if is_negative:
    input_number = abs(input_number) # 2. Check if the number is negative and detach the sign

# 3. Initialize the accumulator
reversed_number = 0

# --- Reversal Loop ---

# 4. Use a 'while' loop to process digits until the number becomes 0
while input_number > 0 :

    # A. Extract the last digit
    last_digit = input_number % 10

    # B. Build the reversed number (Shift existing digits left (x10) and add the new digit)
    # The crucial step that reverses the order of the digits.
    reversed_number = ( reversed_number * 10) + last_digit

    # C. Remove the last digit from the original number
    input_number = input_number // 10
# --- Final Output ---

# 5. Re-apply the negative sign if the original number was negative
if is_negative:
    reversed_number = -reversed_number

# 6. Print the final result
print(f"Reversed number: {reversed_number}")
