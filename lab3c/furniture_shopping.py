def get_numbers(prompt):
    responses = []
    while True:
        response = input(prompt)
        if response == '':
            break
        responses.append(int(response))
    return responses


def print_smaller(numbers, boundary):
    for item in numbers:
        if item < boundary:
            print(f"- ${item}")


def main():
    print("Let's find you some tables and chairs!")
    total_budget = int(input("First, what is your total budget? "))

    print()
    print("Sweet! Now let me know what your table options are.")
    options = get_numbers("Enter the price of a table: ")

    print()
    print("Next, let me know what your chair options are.")
    chair_options = get_numbers("Enter the price of a set of chairs: ")

    print()
    print(f"Since your total budget is ${total_budget}, you can afford the tables that cost: ")
    print_smaller(options, total_budget)

    table_cost = int(input("Which table do you want? "))
    chair_budget = total_budget - table_cost

    print()
    print(f"That means that your chair budget is ${chair_budget}.")
    print("You can afford chairs that cost: ")
    print_smaller(chair_options, chair_budget)


if __name__ == "__main__":
    main()
