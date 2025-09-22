def get_list_from_input():
    phrases = []
    while True:
        response = input()
        if not response:
            break
        phrases.append(response)
    return phrases


def most_punctuation(phrases):
    most = ''
    greatest = 0
    for word in phrases:
        total = 0
        for character in word:
            if not character.isalnum() or character.isspace():
                total += 1
        if total > greatest:
            greatest = total
            most = word
    return most


def main():
    print("Enter strings. End with an empty string.")
    phrases = get_list_from_input()
    print(most_punctuation(phrases))


if __name__ == '__main__':
    main()
