"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SALES_BRACKET = 1000

sales = float(input("Enter sales: $ "))
while sales >= 0:
    if sales < SALES_BRACKET:
        bonus = sales / 10
    else:
        bonus = sales / 100 * 15
    print("Your bonus is: $", bonus, sep='')
    sales = float(input("enter sales: $ "))
