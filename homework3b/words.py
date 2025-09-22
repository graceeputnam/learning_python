def play(secret_word):
    while True:
        guess = input("Guess a word: ")
        if secret_word > guess:
            print("Higher!")
        elif secret_word < guess:
            print("Lower!")
        elif secret_word == guess:
            print("You got it!")
            break


if __name__ == '__main__':
    secret_word = input('Enter a secret word: ')
    play(secret_word)
