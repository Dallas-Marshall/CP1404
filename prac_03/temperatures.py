"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def celsius_to_fahrenheit(temperature):
    temperature_in_fahrenheit = temperature * 9.0 / 5 + 32
    return temperature_in_fahrenheit


def fahrenheit_to_celsius(temperature_fahrenheit):
    temperature_in_celsius = 5 / 9 * (temperature_fahrenheit - 32)
    return temperature_in_celsius


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        print("Result: {:.2f} F".format(celsius_to_fahrenheit(celsius)))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        print("result: {:.2f}".format(fahrenheit_to_celsius(fahrenheit)))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
