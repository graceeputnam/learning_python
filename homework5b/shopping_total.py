import sys


def read_file(input):
    with open(input) as file:
        return file.readlines()


def create_price_list(prices):
    price_dict = {}
    for price in prices:
        new_price = price.split(",")
        new_price[1] = new_price[1].strip()
        price_dict[new_price[0]] = new_price[1]
    return price_dict


def find_price(items, price):
    total = 0
    for item in items.keys():
        total += float(price[item]) * float(items[item])
    total = round(total, 2)
    print(f"The total is ${total}")


def main(input, pricelist):
    cart = read_file(input)
    prices = read_file(pricelist)
    price = create_price_list(prices)
    items = create_price_list(cart)
    find_price(items, price)


if __name__ == '__main__':
   main(sys.argv[1], sys.argv[2])
# :)
