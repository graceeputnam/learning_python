from byubit import Bit


def paint_row(bit):
    bit.right()
    while bit.front_clear():
        if not bit.is_empty():
            line_color = bit.get_color()
            bit.move()
            while bit.is_empty():
                bit.paint(line_color)
                bit.move()
        bit.move()
    get_back(bit)


def get_back(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()


@Bit.worlds('more-lines', 'more-lines2')
def run(bit):
    bit.left()
    while bit.front_clear():
        paint_row(bit)
        bit.move()
    paint_row(bit)
    get_back(bit)


if __name__ == '__main__':
    run(Bit.new_bit)

