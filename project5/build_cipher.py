import sys
import string
import random


def make_cipher():
    new = {}
    alphabet = string.ascii_lowercase
    random_alphabet = random.sample(alphabet, len(alphabet))
    for char, letter in zip(alphabet,random_alphabet):
        new[char] = letter
    return new


def make_lines(cipher):
    new = []
    for item in cipher.keys():
        string = f"{item},{cipher[item]}\n"
        new.append(string)
    return new


def write_lines(cool_lines, output):
    with open(output, "w") as file:
        file.writelines(cool_lines)


def main(output):
    cipher_dict = make_cipher()
    cool_lines = make_lines(cipher_dict)
    write_lines(cool_lines, output)


if __name__ == '__main__':
    main(sys.argv[1])

