def double_words(words):
    new_list = []
    for word in words:
        new_word = word + " " + word
        new_list.append(new_word)
    return new_list


def print_words(words):
    for word in words:
        print(f"- {word}")


def main():
    words = ['really', 'very', 'so', 'crazy']
    doubled = double_words(words)
    print_words(doubled)


if __name__ == '__main__':
    main()
