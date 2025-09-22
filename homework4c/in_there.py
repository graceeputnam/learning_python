import sys


def guess(short):
    while True:
        response = input("Guess: ")
        if response == short:
            print("You got it!")
            break
        elif short in response:
            print("It's in there...")
        else:
            print("Nope.")


if __name__ == '__main__':
    short = sys.argv[1]
    guess(short)
# :)
