units = float(input("How many units of the same product: "))
price = float(input("Price in € per unit: "))

total_items = 0
final_price = 0

lines = ""

price_list = []
unit_list = []

while units > 0 and price > 0:
    total_units_price = units * price
    price_list.append(price)
    unit_list.append(units)

    total_items += units
    final_price += total_units_price

    units = float(input("How many units of the same product (0 to exit): "))
    price = float(input("Price in € per unit: "))

print("------------------------------------")

for price, units in zip(price_list, unit_list):
    print(price, "€ -", units, "units -", price * units, "€")

print("------------------------------------")
print("Total: ", round(final_price, 2), "€")
print("Items: ", round(total_items, 2))

