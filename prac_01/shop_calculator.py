"""Calculate number of items"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items! Please enter a non-negative integer.")
    number_of_items = int(input("Number of items: "))

total_price = 0.0
count = 0

"""Determine the price of each item and calculate total price"""

while count < number_of_items:
    price = float(input(f"Price of item: "))
    total_price += price
    count += 1

if total_price > 100:
    total_price *= 0.90
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
