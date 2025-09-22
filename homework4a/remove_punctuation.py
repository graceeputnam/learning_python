def remove_punctuation(string):
    new = ''
    for character in string:
        if character.isalnum() or character.isspace():
            new += character
    return new


def main():
    response = input("Enter a string: ")
    print(remove_punctuation(response))


if __name__ == '__main__':
    main()
