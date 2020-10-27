import screen

prices = {2: 0, 12: 14, 65: 23, 99: 10}

def get_ticket_price(input_age):
    if 0 < input_age <= 2:
        price = 0
    elif input_age <= 12:
        price = 14
    elif input_age < 65:
        price = 23
    else:
        price = 18

    return price


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
        screen.locate(1, 2)
        input_age = input("What's your age? ")

    return int(input_age)


screen.clear()
age = ask_age()
total_price = 0
line = 4

n_tickets_baby = 0
n_tickets_kid = 0
n_tickets_adult = 0
n_tickets_retired = 0

while age != 0:
    ticket_price = get_ticket_price(age)
    if ticket_price == 0:
        line = 4
        n_tickets_baby += 1
        screen.locate(line, 1)
        print("Ticket price: {}\tNum. Tickets: {}".format(ticket_price, n_tickets_baby))
    if ticket_price == 14:
        line = 5
        n_tickets_kid += 1
        screen.locate(line, 1)
        print("Ticket price: {}\tNum. Tickets: {}".format(ticket_price, n_tickets_kid))
    if ticket_price == 23:
        line = 6
        n_tickets_adult += 1
        screen.locate(line, 1)
        print("Ticket price: {}\tNum. Tickets: {}".format(ticket_price, n_tickets_adult))
    if ticket_price == 18:
        line = 7
        n_tickets_retired += 1
        screen.locate(line, 1)
        print("Ticket price: {}\tNum. Tickets: {}".format(ticket_price, n_tickets_retired))

    line += 1
    total_price += ticket_price

    age = ask_age()

screen.locate(line, 1)
print("Total: {}".format(total_price))
