import sys


def add_char(lines, profession):
    total = 0
    amount = 0
    for i in lines:
        new_i = i.split(",")
        if new_i[5] == profession:
            total += int(new_i[3])
            amount += 1
    avg = total/ amount
    return int(avg)


def read_file(input):
    list1 = []
    with open(input) as file:
        return file.readlines()


def main(input, profession):
    lines = read_file(input)
    cool_lines = add_char(lines, profession)
    print(f"The average income of {profession} is {cool_lines}")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

