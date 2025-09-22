import sys


def search_words(input, word):
    have_word = []
    have_substring = []
    for line in input:
        new_line = line.split()
        for item in new_line:
            if item == word:
                have_word.append(line)
                break
            elif word in item:
                have_substring.append(line)
                break
    return have_word, have_substring


def print_lines(lines, word, secret):
    total = 0
    for item in lines:
        total += 1
    print(f"{total} lines had the {word} '{secret}':")
    for item in lines:
        print(f"- {item}\n")


def readlines(filename):
    with open(filename) as file:
        return file.readlines()


def main(input, word):
    lines = readlines(input)
    have_word, have_substring = search_words(lines, word)
    print_lines(have_word, "word", word)
    print_lines(have_substring, "substring", word)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
#  :)
