from module1.e5_zoo import presentation, screen

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

def main():
    screen.clear()
    presentation.print_screen()

    age = presentation.ask_age()
    total_price = 0.0

    while age != 0:
        ticket_type = get_ticket_price(age)
        ticket_price = prices[ticket_type]

        totals[ticket_type] += 1

        screen.print_line(totals[ticket_type], \
                          tickets[ticket_type]["quantity"][0], tickets[ticket_type]["quantity"][1])

        screen.print_line("{:7.2f}€".format(totals[ticket_type] * ticket_price), \
                          tickets[ticket_type]["price"][0], tickets[ticket_type]["price"][1])

        total_price += ticket_price
        screen.format_line(1)
        screen.print_line("{:7.2f}€".format(total_price), 9, 19)
        screen.reset()
        age = presentation.ask_age()

    screen.locate(11, 1)


main()
