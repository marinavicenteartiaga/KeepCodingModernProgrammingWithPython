from module1.e5_zoo import screen

screen.locate(1, 1)
print("Age: ")

screen.locate(4, 1)
print("Baby tickets...: ")
print("Kid tickets....: ")
print("Adult tickets..: ")
print("Retired tickets: ")

def validate_input(string):
    try:
        number = int(string)
        if number >= 0:
            return True
        return False
    except:
        return False


def ask_age():
    input_age = screen.input_line("What's your age? ", 1, 1)
    while not validate_input(input_age):
        screen.format_line(0, 33, 41)
        screen.print_line("Wrong age. Try it again!", 25, 1, True)
        input_age = screen.input_line("What's your age? ", 1, 1)

    screen.clear_line(25)

    return int(input_age)


def print_screen():
    screen.print_line("Baby....:   -'", 4, 5)
    screen.print_line("Kid.....:   -'", 5, 5)
    screen.print_line("Adult...:   -'", 6, 5)
    screen.print_line("Retired.:   -'", 7, 5)

    screen.format_line(1)
    screen.print_line("Total...: ", 9, 8)
    screen.reset()

