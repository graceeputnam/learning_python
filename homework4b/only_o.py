def only_o(text):
    new = ''
    for char in text:
        if char in "aeiouAEIOU":
            if char.isupper():
                char = 'O'
            else:
                char = 'o'
        new += char
    return new


if __name__ == '__main__':
    print(only_o(input("Enter a string: ")))
