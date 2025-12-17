# Project 69: Temperature Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 5

choice = input("Convert to (C/F): ").upper()
temp = float(input("Enter temperature: "))

if choice == "C":
   print(f"Temperature in Celsius: {fahrenheit_to_celsius(temp):.2f}°C")
elif choice == "F":
   print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temp):.2f}°F")
else:
   print("Invalid choice.")