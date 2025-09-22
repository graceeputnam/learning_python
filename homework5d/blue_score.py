from string import punctuation


def blue_score(phrases):
    new = {}
    blue = ["byu", "cougar", "cougars", "blue"]
    for phrase in phrases:
        new_phrase = phrase.split()
        total = 0
        for word in new_phrase:
            new_word = word.lower()
            new_word = new_word.strip(punctuation)
            if new_word in blue:
                total += 1
        if total in new:
            new[total].append(phrase)
        elif total not in new:
            new[total] = []
            new[total].append(phrase)
    return new


def print_dict(dict):
    for item in dict.keys():
        print(f"{item}:")
        for phrase in dict[item]:
            print(f"{phrase}")
        print()


def get_phrases():
    new = []
    while True:
        phrase = input("Phrase: ")
        if phrase == '':
            break
        new.append(phrase)
    return new


def main():
    phrases = get_phrases()
    blue_dict = blue_score(phrases)
    print_dict(blue_dict)


if __name__ == "__main__":
    main()

