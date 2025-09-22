from byubit import Bit


def start_of_garden(bit):
    if not bit.is_green():
        return True
    return False


def get_to_garden(bit):
    while start_of_garden(bit):
        bit.move()


def clear_rocks(bit):
    bit.move()
    while not bit.is_green():
        if bit.is_blue():
            bit.erase()
            bit.move()
        else:
            bit.move()


def get_to_end(bit):
    while bit.front_clear():
        bit.move()


@Bit.worlds('remove-rocks', 'remove-rocks2')
def run(bit):
    get_to_garden(bit)
    clear_rocks(bit)
    get_to_end(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
