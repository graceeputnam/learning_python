def menu():
    print()
    print("What would you like to do?")
    print(" 1) Add")
    print(" 2) Subtract")
    print(" 3) Quit")


def get_2():
    num_1 = int(input("Number 1: "))
    num_2 = int(input("Number 2: "))
    return num_1, num_2


def add():
    num_1, num_2 = get_2()
    print(num_1 + num_2)


def subtract():
    num_1, num_2 = get_2()
    print(num_1 - num_2)


def calculator():
    while True:
        menu()
        response = input("Option: ")
        if response == "1":
            add()
        elif response == "2":
            subtract()
        elif response == "3":
            break
        else:
            print(f"Unrecognized response: {response}")


if __name__ == '__main__':
    calculator()
