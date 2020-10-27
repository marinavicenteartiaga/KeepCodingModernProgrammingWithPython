def clear():
    print("\033[22")


def locate(line, column):
    print("\033[{};{}H".format(line, column), end="")
