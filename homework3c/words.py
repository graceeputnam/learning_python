def get_words():
    responses = []
    while True:
        response = input("Word: ")
        if response == '':
            break
        responses.append(response)
    return responses


def get_boundary():
    return input("Boundary: ")


def word_length(words):
    print(f"You have {str(len(words))} words")


def small_words(words, boundary):
    print("These are small:")
    for word in words:
        if word < boundary:
            print(word)


def big_words(words, boundary):
    print("These are big:")
    for word in words:
        if word > boundary:
            print(word)


def main():
    words = get_words()
    boundary = get_boundary()
    word_length(words)
    small_words(words, boundary)
    big_words(words, boundary)


if __name__ == '__main__':
    main()
