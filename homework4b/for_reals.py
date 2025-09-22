def for_reals(text):
    new_text = text.replace('%', ' percent')
    newer_text = new_text.replace('!', ' (for reals).')
    return newer_text


if __name__ == '__main__':
    print(for_reals(input("Enter a string: ")))
