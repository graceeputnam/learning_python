import sys
from string import punctuation


def make_filter(words):
    filter = {}
    words = words.split()
    for word in words:
        word = word.strip()
        word = word.strip(punctuation)
        word = word.lower()
        if word not in filter:
            filter[word] = 0
        if word in filter:
            filter[word] += 1
    return filter


def remove_words(words, filter, threshold):
    new = ""
    words = words.split()
    for word in words:
        word = word.strip()
        word = word.strip(punctuation)
        word = word.lower()
        if filter[word] >= int(threshold):
            continue
        else:
            new += word + " "
    return new


def read_content(filename):
    with open(filename) as file:
        return file.read()


def write_content(filename, content):
    with open(filename, 'w') as file:
        content = content.strip()
        file.write(content)


def main(threshold, file, output):
    words = read_content(file)
    filter = make_filter(words)
    print(filter)
    new_words = remove_words(words, filter, threshold)
    write_content(output, new_words)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
