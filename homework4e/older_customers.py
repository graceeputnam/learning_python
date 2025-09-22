import sys


def add_char(lines, age):
    new_string = []
    for i in lines:
        new_line = []
        new_i = i.split(',')
        if new_i[0] == "CustomerID":
            new_line.append(i)
        elif int(new_i[2]) > int(age):
            new_line.append(i)
        sentence = ",".join(new_line)
        new_string.append(sentence)
    return new_string


def read_file(input):
    with open(input) as file:
        return file.readlines()


def write_lines(cool_lines, output):
    with open(output, "w") as file:
        file.writelines(cool_lines)


def main(input, output, age):
    lines = read_file(input)
    cool_lines = add_char(lines, age)
    write_lines(cool_lines, output)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
# :)
