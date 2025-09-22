def want_items(out):
    print(f"What items would you like to purchase?")
    list = []
    while True:
        item = input("Item: ")
        if item == '':
            break
        for thing in out:
            if thing == item:
                print(f"I'm sorry, the item {item.upper()} is out of stock.")
                item = ''
        if not item == '':
            list.append(item)
    return list


def get_items():
    print(f"What items are out of stock?")
    list = []
    while True:
        item = input("Item: ")
        if item == '':
            break
        list.append(item)
    return list


def print_items(purchase):
    total = 0
    for item in purchase:
        total += 1
    print(f"You have {total} items:")
    for item in purchase:
        print(f"- {item}")


def main():
    out = get_items()
    purchase = want_items(out)
    print_items(purchase)


if __name__ == '__main__':
    main()# :)
