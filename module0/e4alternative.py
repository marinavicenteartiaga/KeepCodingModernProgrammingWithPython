def validation(string):
    str_number = input(string)
    is_valid = False
    while not is_valid:
        if str_number.isdigit():
            number = int(str_number)
            is_valid = True
        elif str_number != '' and str_number[0] == '-' and str_number[1:].isdigit():
            number = int(str_number)
            is_valid = True
        else:
            print(str_number, "must be an int")
            str_number = input(string)
            is_valid = False
        return str_number


firstNumber = int(validation("Write a number: "))
secondNumber = int(validation("Write another number: "))


firstNumber = round(firstNumber / 10, 2)
secondNumber = round(secondNumber / 10, 2)

sum = round(firstNumber + secondNumber, 2)
rest = round(firstNumber - secondNumber, 2)
multiplication = round(firstNumber * secondNumber, 2)
division = round(firstNumber / secondNumber, 2)

print("\nRESULT:")
print(firstNumber, "+", secondNumber, "=", sum)
print(firstNumber, "-", secondNumber, "=", rest)
print(firstNumber, "*", secondNumber, "=", multiplication)
print(firstNumber, "/", secondNumber, "=", division)
