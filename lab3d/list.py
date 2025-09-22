def pattern(fruit):
    total = 0
    for fruits in fruit:
        total = total + 1
    return print(total)


def main():
    fruits = ['apple', 'pear', 'banana', 'plum', 'pineapple']
    pattern(fruits)

if __name__ == '__main__':
    main()