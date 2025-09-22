import sys


def product(first, second, third, fourth):
    return float(first* second * third * fourth)


if __name__ == '__main__':
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    third = int(sys.argv[3])
    fourth = int(sys.argv[4])
    print(product(first, second, third, fourth))
# :)
