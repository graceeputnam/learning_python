import sys


def read_text(input):
    with open(input) as file:
        return file.read()


def make_dict(doc):
    new = {}
    for char in doc:
        char = char.lower()
        if char not in new:
            new[char] = 0
        if char in new:
            new[char] = new[char] + 1
    for key in new.keys():
        new[key] = round((new[key]/(len(doc))), 3)
    return new


def main(input):
    doc = read_text(input)
    dict = make_dict(doc)
    print(dict)


if __name__ == '__main__':
    main(sys.argv[1])
# :)
