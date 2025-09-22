def get_foods(type):
    responses = []
    while True:
        response = input(f"Enter a {type}: ")
        if response == '':
            break
        responses.append(response)
    return responses


def print_veggies(veggies):
    print("Vegetables:")
    for veggie in veggies:
        print(f" - {veggie}")


def print_fruits(fruits):
    print("Fruits:")
    for fruit in fruits:
        print(f" - {fruit}")


def check_for_diet(fruits, veggies):
    if len(fruits) > len(veggies):
        print_fruits(fruits)
        print_veggies(veggies)
        print("You need more vegetables!")
    elif len(veggies) > len(fruits):
        print_veggies(veggies)
        print_fruits(fruits)
        print("You need more fruit!")
    elif len(veggies) == len(fruits):
        print_fruits(fruits)
        print_veggies(veggies)
        print("What a healthy balanced diet!")


def main():
    fruits = get_foods("Fruit")
    veggies = get_foods("Vegetable")
    check_for_diet(fruits, veggies)


if __name__ == '__main__':
    main()
