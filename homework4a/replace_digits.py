def replace_digits_with_asterisks(string):
    new_string = ""
    for character in string:
        if character.isdigit():
            new_string += "*"
        else:
            new_string += character
    return new_string


def main():
    response = input("Enter a string: ")
    print(replace_digits_with_asterisks(response))


if __name__ == '__main__':
    main()
