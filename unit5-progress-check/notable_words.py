import sys
from string import punctuation


def read_file(file):
    with open(file) as file:
        return file.read()


def create_dict(doc):
    new = {}
    doc = doc.split()
    for word in doc:
        word = word.strip(punctuation)
        if word not in new:
            new[word] = 0
        if word in new:
            new[word] += 1
    return new


def print_correct(dict, count):
    for key in dict.keys():
        if dict[key] == int(count):
            print(f"{key}: {count}")


def main(file, word_count):
    doc = read_file(file)
    dict = create_dict(doc)
    print_correct(dict, word_count)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

