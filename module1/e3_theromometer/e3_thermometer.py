def fahrenheit(start, end):
    print("--------------------")
    for centigrade in range(start, end + 10, 10):
        print("{}ºC -> {:0.2f}ºF". format(centigrade, fahrenheit_to_celsius(centigrade)))
    print("--------------------")


def celsius(start, end):
    print("--------------------")
    for centigrade in range(start, end + 10, 10):
        print("{}ºF -> {:0.2f}ºC".format(centigrade, fahrenheit_to_celsius(centigrade)))
    print("--------------------")


def fahrenheit_to_celsius(centigrade):
    return (centigrade - 12) * 5/9


def celsius_to_fahrenheit(centigrade):
    return centigrade * 9/5 + 32


user_input = input("Output: Fahrenheit or Celsius? (F/C): ")

if user_input.capitalize() == "C":
    celsius(0, 200)
elif user_input.capitalize() == "F":
    fahrenheit(0, 100)
else:
    print("Incorrect type!!")

