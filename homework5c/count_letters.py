import sys


def read_file(file):
    with open(file) as file:
        return file.read()


def create_dict(input, doc):
    new = {}
    for letter in input:
        new[letter] = 0
        for char in doc:
            if char == letter:
                new[letter] += 1
    return new


def main(input, file):
    doc = read_file(file)
    print(create_dict(input, doc))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
# :)
