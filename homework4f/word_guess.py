import sys
import random


def choose_word(lines):
    return random.choice(lines)


def guess_word(word):
    while True:
        guess = input("Guess a word: ")
        if guess == word:
            print("That's it!")
            break
        elif guess in word:
            print("almost")
            continue
        for char in guess:
            if char in word:
                print("close")
                break
        else:
            print("nope")


def read_file(input):
    list1 = []
    with open(input) as file:
        return file.readlines()


def main(input):
    lines = read_file(input)
    word = choose_word(lines)
    guess_word(word)


if __name__ == '__main__':
    main(sys.argv[1])
# :)
