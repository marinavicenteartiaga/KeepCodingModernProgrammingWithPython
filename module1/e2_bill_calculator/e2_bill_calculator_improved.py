items = []
_UNITS = 0
_PRICE = 1
_TOTAL = 2


def is_decimal(number):
    try:
        float(number)
        return True
    except:
        return False


def is_positive_int(number):
    if str.isdigit(number):
        return True
    else:
        return False


str_units = input("How many units of the same product: ")

while not is_positive_int(str_units):
    str_units = input("Try again! It must be an int: ")

units = int(str_units)

str_price = input("Price in € per unit: ")

while not is_decimal(str_price):
    str_price = input("Try again! It must be a positive number: ")

price = float(str_price)

while units > 0 and price > 0:

    total = units * price
    item = [units, price, total]
    items.append(item)

    str_units = input("How many units of the same product: ")

    while not is_positive_int(str_units):
        str_units = input("Try again! It must be an int: ")

    units = int(str_units)

    str_price = input("Price in € per unit: ")

    while not is_decimal(str_price):
        str_price = input("Try again! It must be a positive number: ")

    price = float(str_price)

print("\n----------------------")

for item in items:
    if item[_UNITS] > 1:
        print(item[_UNITS], " units - ", item[_PRICE], "€ - ", item[_TOTAL], "€")
    else:
        print(item[_UNITS], " unit - ", item[_PRICE], "€ - ", item[_TOTAL], "€")

total_units = 0
for item in items:
    total_units += item[_UNITS]

total_price = 0
for item in items:
    total_price += item[_TOTAL]

print("----------------------")

print("Total units: ", total_units)
print("Final price: ", total_price, "€")
