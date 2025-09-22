
import random


def choose_quote(lines):
    return random.choice(lines)


def compare_words(word_1, word_2):
    new_string = ""
    for char_1, char_2 in zip(word_1, word_2):
        if char_1 == char_2:
            new_string += "*"
        else:
            new_string += "."
    print(new_string)


def main():
    while True:
        word_1 = input("Word 1: ")
        if word_1 == "":
            break
        word_2 = input("Word 2: ")
        compare_words(word_1, word_2)


if __name__ == '__main__':
    main()
# :)

