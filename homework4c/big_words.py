import sys


def get_words(minimum):
    words = []
    total = 0
    while True:
        if total == 5:
            break
        word = input("Word: ")
        if len(word) < minimum:
            print("Too short.")
        else:
            words.append(word)
            total += 1
    return words


def printlist(words):
    for w in words:
        print(f"- {w}")


if __name__ == '__main__':
    minimum = int(sys.argv[1])
    words = get_words(minimum)
    printlist(words)
# :)

