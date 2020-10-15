
while True:
    try:
        firstNumber = int(input("Write a number: "))
        break
    except ValueError:
        print("That wasn't a valid number!! Try again :-)")

while True:
    try:
        secondNumber = int(input("Write another number: "))
        break
    except ValueError:
        print("That wasn't a valid number!! Try again :-)")

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
