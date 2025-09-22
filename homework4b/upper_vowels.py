def upper_vowels(text):
    new = ''
    for char in text:
        if char in "aeiou":
            char = char.upper()
        new += char
    return new


if __name__ == '__main__':
    print(upper_vowels(input("Enter a string: ")))
