# Exercise 64: Read and Process a CSV File

import csv

file_name = "sales_data.csv"


# --- Function to format and print a single row ---
def format_row(row):
    return " | ".join(row)

try:
    with open(file_name, 'r', newline='') as file:

        csv_reader = csv.reader(file)

        # 1. Store all rows in a list
        all_rows = list(csv_reader)

        # Get the total count for reference
        total_rows = len(all_rows)

        print("-" * 30)
        print(f"Reading file: {file_name} (Total rows: {total_rows})")
        print("-" * 30)

        # --- 2. Print the First 5 Rows (The Head) ---

        print("\n--- FIRST 5 ROWS (HEAD) ---")
        # List slicing [0:5] grabs elements from index 0 up to (but not including) 5
        first_5_rows = all_rows[0:5]

        for i, row in enumerate(first_5_rows):
            print(f"Row {i + 1:2}: {format_row(row)}")

        # --- 3. Print the Last 5 Rows (The Tail) ---

        print("\n--- LAST 5 ROWS (TAIL) ---")
        # List slicing [-5:] grabs the last 5 elements of the list
        last_5_rows = all_rows[-5:]

        # Calculate the starting row number for accurate display
        start_index = total_rows - len(last_5_rows)

        for i, row in enumerate(last_5_rows):
            print(f"Row {start_index + i + 1}: {format_row(row)}")

        print("-" * 30)


except FileNotFoundError:
    print(f"Error: The file {file_name} was not found. Please ensure it exists.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")