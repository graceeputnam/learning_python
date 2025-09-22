import sys


def add_char(lines, string):
    new = []
    for i in lines:
        new_line = string + " " + i
        new.append(new_line)
    return new


def read_file(input):
    with open(input) as file:
        return file.readlines()


def write_lines(cool_lines, output):
    with open(output, "w") as file:
        file.writelines(cool_lines)


def main(input, output, string):
    lines = read_file(input)
    cool_lines = add_char(lines, string)
    write_lines(cool_lines, output)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
