def get_list(prompt):
    responses = []
    while True:
        response = input(prompt)
        if response == '':
            break
        responses.append(response)
    return responses


def print_list(header, items, bullet):
    print(header)
    for item in items:
        print(f'{bullet} {item}')


def main():
    visited = get_list("Enter a place you have visited: ")
    dreams = get_list("Enter a destination you want to visit: ")
    print_list("\nI have visited:", visited, "-")
    print_list("\nI want to visit:", dreams, "*")


if __name__ == '__main__':
    main()
