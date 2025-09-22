from byubit import Bit


def paint_row(bit,color):
    while bit.can_move_front():
        bit.move()
        bit.paint(color)


def paint_green(bit):
    color = "green"
    bit.paint(color)
    bit.right()
    paint_row(bit, color)
    bit.paint(color)
    get_back(bit)
    bit.right()


def paint_blue(bit):
    color = "blue"
    bit.paint(color)
    bit.left()
    paint_row(bit, color)
    bit.paint(color)
    get_back(bit)
    bit.left()


def get_back(bit):
    bit.left()
    bit.left()
    while bit.can_move_front():
        bit.move()


def check_for_rows(bit):
    if not bit.can_move_left():
        paint_green(bit)
    elif not bit.can_move_right():
        paint_blue(bit)


@Bit.worlds('up-and-down', 'down-and-up')
def run(bit: Bit):
    while bit.front_clear():
        check_for_rows(bit)
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
