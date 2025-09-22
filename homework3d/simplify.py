def get_words():
    responses = []
    while True:
        response = input("Enter a word: ")
        if response == '':
            break
        responses.append(response)
    return responses


def filter_words(words, max):
    new_list = []
    for word in words:
        if len(word) <= max:
            new_list.append(word)
    return new_list


def print_list(words):
    count = 0
    for word in words:
        count = count + 1
    print(f"There are {count} short words:")
    for word in words:
        print(f"- {word}")


def main():
    words = get_words()
    max_len = int(input("Enter a length: "))
    filtered = filter_words(words, max_len)
    print_list(filtered)


if __name__ == '__main__':
    main()
