import sys


def create_dict(thing):
    new = {}
    while True:
        item = input(f"{thing}: ")
        if item == '':
            break
        if item in new:
            new[item] += 1
        if item not in new:
            new[item] = 1
    return new


def main(input):
    print(create_dict(input))


if __name__ == '__main__':
    main(sys.argv[1])
# :)