from byubit import Bit


def barcode(bit):
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint('blue')
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def check_color(bit):
    if bit.is_blue():
        barcode(bit)


@Bit.worlds('barcode', 'barcode2')
def run(bit):
    while bit.front_clear():
        bit.move()
        check_color(bit)


if __name__ == '__main__':
    run(Bit.new_bit)

