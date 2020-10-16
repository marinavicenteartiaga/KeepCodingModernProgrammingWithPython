def is_decimal(number):
    try:
        float(number)
        return True
    except:
        return False


base_input = input("Triangle's base: ")
while not is_decimal(base_input):
    print(base_input, "Must be a number")
    base_input = input("Triangle's base: ")

height_input = input("Triangle's height: ")
while not is_decimal(height_input):
    print(height_input, "Must be a number")
    height_input = input("Triangle's height: ")

base = float(base_input)
height = float(height_input)

area = (base * height) / 2

print(round(area, 2), "Is the area of the triangle.")

