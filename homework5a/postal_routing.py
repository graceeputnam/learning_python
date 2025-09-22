import sys


def read_file(input):
    list1 = []
    with open(input) as file:
        return file.readlines()


def sort_mail(lines):
    new = []
    for line in lines:
        line = line.split()
        if line[-1] in zip_code_to_delivery_bin:
            new.append(zip_code_to_delivery_bin[line[-1]] + "\n")
        else:
            new.append("unknown\n")
    return new


def write_lines(cool_lines, output):
    with open(output, "w") as file:
        file.writelines(cool_lines)


def main(input, output):
    lines = read_file(input)
    cool_lines = sort_mail(lines)
    write_lines(cool_lines, output)


if __name__ == '__main__':
    zip_code_to_delivery_bin = {
        '5208': '16',
        '10118': '4',
        '227': '76',
        '12345': '1',
        '84604': '25',
        '84602': '25',
        '20895': '82'
    }


main(sys.argv[1], sys.argv[2])
