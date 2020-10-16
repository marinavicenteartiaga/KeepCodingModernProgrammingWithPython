units = float(input("How many units of the same product: "))
price = float(input("Price in € per unit: "))

total_items = 0
final_price = 0

lines = ""

while units > 0 and price > 0:
    total_units_price = units * price
    lines += str(price) + "€ -" + str(units) + "units -" + str(round(total_units_price, 2)) + "€\n"
#    print(price, "€ -", units, "units -", round(total_units_price, 2), "€")

    total_items += units
    final_price += total_units_price

    units = float(input("How many units of the same product (0 to exit): "))
    price = float(input("Price in € per unit: "))

print("------------------------------------\n")
print(lines)
print("------------------------------------")
print("Total: ", round(final_price, 2), "€")
print("Items: ", round(total_items, 2))

