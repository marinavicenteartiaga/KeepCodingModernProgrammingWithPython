def clear():
    print("\033[23")


def locate(line, column):
    print("\033[{};{}H".format(line, column), end="")


def clear_line(line=None, column=None):
    if line is not None and column is not None:
        locate(line, column)
    elif line is not None:
        locate(line, 1)

    print("\033[K", end="")


def print_line(string, line, column, del_end=False):
    locate(line, column)
    if del_end:
        clear_line()
    print(string, end="")


def input_line(msg, line, column, del_end=True):
    locate(line, column)
    if del_end:
        clear_line()
    return input(msg)


def format_line(style, color_text=30, color_background=40):
    print("\033{};{};{}n".format(style, color_text, color_background), end="")


def reset():
    format_line(0, 37, 40)

