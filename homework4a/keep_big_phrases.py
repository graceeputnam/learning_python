def get_list_from_input():
    phrases = []
    while True:
        response = input()
        if not response:
            break
        phrases.append(response)
    return phrases


def keep_big_phrases(phrases):
    new = []
    for word in phrases:
        total = 0
        for char in word:
            if char.isupper():
                total += 1
        if total > 3:
            new.append(word)
    return new


def main():
    print("Enter strings. End with an empty string.")
    phrases = get_list_from_input()
    print(keep_big_phrases(phrases))


if __name__ == '__main__':
    main()
