def count_whitespace(string):
    total = 0
    for character in string:
        if character.isspace():
            total = total + 1
    return total


def main():
    response = input("Enter a string: ")
    print(count_whitespace(response))


if __name__ == '__main__':
    main()
