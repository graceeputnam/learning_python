import sys
import random


def choose_quote(lines):
    return random.choice(lines)


def print_quote(quote):
    new_string = []
    for char in quote:
        if char == "|":
            new_string.append("\n")
        else:
            new_string.append(char)
    new = ''.join(new_string)
    print(new)


def read_file(input):
    list1 = []
    with open(input) as file:
        return file.readlines()


def main(input):
    lines = read_file(input)
    quote = choose_quote(lines)
    print_quote(quote)


if __name__ == '__main__':
    main(sys.argv[1])
# :)
