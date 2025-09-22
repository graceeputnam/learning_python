import sys


def read_lines(input):
    with open(input) as file:
        return file.readlines()


def read_text(input):
    with open(input) as file:
        return file.read()


def make_dict(lines):
    new = {}
    for line in lines:
        new_line = line.split(',')
        new[new_line[0]] = new_line[1].strip()
    return new


def make_lines(cipher_dict, doc):
    new_doc = ''
    for char in doc:
        if char in cipher_dict:
            char = cipher_dict[char]
        elif char.isupper():
            test_char = char.lower()
            if test_char in cipher_dict:
                char = cipher_dict[test_char].upper()
        new_doc += char
    return new_doc


def write_lines(cool_lines, output):
    with open(output, "w") as file:
        file.write(cool_lines)


def main(sub_cipher, input, output):
    lines = read_lines(sub_cipher)
    cipher_dict = make_dict(lines)
    doc = read_text(input)
    cool_lines = make_lines(cipher_dict, doc)
    write_lines(cool_lines, output)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])

