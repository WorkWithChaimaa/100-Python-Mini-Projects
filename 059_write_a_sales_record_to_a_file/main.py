SALES_RECORD_FILE = "sales.txt"

customer = input("Enter customer name: ")
item = input("Enter item: ")

price = 0.00

try:
    price = float(input("Enter price: "))
    formatted_price = f"${price:.2f}"
except ValueError:
    print("Invalid price entered. Defaulting to $0.00.")
    formatted_price = "$0.00"

sales_record = (
    f"Customer: {customer}, "
    f"Item: {item}, "
    f"Price: {formatted_price}\n"
)

try:
    with open(SALES_RECORD_FILE, "a") as file:
        file.write(sales_record)
        print(f"Record written to {SALES_RECORD_FILE}")

except Exception as e:
    print(f"An error occurred during file writing: {e}")

try:
    with open(SALES_RECORD_FILE, "r") as file:
        print("\n--- Current sales.txt content ---")
        print(file.read())
except FileNotFoundError:
    pass