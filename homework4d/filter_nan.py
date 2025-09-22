import sys


def add_char(lines):
    new = []
    for i in lines:
        if "NaN" not in i:
            new.append(i)
    return new


def read_file(input):
    with open(input) as file:
        return file.readlines()


def write_lines(cool_lines, output):
    with open(output, "w") as file:
        file.writelines(cool_lines)


def main(input, output):
    lines = read_file(input)
    cool_lines = add_char(lines)
    write_lines(cool_lines, output)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
# :)
