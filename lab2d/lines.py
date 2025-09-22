from byubit import Bit


def get_back(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()


def paint_row(bit):
    bit.right()
    while not bit.is_red() and not bit.is_blue() and not bit.is_green():
        bit.move()
    line_color = bit.get_color()
    bit.move()
    while not bit.is_blue() and not bit.is_green() and not bit.is_red():
        bit.paint(line_color)
        bit.move()
    get_back(bit)


@Bit.worlds('lines')
def run(bit):
    bit.left()
    while bit.front_clear():
        paint_row(bit)
        bit.move()
    paint_row(bit)
    get_back(bit)


if __name__ == '__main__':
    run(Bit.new_bit)

