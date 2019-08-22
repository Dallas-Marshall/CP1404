# Electricity Costs

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
electricity_cost = 0
# Define Menu:
MENU = """Please select tariff;
Tariff(11)
Tariff(31)"""

# Display Menu
print(MENU)

# Ask user to select menu option
user_choice = int(input(">>> "))

# Define relevant electricity cost
if user_choice == 31:
    electricity_cost = TARIFF_31
else:
    electricity_cost = TARIFF_11

# Daily use in kWh
daily_use = float(input("What is your daily usage in KWh: "))

# Number of days in the billing period
billing_period = int(input("How many days are in the billing period? "))

# Calculate bill total
bill_total = electricity_cost * daily_use * billing_period
print("Your estimated bill is: ${:.2f}".format(bill_total))
