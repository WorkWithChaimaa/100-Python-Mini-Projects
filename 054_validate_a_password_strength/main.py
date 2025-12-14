# Exercise 54: Validate a Password Strength
special_chars = '!@#$%^&*()-_+=<>?/'

# The while True loop runs until the 'break' statement is hit.
while True:
    password = input("Enter your password: ")

    # --- CHECKLIST: Evaluate ALL three conditions ---
    has_min_length = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    has_special_chars = any(char in special_chars for char in password)

    # --- DECISION ---
    if has_min_length and has_number and has_special_chars:
        print("Password is valid")
        break  # Exit the loop, validation successful

    # --- FAILURE ---
    else:
        print("\n--- Validation Failed ---")
        if not has_min_length:
            print("❌ Must be at least 8 characters long.")
        if not has_number:
            print("❌ Must contain at least one number (0-9).")
        if not has_special_chars:
            print(f"❌ Must contain at least one special character (e.g., {special_chars}).")

        # The loop automatically repeats, asking for a new password on the next iteration.