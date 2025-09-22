import sys


def read_file(file):
    with open(file) as file:
        return file.readlines()


def create_dict(doc_lines, columns):
    new = {}
    for line in doc_lines:
        new_line = line.split(',')
        word = new_line[int(columns)]
        word = word.strip()
        if word in new:
            new[word] += 1
        elif word not in new:
            new[word] = 1
    return new


def main(file, column):
    doc_lines = read_file(file)
    print(create_dict(doc_lines, column))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
# :)
