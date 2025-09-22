from byubit import Bit


def get_to_green_square(bit):
    while not bit.is_green():
        bit.move()


def turn_dots_blue(bit):
    if bit.is_red():
        bit.paint("blue")


@Bit.worlds('fix-reds')
def run(bit):
    get_to_green_square(bit)
    while bit.front_clear():
        bit.move()
        turn_dots_blue(bit)


if __name__ == '__main__':
    run(Bit.new_bit)

