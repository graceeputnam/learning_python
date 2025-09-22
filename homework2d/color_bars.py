from byubit import Bit


def paint_line(bit):
    line_color = bit.get_color()
    bit.left()
    while bit.front_clear():
        bit.paint(line_color)
        bit.move()
    bit.paint(line_color)


def back_down(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('color-bars', 'color-bars2')
def run(bit):
    while bit.front_clear():
        paint_line(bit)
        back_down(bit)
        bit.move()
    paint_line(bit)
    back_down(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
