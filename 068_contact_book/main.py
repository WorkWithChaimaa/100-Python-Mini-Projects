# Project 68: Contact Book

contact_details = {}

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    contact_details[name] = phone_number
    print("Contact details saved")

def search_contact():
    name = input("Enter name: ")
    if name in contact_details:
        print(contact_details[name])
    else:
        print("Contact not found")

def display_contacts():
    for name, phone_number in contact_details.items():
        print(f"{name} : {phone_number}")

def save_contact():
    with open("contacts.txt", "w") as file:
        for name, phone_number in contact_details.items():
            file.write(f"{name} : {phone_number}\n")
        print("Contact saved")

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Display Contacts\n4. Save & Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        save_contact()
        break
    else:
        print("Invalid choice")
