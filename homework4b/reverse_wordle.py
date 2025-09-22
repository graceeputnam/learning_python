
def substitue_letters(blocked, replacement):
    while True:
        word = input("Word: ")
        if word == '':
            break
        new_word = ''
        for char in word:
            if char in blocked or char in blocked.upper():
                char = replacement
            new_word += char
        print(new_word)


def main():
    blocked = input("Characters to block: ")
    replacement = input("Replacement: ")
    substitue_letters(blocked, replacement)


if __name__ == '__main__':
    main()
# :)
