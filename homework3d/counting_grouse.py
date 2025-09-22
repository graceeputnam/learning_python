def get_words():
    responses = []
    while True:
        response = input("Enter an observation count: ")
        if response == "":
            break
        responses.append(response)
    return responses


def add_em(observation):
    total = 0
    for number in observation:
        total = total + int(number)
    return total


def smallest(observation):
    smallest = None
    for number in observation:
        if smallest == None:
            smallest = int(number)
        elif int(number) < smallest:
            smallest = int(number)
    return print(f"The smallest count is: {smallest}")


def biggest(observation):
    biggest = 0
    for number in observation:
        if int(number) > biggest:
            biggest = int(number)
    return print(f"The largest count is: {biggest}")


def estimate_factor(factor, counts):
    print("The estimated grouse populations are:")
    for i in counts:
        estimate = int(i) * factor
        print(f"- {estimate}")


def main():
    observation = get_words()
    print(f"There are {add_em(observation)} total grouse.")
    smallest(observation)
    biggest(observation)
    factor = int(input("Enter factor: "))
    estimate_factor(factor, observation)


if __name__ == '__main__':
    main()
