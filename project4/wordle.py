import sys
import random


def check_for_same(guess, random_word):
    new = ""
    for char, wchar in zip(guess, random_word):
        if char == wchar:
            new += "!"
        elif char in random_word:
            new += "?"
        else:
            new += "*"
    return new


def guess_word(word, guesses):
    random_word = random.choice(word)
    for i in range(int(guesses)):
        guess = input(f"Guess # {i+1}: \n")
        new = check_for_same(guess, random_word)
        print(new)
        if new == "!" * len(new):
            print("Way to go!")
            break
    if not new == "!"*len(new):
        print(f"Maybe next time. The answer is {random_word.strip()}.")


def read_file(input):
    list1 = []
    with open(input) as file:
        return file.readlines()


def main(input, guesses):
    lines = read_file(input)
    guess_word(lines, guesses)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
# :)
