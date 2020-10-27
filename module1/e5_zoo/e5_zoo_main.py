import screen

prices = {
        "Baby": 0.0,
        "Kid": 14.0,
        "Adult": 23.0,
        "Retired": 18.0
    }

totals = {"Baby": 0, "Kid": 0, "Adult": 0, "Retired": 0}

tickets = {
        "Baby": {
            "quantity": (4, 15),
            "price": (4, 19),
        },
        "Kid": {
            "quantity": (5, 15),
            "price": (5, 19),
        },
        "Adult": {
            "quantity": (6, 15),
            "price": (6, 19),
        },
        "Retired": {
            "quantity": (7, 15),
            "price": (7, 19),
        }
    }

def get_ticket_price(input_age):
    if 0 < input_age <= 2:
        ticket_type = "Baby"
    elif input_age <= 12:
        ticket_type = "Kid"
    elif input_age < 65:
        ticket_type = "Adult"
    else:
        ticket_type = "Retired"

    return ticket_type


def validate_input(string):
    try:
        number = int(string)
        if number >= 0:
            return True
        return False
    except:
        return False


def ask_age():
    screen.locate(1, 1)
    input_age = input("What's your age? ")
    while not validate_input(input_age):
        print("Wrong age. Try it again!")
        screen.locate(1, 1)
        input_age = input("What's your age? ")

    return int(input_age)


def print_screen():
    screen.locate(5, 5)
    print("Baby....:   -'")
    screen.locate(6, 5)
    print("Kid.....:   -'")
    screen.locate(7, 5)
    print("Adult...:   -'")
    screen.locate(8, 5)
    print("Retired.:   -'")

    screen.locate(9, 8)
    print("Total...: ")


def main():
    screen.clear()
    print_screen()
    age = ask_age()
    total_price = 0.0
    line = 4

    while age != 0:
        ticket_type = get_ticket_price(age)
        ticket_price = prices[ticket_type]

        totals[ticket_type] += 1

        screen.locate(tickets[ticket_type]["quantity"][0], tickets[ticket_type]["quantity"][1])
        print(totals[ticket_type])
        screen.locate(tickets[ticket_type]["price"][0], tickets[ticket_type]["price"][1])
        print("{:7.2f}€".format(totals[ticket_type]*ticket_price))

        total_price += ticket_price
        screen.locate(9, 19)
        print("{:7.2f}€".format(total_price))

        age = ask_age()

    screen.locate(11, 1)


main()
