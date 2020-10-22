base_16 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
angle = 360 / len(base_16)

input_str = "Hello"

for character in input_str:
    hexadecimal_value = hex(ord(character))
    digit1 = hexadecimal_value[2]
    angle1 = base_16.index(digit1) * angle

    digit2 = hexadecimal_value[3]
    angle2 = base_16.index(digit2) * angle

    print(digit1, '-', angle1)
    print(digit2, '-', angle2)


