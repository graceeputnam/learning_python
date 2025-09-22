def doubles(text):
    new_text = text.replace("oo", "oooooo")
    newer_text = new_text.replace("ee", "eeeeee")
    return newer_text


if __name__ == '__main__':
    print(doubles(input("Enter a string: ")))
