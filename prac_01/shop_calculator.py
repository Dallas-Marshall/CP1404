number_of_items = int(input("How many items are you buying: "))

while number_of_items <= 0:
    number_of_items = int(input("How many items are you buying: "))

total_price = 0

for i in range(1, number_of_items + 1):
    price_of_item = float(input("price of item " + str(i) + ": $ "))
    total_price = total_price + price_of_item

if total_price > 100:
    total_price = total_price * 0.9
print("Your total price for " + str(number_of_items) + " items is: $ " + str(total_price))
