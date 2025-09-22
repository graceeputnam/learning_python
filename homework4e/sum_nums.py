import sys


def add_char(lines):
    total = 0
    for i in lines:
        num = int(i)
        total += num
    return total


def read_file(input):
    new_list = ""
    with open(input) as file:
        new_file = file.readlines()
        for char in new_file:
            new_list += char
        return new_list.split()


def main(input):
    lines = read_file(input)
    print(f"The total is {add_char(lines)}")


if __name__ == '__main__':
    main(sys.argv[1])
# :)
