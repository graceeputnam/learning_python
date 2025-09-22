def get_list(prompt):
    responses = []
    while True:
        response = input(prompt)
        if response == '':
            break
        responses.append(response)
    return responses


def print_list(items, bullets):
    for bullet in bullets:
        print()
        for item in items:
            print(f'{bullet} {item}')
    print()


def main():
    movies = get_list("Item: ")
    print()
    bullets = get_list("Custom Bullet Point: ")
    print_list(movies, bullets)


if __name__ == '__main__':
    main()
