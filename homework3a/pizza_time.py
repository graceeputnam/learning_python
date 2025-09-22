

def get_name():
    return input('What is your name? ')


def get_pizza():
    return input('What kind of pizza do you want? ')


def get_toppings():
    return input('What toppings do you want? ')


def pizza_time():
    print("Welcome to Papa John's!")
    name = get_name()
    pizza = get_pizza()
    toppings = get_toppings()
    return print(f"{name} wants a {pizza} pizza with {toppings}!")


if __name__ == '__main__':
    pizza_time()
