import sys


def read_file(input):
    list1 = []
    with open(input) as file:
        return file.readlines()


def correction(lines):
    new = []
    for line in lines:
        line = line.split()
        new_line = []
        for word in line:
            if word in corrections:
                new_line.append(corrections[word])
            else:
                new_line.append(word)
        new_line = " ".join(new_line)
        new_line += "\n"
        new.append(new_line)
    return new


def write_lines(cool_lines, output):
    with open(output, "w") as file:
        file.writelines(cool_lines)


def main(input, output):
    lines = read_file(input)
    cool_lines = correction(lines)
    write_lines(cool_lines, output)


if __name__ == '__main__':
    corrections = {
    'teh': 'the',
    'adn': 'and',
    'thye': 'they',
    'yuo': 'you',
    'i': 'I'
    }


main(sys.argv[1], sys.argv[2])
