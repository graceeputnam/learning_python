from string import punctuation
import sys


def scan_words(words):
    new = {}
    words_split = words.split()
    for items in words_split:
        new_item = items.lower().strip(punctuation)
        char_count = 0
        for char in new_item:
            char_count += 1
        first_char = new_item[0].strip()
        key = f"({char_count}, '{first_char}')"
        if key not in new:
            new[key] = []
        if key in new:
            new[key].append(new_item)
    return new


def read_file(file):
    with open(file) as file:
        return file.read()


def print_dict(dict):
    for key in dict.keys():
        print(f"{key}: {dict[key]}")


def main(input):
    words = read_file(input)
    word_dict = scan_words(words)
    print_dict(word_dict)


if __name__ == "__main__":
    main(sys.argv[1])
# :)
