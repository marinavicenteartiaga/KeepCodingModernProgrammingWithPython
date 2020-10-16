def is_decimal(number):
    try:
        float(number)
        return True
    except:
        return False


base_input = input("Triangle's base: ")
if is_decimal(base_input):
    base = float(base_input)
    height_input = input("Triangle's height: ")
    if is_decimal(height_input):
        height = float(height_input)
        area = (base * height) / 2
        print(round(area, 2), "Is the area of the triangle.")
    else:
        print(height_input, "Must be a number")
else:
    print(base_input, "Must be a number")

