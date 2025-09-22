from byubit import Bit


def check_color(bit):
    if bit.is_blue():
        bit.erase()
    else:
        bit.paint("blue")


def up_and_down(bit):
    bit.left()
    while bit.can_move_front():
        check_color(bit)
        bit.move()
    check_color(bit)
    bit.right()
    bit.right()
    while bit.can_move_front():
        bit.move()
    bit.left()


@Bit.worlds('invert', 'invert2')
def run(bit):
    while bit.can_move_front():
        up_and_down(bit)
        bit.move()
    up_and_down(bit)


if __name__ == '__main__':
    run(Bit.new_bit)

